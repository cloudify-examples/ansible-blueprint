#!/usr/bin/env python

import os
import tempfile
import subprocess

from cloudify import ctx
from cloudify.state import ctx_parameters as inputs
from cloudify.exceptions import NonRecoverableError, OperationRetry


def get_config():
    ctx.logger.info('Getting config from properties, runtime_properties, and inputs.')
    _config = ctx.node.properties.get('resource_config', {})
    _config.update(
        ctx.instance.runtime_properties.get('resource_config', {}))
    _config.update(inputs.get('resource_config', {}))
    return _config


def get_rendered_file(_p, _v):

    _, _temporary_file_path = tempfile.mkstemp()

    _rendered_file = \
        ctx.download_resource_and_render(
            _p,
            target_path=_temporary_file_path,
            template_variables=_v or None)

    return _rendered_file


if __name__ == '__main__':

    config = get_config()
    target_path = config.get('target_path')
    target_path_dir = os.path.dirname(target_path)
    if not os.path.exists(target_path_dir):
        raise OperationRetry('{0} does not exist'.format(target_path_dir))

    resource_path = config.get('resource_path')
    if not resource_path:
        raise NonRecoverableError('not resource_path')

    template_variables = config.get('template_variables')
    temporary_file_path = get_rendered_file(resource_path, template_variables)

    ctx.logger.info("Moving things into place")

    try:
        os.rename(temporary_file_path, target_path)
    except OSError:
        command = 'sudo mv {0} {1}'.format(temporary_file_path, target_path)
        subprocess_args = {
            'args': command.split(),
            'stdout': subprocess.PIPE,
            'stderr': subprocess.PIPE
        }
        ctx.logger.debug('subprocess_args {0}.'.format(subprocess_args))
        process = subprocess.Popen(**subprocess_args)
        output, error = process.communicate()
        if process.returncode:
            raise OperationRetry(
                'Running `{0}` returns error `{1}`.'.format(command, error))
