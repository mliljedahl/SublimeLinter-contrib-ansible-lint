#
# linter.py
# Linter for SublimeLinter4, a code checking framework for Sublime Text 3
#
# Written by Markus Liljedahl
# Copyright (c) 2017 Markus Liljedahl
#
# License: MIT
#

"""This module exports the AnsibleLint plugin class."""

from SublimeLinter.lint import Linter, util
from distutils.version import LooseVersion
import re
import os
import subprocess
from subprocess import PIPE


class AnsibleLint(Linter):
    """Provides an interface to ansible-lint."""

    # linter settings
    cmd = ('ansible-lint', '${args}', '${file}')
    regex = r'(?P<filename>^.+):(?P<line>\d+): \[.(?P<error>.+)\] (?P<message>.+)'

    # -p generate non-multi-line, pep8 compatible output
    multiline = False

    # ansible-lint does not support column number
    word_re = False
    line_col_base = (1, 1)

    tempfile_suffix = 'yml'
    error_stream = util.STREAM_STDOUT

    defaults = {
        'selector': 'source.ansible',
        'args': '--nocolor -p',
        '--exclude= +': ['.galaxy'],
        '-c': '',
        '-r': '',
        '-R': '',
        '-t': '',
        '-x': '',
    }

    def __init__(self, view, settings):
        """If it uses Ansible Lint 5 will be updated the regex."""
        super(AnsibleLint, self).__init__(view, settings)

        # Must be resolved the path of Ansible Lint and Ansible if you'd like to use Ansible Lint 5.
        # Because the ansible will be called from Ansible Lint 5 in parsing playbook codes.
        # If the path doesn't resolve, an error for Ansible occurs when Ansible Lint execution.
        env = os.environ.copy()
        env_setting = self.settings.get('env', {})
        if env_setting and 'PATH' in env_setting.keys():
            env['PATH'] = env['PATH'] + ':%s' % env_setting['PATH']

        # version gets of Ansible Lint
        try:
            proc = subprocess.Popen(['ansible-lint', '--version'], env=env, stdout=PIPE, stdin=PIPE)
            result = proc.communicate()[0].decode('utf-8')
            ansible_version = re.findall(r'ansible-lint (\d+.\d+.\d+)', result)[0]
        except Exception:
            ansible_version = None

        # regex to re-set if Ansible Lint version is 5 or more
        if ansible_version and LooseVersion(ansible_version) >= ('5.0.0'):
            regex = r'(?P<filename>^.+):(?P<line>\d+): (?P<message>.+)'
            self.regex = re.compile(regex, self.re_flags)
