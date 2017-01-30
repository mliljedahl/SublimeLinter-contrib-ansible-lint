SublimeLinter-contrib-ansible-lint
==================================

[![Build Status](https://travis-ci.org/SublimeLinter/SublimeLinter-contrib-ansible-lint.svg?branch=master)](https://travis-ci.org/SublimeLinter/SublimeLinter-contrib-ansible-lint)

This linter plugin for [SublimeLinter][docs] provides an interface to [ansible-lint](https://github.com/willthames/ansible-lint). It will be used with files that have the “Ansible” syntax.

## Installation
SublimeLinter 3 must be installed in order to use this plugin. If SublimeLinter 3 is not installed, please follow the instructions [here][installation].

### Linter installation
Before using this plugin, you must ensure that `ansible-lint` is installed on your system. To install `ansible-lint`, do the following:

1. Install [Python](http://python.org/download/) and [pip](http://www.pip-installer.org/en/latest/installing.html).

1. Install `ansible-lint` by typing the following in a terminal:
   ```
   [sudo] pip install ansible-lint
   ```

**Note:** This plugin requires `ansible-lint` 3.0.1 or later.

### Syntax installation
Also ensure that [Ansible](https://github.com/clifford-github/sublime-ansible) is installed in Sublime Text. To install `Ansible`, do the following:

To install via Package Control, do the following:

1. Within Sublime Text, bring up the [Command Palette][cmd] and type `install`. Among the commands you should see `Package Control: Install Package`. If that command is not highlighted, use the keyboard or mouse to select it. There will be a pause of a few seconds while Package Control fetches the list of available plugins.

1. When the plugin list appears, type `ansible`. Among the entries you should see `Ansible`. If that entry is not highlighted, use the keyboard or mouse to select it.

**Note:** If `Ansible` syntax is not installed this plugin will not work.

#### Syntax configuration
To be able to automatically open the `.yml` files in an Ansible project with the Ansible syntax, `ApplySyntax` needs to be configured with the settings below. If this is not done the `.yml` files will be opend with the YAML syntax and the linter plugin will not work without manually change the syntax for every file.

The settings can be found under:

```
Sublime Text -> Preferences -> Package Settings -> ApplySyntax -> Settings - User
```

```
    "syntaxes": [{
        "name": "Ansible/Ansible",
        "rules": [
          {"file_name": ".*/tasks/.*.yml$"},
          {"file_name": ".*/handler/.*.yml$"},
          {"file_name": ".*/*_vars/.*.yml$"},
          {"file_name": ".*/roles/.*.yml$"},
          {"file_name": ".*/playbooks/.*.yml$"},
          {"file_name": ".*/.*ansible.*/.*.yml$"}
        ]
      }]
```

### Linter configuration
In order for `ansible-lint` to be executed by SublimeLinter, you must ensure that its path is available to SublimeLinter. Before going any further, please read and follow the steps in [“Finding a linter executable”](http://sublimelinter.readthedocs.org/en/latest/troubleshooting.html#finding-a-linter-executable) through “Validating your PATH” in the documentation.

Once you have installed and configured `ansible-lint`, you can proceed to install the SublimeLinter-contrib-ansible-lint plugin if it is not yet installed.

### Plugin installation
Please use [Package Control][pc] to install the linter plugin. This will ensure that the plugin will be updated when new versions are available. If you want to install from source so you can modify the source code, you probably know what you are doing so we won’t cover that here.

To install via Package Control, do the following:

1. Within Sublime Text, bring up the [Command Palette][cmd] and type `install`. Among the commands you should see `Package Control: Install Package`. If that command is not highlighted, use the keyboard or mouse to select it. There will be a pause of a few seconds while Package Control fetches the list of available plugins.

1. When the plugin list appears, type `ansible-lint`. Among the entries you should see `SublimeLinter-contrib-ansible-lint`. If that entry is not highlighted, use the keyboard or mouse to select it.

### Reccomended plugin
It is highly recommended to also install the Sublime plugin [Trailing Spaces](https://github.com/SublimeText/TrailingSpaces) by using [Package Control][pc]. And to set the `Trim On Save` option to `true`.

The settings can be found under:

```
Sublime Text -> Preferences -> Settings
```

```
    { "trailing_spaces_trim_on_save": true }
```

## Settings
For general information on how SublimeLinter works with settings, please see [Settings][settings]. For information on generic linter settings, please see [Linter Settings][linter-settings].

In addition to the standard SublimeLinter settings, SublimeLinter-contrib-ansible-lint provides its own settings. Those marked as “Inline Setting” or “Inline Override” may also be [used inline][inline-settings].

|Setting|Description|Inline Setting|Inline Override|
|:------|:----------|:------------:|:-------------:|
|r|Specify one or more rules directories using one or more -r arguments. Any -r flags override the default rules in /usr/local/lib/python2.7/dist-packages/ansiblelint/rules, unless -R is also used.|&#10003;|&#10003;|
|R|Use default rules in /usr/local/lib/python2.7/dist-packages/ansiblelint/rules in addition to any extra rules directories specified with -r. There is no need to specify this if no -r flags are used.|&#10003;|&#10003;|
|t|Only check rules whose id/tags match these values.|&#10003;|&#10003;|
|x|Only check rules whose id/tags do not match these values.|&#10003;|&#10003;|
|exclude|Path to directories or files to skip.|&#10003;|&#10003;|

### List of all tags
|Tags|IDs|
|:---|:--|
|behaviour|ANSIBLE0016|
|bug|ANSIBLE0014|
|deprecated|ANSIBLE0018, ANSIBLE0015, ANSIBLE0008|
|formatting|ANSIBLE0002, ANSIBLE0009, ANSIBLE0015|
|idempotency|ANSIBLE0012|
|oddity|ANSIBLE0017|
|readability|ANSIBLE0011|
|repeatability|ANSIBLE0005, ANSIBLE0004, ANSIBLE0010|
|resources|ANSIBLE0006, ANSIBLE0007|
|safety|ANSIBLE0013|

## Contributing
If you would like to contribute enhancements or fixes, please do the following:

1. Fork the plugin repository.
1. Hack on a separate topic branch created from the latest `master`.
1. Commit and push the topic branch.
1. Make a pull request.
1. Be patient.  ;-)

Please note that modifications should follow these coding guidelines:

- Indent is 4 spaces.
- Code should pass flake8 and pep257 linters.
- Vertical whitespace helps readability, don’t be afraid to use it.
- Please use descriptive variable names, no abbreviations unless they are very well known.

Thank you for helping out!

[docs]: http://sublimelinter.readthedocs.org
[installation]: http://sublimelinter.readthedocs.org/en/latest/installation.html
[locating-executables]: http://sublimelinter.readthedocs.org/en/latest/usage.html#how-linter-executables-are-located
[pc]: https://sublime.wbond.net/installation
[cmd]: http://docs.sublimetext.info/en/sublime-text-3/extensibility/command_palette.html
[settings]: http://sublimelinter.readthedocs.org/en/latest/settings.html
[linter-settings]: http://sublimelinter.readthedocs.org/en/latest/linter_settings.html
[inline-settings]: http://sublimelinter.readthedocs.org/en/latest/settings.html#inline-settings
