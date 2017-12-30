"""
Role tests
"""

import os
from testinfra.utils.ansible_runner import AnsibleRunner

testinfra_hosts = AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_packages(host):
    """
    Test if needed packages installed
    """

    packages = []

    if host.system_info.distribution in ('debian', 'ubuntu'):
        packages = ['sysfsutils']

    for package in packages:
        assert host.package(package).is_installed


def test_sysfs_utils_service(host):
    """
    Test if sys FS utils service started
    """

    service = ''

    if host.system_info.distribution in ('debian', 'ubuntu'):
        service = 'sysfsutils'

    assert host.service(service).is_enabled

    # Systemctl not available with Docker images
    if 'docker' != host.backend.NAME:
        assert host.service(service).is_running
