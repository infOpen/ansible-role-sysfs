"""
Role configuration tests
"""

from testinfra.utils.ansible_runner import AnsibleRunner

testinfra_hosts = AnsibleRunner('.molecule/ansible_inventory').get_hosts('all')


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


def test_sysfs_rules(host):
    """
    Check sysfs rules
    """

    rules = []

    if host.system_info.distribution in ('debian', 'ubuntu'):
        rules = [
            (
                '/sys/kernel/mm/transparent_hugepage/defrag',
                'always madvise [never]'
            ),
            (
                '/sys/kernel/mm/transparent_hugepage/enabled',
                'always madvise [never]'
            ),
        ]

    for rule in rules:
        assert host.check_output('cat {}'.format(rule[0])) == rule[1]
