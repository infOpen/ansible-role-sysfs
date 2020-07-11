# sysfs

[![CI](https://github.com/infOpen/ansible-role-sysfs/workflows/CI/badge.svg)](https://github.com/infOpen/ansible-role-sysfs/actions)
[![Mergify Status][mergify-status]][mergify]
[![Updates](https://pyup.io/repos/github/infOpen/ansible-role-sysfs/shield.svg)](https://pyup.io/repos/github/infOpen/ansible-role-sysfs/)
[![Python 3](https://pyup.io/repos/github/infOpen/ansible-role-sysfs/python-3-shield.svg)](https://pyup.io/repos/github/infOpen/ansible-role-sysfs/)
[![Ansible Role](https://img.shields.io/ansible/role/18028.svg)](https://galaxy.ansible.com/infOpen/sysfs/)

Install sysfs package.

## Requirements

This role requires Ansible 2.8 or higher,
and platform requirements are listed in the metadata file.

## Testing

This role use [Molecule](https://github.com/ansible-community/molecule) to run tests.

Local and Github Actions tests run tests on Docker by default.
See molecule documentation to use other backend.

Currently, tests are done on:
- CentOS 7
- CentOS 8
- Debian Buster
- Debian Stretch
- Ubuntu Bionic
- Ubuntu Focal

and use:
- Ansible 2.8.x
- Ansible 2.9.x

### Running tests

#### Using Docker driver

```
$ tox
```

You can also configure molecule options and molecule command using environment variables:
* `MOLECULE_OPTIONS` Default: "--debug"
* `MOLECULE_COMMAND` Default: "test"

```
$ MOLECULE_OPTIONS='' MOLECULE_COMMAND=converge tox
```

## Role Variables

### Default role variables

``` yaml
# Package management
sysfs_packages: "{{ _sysfs_packages | default([]) }}"

# Service management
sysfs_service_file_path: "{{ _sysfs_service_file_path | default('') }}"
sysfs_service_name: "{{ _sysfs_service_name | default('') }}"
sysfs_service_enabled: True

# Configuration management
sysfs_config: "{{ _sysfs_config }}"
sysfs_dependent_services: []
sysfs_rules: []
```

### Debian OS family variables

``` yaml
# System prerequisites
_sysfs_packages:
  - name: 'sysfsutils'

# Service management
_sysfs_service_name: 'sysfsutils'
_sysfs_service_file_path: '/etc/init.d/sysfsutils'

# Configuration management
_sysfs_config:
  files: {}
  folder:
    path: '/etc/sysfs.d'
```

## Dependencies

None

## Example Playbook

``` yaml
- hosts: servers
  roles:
    - { role: infOpen.sysfs }
```

## License

MIT

## Author Information

Alexandre Chaussier (for Infopen company)
- https://www.infopen.pro
- a.chaussier [at] infopen.pro

[mergify]: https://mergify.io
[mergify-status]: https://img.shields.io/endpoint.svg?url=https://gh.mergify.io/badges/infOpen/ansible-role-sysfs&style=flat
