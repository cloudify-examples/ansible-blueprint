[![Build Status](https://circleci.com/gh/cloudify-examples/ansible-blueprint.svg?style=shield&circle-token=:circle-token)](https://circleci.com/gh/cloudify-examples/ansible-blueprint)

# cloudify-nodecellar-example-ansible
A spin on the Cloudify-Nodecellar-Example using Ansible instead of bash scripts.

## Notes

* This is a community contributed example.
* Tested with Cloudify 3.3m4, Cloudify 3.4 and 4.0

## Prerequisites for non-local ##

+ OpenStack manager/ AWS manager
+ GCC installed on your manager (OpenStack only)

## Instructions

1) upload the blueprint (openstack/ aws) to your manager:
```
cfy blueprints upload ../ansible-bluprint/youre-manager-ansible-blueprint.yaml -b ansible
```

2) create a deployment based on your blueprint inputs file:
```
cfy deployments create -b ansible -i ../ansible-bluprint/inputs/youre-manager-ansible-blueprint-inputs.yaml
```

3) start the install workflow:
```
cfy executions start -d ansible install
```

## Local instructions

Download the Vagrant Box from GetCloudify.org:
Cloudify 3.3m4- http://getcloudify.org/guide/3.2/quickstart.html#important-before-you-begin.
Cloudify 3.4- http://docs.getcloudify.org/3.4.1/manager/getting-started/

These simple commands should start the deployment on your vagrant machine:

```
1) cd /vagrant
```

```
2) git clone https://github.com/cloudify-examples/cloudify-nodecellar-example-ansible.git
```

```
3) cd cloudify-nodecellar-example-ansible
```

```
4) git checkout {branch or tag id}
```

```
5) cfy local init --install-plugins -p local-ansible-blueprint.yaml -i inputs/local.yaml.template
```

```
6) cfy local execute -w install
```

