"""
Role tests
"""

import os
import pytest
from testinfra.utils.ansible_runner import AnsibleRunner

testinfra_hosts = AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_rules_folder(host):
    """
    Test if rules folders exists
    """

    rules_folder = {
        'path': '/etc/sysfs.d',
        'user': 'root',
        'group': 'root',
        'mode': 0o700,
    }

    assert host.file(rules_folder['path']).exists
    assert host.file(rules_folder['path']).is_directory
    assert host.file(rules_folder['path']).user == rules_folder['user']
    assert host.file(rules_folder['path']).group == rules_folder['group']
    assert host.file(rules_folder['path']).mode == rules_folder['mode']


def test_rules_files(host):
    """
    Test if rules files exists
    """

    rules_file = {
        'path': '/etc/sysfs.d/transparent-huge-pages.conf',
        'user': 'root',
        'group': 'root',
        'mode': 0o400,
    }

    expected_content = {
        'kernel/mm/transparent_hugepage/defrag = never',
        'kernel/mm/transparent_hugepage/enabled = never',
    }

    file_content = host.check_output('cat {}'.format(rules_file['path']))
    file_content_set = set(it.strip() for it in file_content.split("\n"))

    assert host.file(rules_file['path']).exists
    assert host.file(rules_file['path']).is_file
    assert host.file(rules_file['path']).user == rules_file['user']
    assert host.file(rules_file['path']).group == rules_file['group']
    assert host.file(rules_file['path']).mode == rules_file['mode']
    assert expected_content.issubset(file_content_set)


def test_packages(host):
    """
    Test if needed packages installed
    """

    assert host.package('sysfsutils').is_installed


def test_sysfs_utils_service(host):
    """
    Test if sys FS utils service started
    """

    if host.system_info.distribution not in ('debian', 'ubuntu'):
        pytest.skip('Test defined for another distribution')

    assert host.service('sysfsutils').is_enabled
