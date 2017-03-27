#!/bin/bash -e

ctx logger info "installing ansible"

# Make sure that ansible exists in the virtualenv
set -e
if ! type ansible > /dev/null; then
    pip install ansible
    ctx logger info "installed ansible"
fi
set +e

TEMP_DIR='/tmp'
ANSIBLE_DIRECTORY=${TEMP_DIR}/$(ctx execution-id)/ansible
FILENAME=$(ctx node properties playbook_file_name)
PLAYBOOK_PATH=${ANSIBLE_DIRECTORY}/${FILENAME}

mkdir -p ${ANSIBLE_DIRECTORY}/roles

# Download and Move the Default Ansible Config in place
TEMP_CONF_PATH=$(ctx download-resource-and-render resources/ansible.cfg)
ctx logger info "downloaded resource to ${TEMP_CONF_PATH}"
CONF_PATH=$ANSIBLE_DIRECTORY/ansible.cfg
cp $TEMP_CONF_PATH $CONF_PATH
ctx logger info "copied ${TEMP_CONF_PATH} ${CONF_PATH}"
export ANSIBLE_CONFIG=${CONF_PATH}
ctx instance runtime-properties confpath ${CONF_PATH}

# Add the ansible hostname name to the inventory and to etc hosts
NODE_HOSTNAME=$(ctx node name)
NODE_ADDRESS=$(ctx node properties public_ip)

cat <<EOF > ${ANSIBLE_DIRECTORY}/inventory
$NODE_HOSTNAME
EOF

set -e
if ! ping -c 1 ${NODE_HOSTNAME} > /dev/null; then
    echo "${NODE_ADDRESS} ${NODE_HOSTNAME}" | sudo tee -a /etc/hosts
    ctx logger info "added hostname ${NODE_HOSTNAME}"
fi
set +e

# Download the playbook that will download the roles for the other modules
PLAYBOOK=$(ctx download-resource-and-render resources/${FILENAME})
cp $PLAYBOOK $PLAYBOOK_PATH
ctx logger info "downloaded resource to ${PLAYBOOK_PATH}"
ansible-playbook ${PLAYBOOK_PATH} --connection=paramiko -vvvv > ${ANSIBLE_DIRECTORY}/output.log 2>&1
ctx logger info "executed ${PLAYBOOK_PATH}"
