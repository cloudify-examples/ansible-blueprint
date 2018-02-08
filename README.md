[![Build Status](https://circleci.com/gh/cloudify-examples/ansible-blueprint.svg?style=shield&circle-token=:circle-token)](https://circleci.com/gh/cloudify-examples/ansible-blueprint)

# Ansible Blueprint
An example Ansible Blueprint.

## Compatibility

Tested with:
  * Cloudify 4.2

## Pre-installation steps

Upload the required plugins:

  * [Openstack Plugin](https://github.com/cloudify-cosmo/cloudify-openstack-plugin/releases).
  * [AWSSDK Plugin](https://github.com/cloudify-incubator/cloudify-awssdk-plugin/releases).
  * [AWS Plugin](https://github.com/cloudify-cosmo/cloudify-aws-plugin/releases).
  * [GCP Plugin](https://github.com/cloudify-incubator/cloudify-gcp-plugin/releases).
  * [Azure Plugin](https://github.com/cloudify-incubator/cloudify-azure-plugin/releases).
  * [Utilities Plugin](https://github.com/cloudify-incubator/cloudify-utilities-plugin/releases).
  * [Fabric Plugin](https://github.com/cloudify-cosmo/cloudify-fabric-plugin/releases).

_Check the blueprint for the latest version of the plugin._

Install the relevant example network blueprint for the IaaS that you wish to deploy on:

  * [Openstack Example Network](https://github.com/cloudify-examples/openstack-example-network)
  * [AWS Example Network](https://github.com/cloudify-examples/aws-example-network)
  * [GCP Example Network](https://github.com/cloudify-examples/gcp-example-network)
  * [Azure Example Network](https://github.com/cloudify-examples/azure-example-network)

## Installation

On your Cloudify Manager, navigate to `Local Blueprints` select `Upload`.

[Right-click and copy URL](https://github.com/cloudify-examples/ansible-blueprint/archive/master.zip). Paste the URL where it says `Enter blueprint url`. Provide a blueprint name, such as `ansible` in the field labeled `blueprint name`.

Select the blueprint for the relevant IaaS you wish to deploy on, for example `openstack.yaml` from `Blueprint filename` menu. Click `Upload`.

After the new blueprint has been created, click the `Deploy` button.

Navigate to `Deployments`, find your new deployment, select `Install` from the `workflow`'s menu. At this stage, you may provide your own values for any of the default `deployment inputs`.


## Uninstallation

Navigate to the deployment and select `Uninstall`. When the uninstall workflow is finished, select `Delete deployment`.
