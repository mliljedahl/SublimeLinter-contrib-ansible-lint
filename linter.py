#
# linter.py
# Linter for SublimeLinter3, a code checking framework for Sublime Text 3
#
# Written by Markus Liljedahl
# Copyright (c) 2017 Markus Liljedahl
#
# License: MIT
#

"""This module exports the AnsibleLint plugin class."""

from SublimeLinter.lint import Linter, util


class AnsibleLint(Linter):
    """Provides an interface to ansible-lint."""

    syntax = 'ansible'
    cmd = ('ansible-lint', '-p', '--nocolor', '@')
    executable = None
    version_args = '--version'
    version_re = r'(?P<version>\d+\.\d+\.\d+)'
    version_requirement = '>= 3.0.1'
    regex = r'.+:(?P<line>\d+):.+\] (?P<message>.+)'
    multiline = True
    line_col_base = (1, 1)
    tempfile_suffix = 'yml'
    error_stream = util.STREAM_STDOUT
    selectors = {}
    word_re = None
    defaults = {
        '-r:,': '',
        '-R:,': '',
        '-t:,': '',
        '-x:,': '',
        '--exclude=,': ''
    }
    inline_settings = ('r', 'R', 't', 'x', 'exclude')
    inline_overrides = ('r', 'R', 't', 'x', 'exclude')
    comment_re = r'\s*#'