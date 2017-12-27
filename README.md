[![Build Status](https://circleci.com/gh/cloudify-examples/ansible-blueprint.svg?style=shield&circle-token=:circle-token)](https://circleci.com/gh/cloudify-examples/ansible-blueprint)

# Ansible Blueprint

Demonstrates working with Cloudify and Ansible.

*Requirements:*

- Cloudify Manager
- AWS or Openstack
- Fabric, Utilities, Diamond, and AWS or Openstack Plugins.
- Environment-specific secrets. See [Cloudify Environment Setup](https://github.com/cloudify-examples/cloudify-environment-setup)

This is an example. It creates a new Ansible server, however in most scenarios, you will already have your own Ansible environment. Most of the integration points (uploading playbooks, parsing and updating inventories) will be the same.


*Installation:*

0. [Setup](https://github.com/cloudify-examples/cloudify-environment-setup) your Cloudify environment.
1. Run `cfy install aws-blueprint.yaml -b demo` or `cfy install openstack-blueprint.yaml -b demo`.
2. Run `cfy deployments outputs demo`
3. Visit the URL in the outputs.

*Uninstallation:*

1. Run `cfy uninstall --allow-custom-parameters -p ignore_failure=true demo`
