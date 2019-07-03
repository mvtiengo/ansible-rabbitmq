import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')

def test_rabbitmq_is_installed(host):
    rabbitmq = host.package("rabbitmq-server")
    assert rabbitmq.is_installed
