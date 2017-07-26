[![Build Status](https://circleci.com/gh/cloudify-examples/ansible-blueprint.svg?style=shield&circle-token=:circle-token)](https://circleci.com/gh/cloudify-examples/ansible-blueprint)

# Ansible Blueprint
An example Ansible Blueprint.

## Notes

* This is a community contributed example.
* Tested with Cloudify 4.1

*Installation:*

0. [Setup](https://github.com/cloudify-examples/cloudify-environment-setup) your Cloudify environment.
1. Run `cfy install aws-blueprint.yaml -b demo` or `cfy install openstack-blueprint.yaml -b demo`.
2. Run `cfy deployments outputs demo`
3. Visit the URL in the outputs.

*Uninstallation:*

1. Run `cfy uninstall --allow-custom-parameters -p ignore_failure=true demo`

