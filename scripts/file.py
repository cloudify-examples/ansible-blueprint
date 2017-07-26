#!/usr/bin/env python

import os
import tempfile
import subprocess

from cloudify import ctx
from cloudify.state import ctx_parameters as inputs
from cloudify.exceptions import OperationRetry


def execute(_command):

    subprocess_args = {
        'args': _command.split(),
        'stdout': subprocess.PIPE,
        'stderr': subprocess.PIPE
    }
    ctx.logger.debug('subprocess_args {0}.'.format(subprocess_args))
    process = subprocess.Popen(**subprocess_args)
    output, error = process.communicate()
    if process.returncode:
        raise OperationRetry(
            'Running `{0}` returns error `{1}`.'.format(command, error))
    return process


def get_resource_config():
    ctx.logger.info('Getting config from properties, runtime_properties, and inputs.')
    _config = ctx.node.properties.get('resource_config', {})
    _config.update(
        ctx.instance.runtime_properties.get('resource_config', {}))
    _config.update(inputs.get('resource_config', {}))
    return _config


if __name__ == '__main__':

    resource_config = get_resource_config()
    file_path = resource_config.get('file_path')
    file_content = resource_config.get('file_content')
    file_permissions = resource_config.get('file_permissions')

    _, temporary_file_path = tempfile.mkstemp()
    with open(temporary_file_path, 'w') as outfile:
        outfile.write(file_content)
    try:
        os.rename(temporary_file_path, file_path)
        command = 'chmod {0} {1}'.format(file_permissions, file_path)
        execute(command)
    except OSError:
        command = 'sudo mv {0} {1}'.format(temporary_file_path, file_path)
        execute(command)
        command = 'sudo chmod {0} {1}'.format(file_permissions, file_path)
        execute(command)

