#!/usr/bin/env python

import os
import tempfile
import subprocess
import ConfigParser
from ConfigParser import DuplicateSectionError

from cloudify import ctx
from cloudify.state import ctx_parameters as inputs
from cloudify.exceptions import OperationRetry


def get_resource_config():
    ctx.logger.info('Getting config from properties, runtime_properties, and inputs.')
    _config = ctx.node.properties.get('resource_config', {})
    _config.update(
        ctx.instance.runtime_properties.get('resource_config', {}))
    _config.update(inputs.get('resource_config', {}))
    return _config



if __name__ == '__main__':

    config_parser = ConfigParser.ConfigParser()

    file_path = ctx.node.properties.get('file_path')
    resource_config = get_resource_config()

    if os.path.exists(file_path):
        config_parser.read(file_path)

    for section, section_config in resource_config.items():
        try:
            config_parser.add_section(section)
        except DuplicateSectionError:
            pass
        if isinstance(section_config, list) or \
                isinstance(section_config, set):
            for li in section_config:
                config_parser.set(section, li)
        elif isinstance(section_config, dict):
            for k, v in section_config.items():
                config_parser.set(section, k, v)


    # Ansible allows something like this:.
    # [Section1]
    # string
    # But this is not supported in ConfigParser.
    # It will look like this:
    # [Section1]
    # string = None
    _, temporary_file_path_non_ansible = tempfile.mkstemp()
    with open(temporary_file_path_non_ansible, 'w') as outfile:
        config_parser.write(outfile)
    _, temporary_file_path = tempfile.mkstemp()
    with open(temporary_file_path_non_ansible, 'r') as infile:
        with open(temporary_file_path, 'w') as outfile:
            for line in infile.readlines():
                split_line = line.split(' = None')
                outfile.writelines(split_line[0])

    try:
        os.rename(temporary_file_path, file_path)
    except OSError:
        command = 'sudo mv {0} {1}'.format(temporary_file_path, file_path)
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
