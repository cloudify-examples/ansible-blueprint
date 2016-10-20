[![Build Status](https://circleci.com/gh/cloudify-examples/ansible-blueprint.svg?style=shield&circle-token=:circle-token)](https://circleci.com/gh/cloudify-examples/ansible-blueprint)

# cloudify-nodecellar-example-ansible
A spin on the Cloudify-Nodecellar-Example using Ansible instead of bash scripts.

## Notes

* This is a community contributed example.
* Tested only with Cloudify 3.3m4

## Instructions

Download the Vagrant Box from GetCloudify.org: http://getcloudify.org/guide/3.2/quickstart.html#important-before-you-begin.

These simple commands should start the deployment on your vagrant machine:

`
  cd /vagrant
`
`
  git clone https://github.com/cloudify-examples/cloudify-nodecellar-example-ansible.git
`

`
  cd cloudify-nodecellar-example-ansible
`

`
  git checkout {branch or tag id}
`

`
  cfy local init --install-plugins -p local-ansible-blueprint.yaml -i inputs/local.yaml.template
`

`
  cfy local execute -w install
`

