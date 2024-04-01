# -*- coding: utf-8 -*-
# Copyright 2020 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

#############################################
#                WARNING                    #
#############################################
#
# This file is auto generated by the resource
#   module builder playbook.
#
# Do not edit this file manually.
#
# Changes to this file will be over written
#   by the resource module builder.
#
# Changes should be made in the model used to
#   generate this file or in the resource module
#   builder template.
#
#############################################

from __future__ import absolute_import, division, print_function


__metaclass__ = type

from ansible_collections.junipernetworks.junos.plugins.modules import junos_l3_interfaces
from ansible_collections.junipernetworks.junos.tests.unit.compat.mock import patch
from ansible_collections.junipernetworks.junos.tests.unit.modules.utils import set_module_args

from .junos_module import TestJunosModule, load_fixture


class TestJunosL3InterfacesModule(TestJunosModule):
    module = junos_l3_interfaces

    def setUp(self):
        super(TestJunosL3InterfacesModule, self).setUp()
        self.mock_lock_configuration = patch(
            "ansible_collections.junipernetworks.junos.plugins.module_utils.network.junos.junos.lock_configuration",
        )
        self.lock_configuration = self.mock_lock_configuration.start()
        self.mock_unlock_configuration = patch(
            "ansible_collections.junipernetworks.junos.plugins.module_utils.network.junos.junos.unlock_configuration",
        )
        self.unlock_configuration = self.mock_unlock_configuration.start()
        self.mock_load_config = patch(
            "ansible_collections.junipernetworks.junos.plugins.module_utils.network.junos.config.l3_interfaces.l3_interfaces.load_config",
        )
        self.load_config = self.mock_load_config.start()

        self.mock_validate_config = patch(
            "ansible_collections.ansible.netcommon.plugins.module_utils.network.common.utils.validate_config",
        )
        self.validate_config = self.mock_validate_config.start()

        self.mock_commit_configuration = patch(
            "ansible_collections.junipernetworks.junos.plugins.module_utils.network.junos.config.l3_interfaces.l3_interfaces.commit_configuration",
        )
        self.mock_commit_configuration = self.mock_commit_configuration.start()

        self.mock_get_config = patch(
            "ansible_collections.junipernetworks.junos.plugins.module_utils.network.junos.facts.l3_interfaces.l3_interfaces."
            "L3_interfacesFacts.get_config",
        )
        self.get_config = self.mock_get_config.start()

    def tearDown(self):
        super(TestJunosL3InterfacesModule, self).tearDown()
        self.mock_get_config.stop()
        self.mock_load_config.stop()
        self.mock_validate_config.stop()
        self.mock_lock_configuration.stop()
        self.mock_unlock_configuration.stop()
        self.mock_commit_configuration.stop()

    def load_fixtures(self, commands=None, format="text", changed=False):
        self.get_config.return_value = load_fixture(
            "junos_interfaces_config.xml",
        )
        if changed:
            self.load_config.return_value = load_fixture(
                "get_configuration_rpc_reply_diff.txt",
            )
        else:
            self.load_config.return_value = None

    def test_junos_l3_interfaces_merged(self):
        set_module_args(
            dict(
                config=[
                    dict(
                        name="ge-0/0/1",
                        ipv4=[
                            dict(address="100.64.0.1/10"),
                            dict(address="100.64.0.2/10"),
                        ],
                    ),
                ],
                state="merged",
            ),
        )
        commands = [
            '<nc:interfaces xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0"><nc:interface>'
            "<nc:name>ge-0/0/1</nc:name><nc:unit><nc:name>0</nc:name>"
            "<nc:family><nc:inet><nc:address><nc:name>100.64.0.1/10</nc:name></nc:address>"
            "<nc:address><nc:name>100.64.0.2/10</nc:name></nc:address></nc:inet></nc:family>"
            "</nc:unit></nc:interface></nc:interfaces>",
        ]
        result = self.execute_module(changed=True)
        self.assertEqual(sorted(result["commands"]), sorted(commands))

    def test_junos_l3_interfaces_merged_idempotent(self):
        self.get_config.return_value = load_fixture(
            "junos_interfaces_config.xml",
        )
        src = load_fixture("junos_l3_interfaces.cfg", content="str")
        set_module_args(dict(src=src))
        set_module_args(
            dict(
                config=[
                    dict(
                        name="ge-0/0/1",
                        ipv4=[
                            dict(address="100.64.0.1/10"),
                            dict(address="100.64.0.2/10"),
                        ],
                    ),
                ],
                state="merged",
            ),
        )
        self.execute_module(changed=False, commands=[])

    def test_junos_l3_interfaces_replaced(self):
        set_module_args(
            dict(
                config=[
                    dict(
                        name="ge-0/0/2",
                        ipv4=[
                            dict(address="100.64.0.1/10"),
                            dict(address="100.64.0.2/10"),
                        ],
                    ),
                ],
                state="replaced",
            ),
        )
        commands = [
            '<nc:interfaces xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0"><nc:interface>'
            "<nc:name>ge-0/0/2</nc:name><nc:unit><nc:name>0</nc:name>"
            "<nc:family><nc:inet><nc:address><nc:name>100.64.0.1/10</nc:name></nc:address>"
            "<nc:address><nc:name>100.64.0.2/10</nc:name></nc:address></nc:inet></nc:family>"
            "</nc:unit></nc:interface></nc:interfaces>",
        ]
        result = self.execute_module(changed=True)

        self.assertEqual(sorted(result["commands"]), sorted(commands))

    def test_junos_l3_interfaces_replaced_idempotent(self):
        self.get_config.return_value = load_fixture(
            "junos_interfaces_config.xml",
        )
        src = load_fixture("junos_l3_interfaces.cfg", content="str")
        set_module_args(dict(src=src))
        set_module_args(
            dict(
                config=[
                    dict(
                        name="ge-0/0/1",
                        ipv4=[
                            dict(address="100.64.0.1/10"),
                            dict(address="100.64.0.2/10"),
                        ],
                    ),
                ],
                state="merged",
            ),
        )
        self.execute_module(changed=False, commands=[])

    def test_junos_l3_interfaces_overridden(self):
        set_module_args(
            dict(
                config=[
                    dict(
                        name="ge-0/0/1",
                        ipv4=[
                            dict(address="100.64.0.1/10"),
                            dict(address="100.64.0.2/10"),
                        ],
                    ),
                ],
                state="overridden",
            ),
        )
        commands = [
            '<nc:interfaces xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0"><nc:interface>'
            "<nc:name>ge-0/0/1</nc:name><nc:unit><nc:name>0</nc:name>"
            "<nc:family><nc:inet><nc:address><nc:name>100.64.0.1/10</nc:name></nc:address>"
            "<nc:address><nc:name>100.64.0.2/10</nc:name></nc:address></nc:inet></nc:family>"
            "</nc:unit></nc:interface></nc:interfaces>",
        ]
        result = self.execute_module(changed=True)

        self.assertEqual(sorted(result["commands"]), commands)

    def test_junos_l3_interfaces_overridden_idempotent(self):
        self.get_config.return_value = load_fixture(
            "junos_interfaces_config.xml",
        )
        src = load_fixture("junos_l3_interfaces.cfg", content="str")
        set_module_args(dict(src=src))
        set_module_args(
            dict(
                config=[
                    dict(
                        name="ge-0/0/1",
                        ipv4=[
                            dict(address="100.64.0.1/10"),
                            dict(address="100.64.0.2/10"),
                        ],
                    ),
                ],
                state="overridden",
            ),
        )
        self.execute_module(changed=False, commands=[])

    def test_junos_l3_interfaces_rendered(self):
        set_module_args(
            dict(
                config=[
                    dict(
                        name="ge-0/0/1",
                        ipv4=[
                            dict(address="100.64.0.1/10"),
                            dict(address="100.64.0.2/10"),
                        ],
                    ),
                ],
                state="rendered",
            ),
        )
        commands = [
            '<nc:interfaces xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0"><nc:interface>'
            "<nc:name>ge-0/0/1</nc:name><nc:unit><nc:name>0</nc:name>"
            "<nc:family><nc:inet><nc:address><nc:name>100.64.0.1/10</nc:name></nc:address>"
            "<nc:address><nc:name>100.64.0.2/10</nc:name></nc:address></nc:inet></nc:family>"
            "</nc:unit></nc:interface></nc:interfaces>",
        ]
        self.execute_module(changed=False, commands=commands)
