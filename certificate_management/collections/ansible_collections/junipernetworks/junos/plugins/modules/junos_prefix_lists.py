#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright 2019 Red Hat
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

"""
The module file for junos_prefix_lists
"""

from __future__ import absolute_import, division, print_function


__metaclass__ = type

ANSIBLE_METADATA = {
    "metadata_version": "1.1",
    "status": ["preview"],
    "supported_by": "network",
}

DOCUMENTATION = """
---
module: junos_prefix_lists
version_added: 2.1.0
short_description: Manage prefix-lists attributes of interfaces on Junos devices.
description: Manage prefix-lists attributes of interfaces on Junos network devices.
author: Rohit Thakur (@rohitthakur2590)
requirements:
  - ncclient (>=v0.6.4)
  - xmltodict (>=0.12.0)
notes:
  - This module requires the netconf system service be enabled on the device being managed.
  - This module works with connection C(netconf).
  - See L(the Junos OS Platform Options,https://docs.ansible.com/ansible/latest/network/user_guide/platform_junos.html).
  - Tested against JunOS v18.4R1
options:
  running_config:
    description:
      - This option is used only with state I(parsed).
      - The value of this option should be the output received from the Junos device
        by executing the command B(show policy-options).
      - The state I(parsed) reads the configuration from C(running_config) option and
        transforms it into Ansible structured data as per the resource module's argspec
        and the value is then returned in the I(parsed) key within the result
    type: str
  config:
    description: The provided link BGP address family dictionary.
    type: list
    elements: dict
    suboptions:
      name:
        description: Specify the name of the prefix-list.
        type: str
        required: true
      address_prefixes:
        description: Specify address prefixes.
        type: list
        elements: str
      dynamic_db:
        description: Enable object to exist in dynamic DB.
        type: bool
  state:
    description:
      - The state the configuration should be left in.
    type: str
    choices:
    - merged
    - replaced
    - overridden
    - deleted
    - parsed
    - gathered
    - rendered
    default: merged
"""
EXAMPLES = """
# Using merged
#
# Before state
# ------------
#
# vagrant@vsrx# show policy-options
#
# [edit]

- name: Merge Junos prefix  lists
  junipernetworks.junos.junos_prefix_lists:
    config:
      - name: Internal
        address_prefixes:
          - 172.16.1.32
          - 172.16.3.32
      - name: Test1
        dynamic_db: true
      - name: Test2
        address_prefixes:
          - 172.16.2.32
          - 172.16.7.32
          - 172.16.9.32
    state: merged
#
# -------------------------
# Module Execution Result
# -------------------------
#
#    "before": []
#    "commands": [
#         "<nc:policy-options xmlns:nc=\"urn:ietf:params:xml:ns:netconf:base:1.0\">
#         "<nc:prefix-list><nc:name>Internal</nc:name><nc:prefix-list-item><nc:name>172.16.1.32</nc:name>"
#         "</nc:prefix-list-item><nc:prefix-list-item><nc:name>172.16.3.32</nc:name>"
#         "</nc:prefix-list-item></nc:prefix-list><nc:prefix-list><nc:name>Test1</nc:name>"
#         "<nc:dynamic-db/></nc:prefix-list><nc:prefix-list><nc:name>Test2</nc:name>"
#         "<nc:prefix-list-item><nc:name>172.16.2.32</nc:name></nc:prefix-list-item>"
#         "<nc:prefix-list-item><nc:name>172.16.7.32</nc:name></nc:prefix-list-item>"
#         "<nc:prefix-list-item><nc:name>172.16.9.32</nc:name></nc:prefix-list-item>"
#         "</nc:prefix-list></nc:policy-options>"
#     ]
#
# "after": [
#         {
#             "address_prefixes": [
#                 "172.16.1.32/32",
#                 "172.16.3.32/32"
#             ],
#             "name": "Internal"
#         },
#         {
#             "dynamic_db": true,
#             "name": "Test1"
#         },
#         {
#             "address_prefixes": [
#                 "172.16.2.32/32",
#                 "172.16.7.32/32",
#                 "172.16.9.32/32"
#             ],
#             "name": "Test2"
#         }
#     ]
# After state
# -----------
#
# vagrant@vsrx# show policy-options
# prefix-list Internal {
#     172.16.1.32/32;
#     172.16.3.32/32;
# }
# prefix-list Test1 {
#     dynamic-db;
# }
# prefix-list Test2 {
#     172.16.2.32/32;
#     172.16.7.32/32;
#     172.16.9.32/32;
# }
#
# Using gathered
#
# Before state
# ------------
#
# vagrant@vsrx# show policy-options
# prefix-list Internal {
#     172.16.1.32/32;
#     172.16.3.32/32;
# }
# prefix-list Test1 {
#     dynamic-db;
# }
# prefix-list Test2 {
#     172.16.2.32/32;
#     172.16.7.32/32;
#     172.16.9.32/32;
# }

- name: Gather Junos prefix-lists
  junipernetworks.junos.junos_prefix_lists:
    state: gathered
#
#
# -------------------------
# Module Execution Result
# -------------------------
#
#    "gathered": [
#         {
#             "address_prefixes": [
#                 "172.16.1.32/32",
#                 "172.16.3.32/32"
#             ],
#             "name": "Internal"
#         },
#         {
#             "dynamic_db": true,
#             "name": "Test1"
#         },
#         {
#             "address_prefixes": [
#                 "172.16.2.32/32",
#                 "172.16.7.32/32",
#                 "172.16.9.32/32"
#             ],
#             "name": "Test2"
#         }
#     ]
#
# Using replaced
#
# Before state
# ------------
#
# vagrant@vsrx# show policy-options
# prefix-list Internal {
#     172.16.1.32/32;
#     172.16.3.32/32;
# }
# prefix-list Test1 {
#     dynamic-db;
# }
# prefix-list Test2 {
#     172.16.2.32/32;
#     172.16.7.32/32;
#     172.16.9.32/32;
# }
- name: Replace existing Junos prefix-lists configuration with provided config
  junipernetworks.junos.junos_prefix_lists:
   config:
     - name: Test2
       address_prefixes:
         - 172.16.4.32
         - 172.16.8.32
         - 172.16.9.32"
   state: replaced
# -------------------------
# Module Execution Result
# -------------------------
#
#    "before": [
#         {
#             "address_prefixes": [
#                 "172.16.1.32/32",
#                 "172.16.3.32/32"
#             ],
#             "name": "Internal"
#         },
#         {
#             "dynamic_db": true,
#             "name": "Test1"
#         },
#         {
#             "address_prefixes": [
#                 "172.16.2.32/32",
#                 "172.16.7.32/32",
#                 "172.16.9.32/32"
#             ],
#             "name": "Test2"
#         }
#     ]
#    "commands": [
#         "<nc:policy-options xmlns:nc=\"urn:ietf:params:xml:ns:netconf:base:1.0\">
#         "<nc:prefix-list delete=\"delete\"><nc:name>Test2</nc:name></nc:prefix-list>"
#         "<nc:prefix-list><nc:name>Test2</nc:name><nc:prefix-list-item><nc:name>172.16.4.32</nc:name>"
#         "</nc:prefix-list-item><nc:prefix-list-item><nc:name>172.16.8.32</nc:name>"
#         "</nc:prefix-list-item><nc:prefix-list-item><nc:name>172.16.9.32</nc:name>"
#         "</nc:prefix-list-item></nc:prefix-list></nc:policy-options>"
#     ]
#
# "after": [
#         {
#             "address_prefixes": [
#                 "172.16.1.32/32",
#                 "172.16.3.32/32"
#             ],
#             "name": "Internal"
#         },
#         {
#             "dynamic_db": true,
#             "name": "Test1"
#         },
#         {
#             "address_prefixes": [
#                 "172.16.4.32/32",
#                 "172.16.8.32/32",
#                 "172.16.9.32/32"
#             ],
#             "name": "Test2"
#         }
#     ]
# After state
# -----------
#
# vagrant@vsrx# show policy-options
# prefix-list Internal {
#     172.16.1.32/32;
#     172.16.3.32/32;
# }
# prefix-list Test1 {
#     dynamic-db;
# }
# prefix-list Test2 {
#     172.16.4.32/32;
#     172.16.8.32/32;
#     172.16.9.32/32;
# }
# Using overridden
#
# Before state
# ------------
#
# vagrant@vsrx# show policy-options
# prefix-list Internal {
#     172.16.1.32/32;
#     172.16.3.32/32;
# }
# prefix-list Test1 {
#     dynamic-db;
# }
# prefix-list Test2 {
#     172.16.4.32/32;
#     172.16.8.32/32;
#     172.16.9.32/32;
# }
- name: Override Junos prefix-lists configuration with provided configuration
  junipernetworks.junos.junos_prefix_lists:
   config:
     - name: Test2
       address_prefixes:
         - 172.16.4.32/28
         - 172.16.8.32/28
         - 172.16.9.32/28
   state: overridden

# -------------------------
# Module Execution Result
# -------------------------
#
#    "before": [
#         {
#             "address_prefixes": [
#                 "172.16.1.32/32",
#                 "172.16.3.32/32"
#             ],
#             "name": "Internal"
#         },
#         {
#             "dynamic_db": true,
#             "name": "Test1"
#         },
#         {
#             "address_prefixes": [
#                 "172.16.4.32/32",
#                 "172.16.8.32/32",
#                 "172.16.9.32/32"
#             ],
#             "name": "Test2"
#         }
#     ]
#    "commands": [
#         "<nc:policy-options xmlns:nc=\"urn:ietf:params:xml:ns:netconf:base:1.0\">
#         "<nc:prefix-list delete=\"delete\"><nc:name>Internal</nc:name>"
#         "</nc:prefix-list><nc:prefix-list delete=\"delete\"><nc:name>Test1</nc:name>"
#         "</nc:prefix-list><nc:prefix-list delete=\"delete\"><nc:name>Test2</nc:name>"
#         "</nc:prefix-list><nc:prefix-list><nc:name>Test2</nc:name><nc:prefix-list-item>"
#         "<nc:name>172.16.4.32/28</nc:name></nc:prefix-list-item><nc:prefix-list-item>"
#         "<nc:name>172.16.8.32/28</nc:name></nc:prefix-list-item><nc:prefix-list-item>"
#         "<nc:name>172.16.9.32/28</nc:name></nc:prefix-list-item></nc:prefix-list></nc:policy-options>"
#     ]
#
# "after": [
#         {
#             "address_prefixes": [
#                 "172.16.4.32/28",
#                 "172.16.8.32/28",
#                 "172.16.9.32/28"
#             ],
#             "name": "Test2"
#         }
#     ]
# After state
# -----------
#
# vagrant@vsrx# show policy-options
# prefix-list Test2 {
#     172.16.4.32/28;
#     172.16.8.32/28;
#     172.16.9.32/28;
# }
# Using deleted
#
# Before state
# ------------
#
# vagrant@vsrx# show policy-options
# prefix-list Internal {
#     172.16.1.32/32;
#     172.16.3.32/32;
# }
# prefix-list Test1 {
#     dynamic-db;
# }
# prefix-list Test2 {
#     172.16.2.32/32;
#     172.16.7.32/32;
#     172.16.9.32/32;
# }

- name: Delete provided prefix-lists
  junipernetworks.junos.junos_prefix_lists:
   config:
     - name: "Test1"
     - name: "Test2"
   state: deleted
# ------------------------
# Module Execution Results
# ------------------------
#
#    "before": [
#         {
#             "address_prefixes": [
#                 "172.16.1.32/32",
#                 "172.16.3.32/32"
#             ],
#             "name": "Internal"
#         },
#         {
#             "dynamic_db": true,
#             "name": "Test1"
#         },
#         {
#             "address_prefixes": [
#                 "172.16.2.32/32",
#                 "172.16.7.32/32",
#                 "172.16.9.32/32"
#             ],
#             "name": "Test2"
#         }
#     ]
#    "commands": [
#         "<nc:policy-options xmlns:nc=\"urn:ietf:params:xml:ns:netconf:base:1.0\">
#         "<nc:prefix-list delete=\"delete\"><nc:name>Test1</nc:name></nc:prefix-list>"
#         "<nc:prefix-list delete=\"delete\"><nc:name>Test2</nc:name></nc:prefix-list></nc:policy-options>"
#     ]
#
# "after": [
#         {
#             "address_prefixes": [
#                 "172.16.1.32/32",
#                 "172.16.3.32/32"
#             ],
#             "name": "Internal"
#         }
#     ]
# After state
# -----------
#
# vagrant@vsrx# show policy-options
# prefix-list Internal {
#     172.16.1.32/32;
#     172.16.3.32/32;
# }
#
# Using deleted without specifying config
#
# Before state
# ------------
#
# vagrant@vsrx# show policy-options
# prefix-list Internal {
#     172.16.1.32/32;
#     172.16.3.32/32;
# }
# prefix-list Test1 {
#     dynamic-db;
# }
# prefix-list Test2 {
#     172.16.2.32/32;
#     172.16.7.32/32;
#     172.16.9.32/32;
# }

- name: Delete complete Junos prefix-lists configuration
  junipernetworks.junos.junos_prefix_lists:
   state: deleted

# ------------------------
# Module Execution Results
# ------------------------
#
#    "before": [
#         {
#             "address_prefixes": [
#                 "172.16.1.32/32",
#                 "172.16.3.32/32"
#             ],
#             "name": "Internal"
#         },
#         {
#             "dynamic_db": true,
#             "name": "Test1"
#         },
#         {
#             "address_prefixes": [
#                 "172.16.2.32/32",
#                 "172.16.7.32/32",
#                 "172.16.9.32/32"
#             ],
#             "name": "Test2"
#         }
#     ]
#    "commands": ["<nc:policy-options xmlns:nc=\"urn:ietf:params:xml:ns:netconf:base:1.0\">
#                 "<nc:prefix-list delete=\"delete\"/></nc:policy-options>"
#                ]
#
# "after": []
# After state
# -----------
#
# vagrant@vsrx# show policy-options
#
# [edit]

#
# Using parsed
# parsed.cfg
# ------------
# <?xml version="1.0" encoding="UTF-8"?>
# <rpc-reply message-id="urn:uuid:0cadb4e8-5bba-47f4-986e-72906227007f">
#     <configuration changed-seconds="1590139550" changed-localtime="2020-05-22 09:25:50 UTC">
#         <version>18.4R1-S2.4</version>
#         <policy-options>
#         <prefix-list>
#             <name>64510</name>
#         </prefix-list>
#         <prefix-list>
#             <name>64500</name>
#             <dynamic-db/>
#             <prefix-list-item>
#                 <name>172.16.1.16/28</name>
#             </prefix-list-item>
#             <prefix-list-item>
#                 <name>172.16.1.32/28</name>
#             </prefix-list-item>
#         </prefix-list>
#     </policy-options>
#     </configuration>
# </rpc-reply>
- name: Parse running prefix-lists configuration
  junipernetworks.junos.junos_prefix_lists:
    running_config: "{{ lookup('file', './parsed.cfg') }}"
    state: parsed
#
#
# -------------------------
# Module Execution Result
# -------------------------
#
#
# "parsed":  [
#         {
#             "name": "64510"
#         },
#         {
#             "address_prefixes": [
#                 "172.16.1.16/28",
#                 "172.16.1.32/28"
#             ],
#             "dynamic_db": true,
#             "name": "64500"
#         }
#     ]
#
#
# Using rendered
#
- name: Render the xml for provided  configuration
  junipernetworks.junos.junos_prefix_lists:
    config:
      - name: Internal
        address_prefixes:
          - 172.16.1.32
          - 172.16.3.32
      - name: Test1
        dynamic_db: true
      - name: Test2
        address_prefixes:
          - 172.16.2.32
          - 172.16.7.32
          - 172.16.9.32
    state: rendered
#
#
# -------------------------
# Module Execution Result
# -------------------------
#
#
# "rendered": "<nc:policy-options xmlns:nc=\"urn:ietf:params:xml:ns:netconf:base:1.0\">
#             "<nc:prefix-list><nc:name>Internal</nc:name><nc:prefix-list-item><nc:name>172.16.1.32</nc:name>"
#             "</nc:prefix-list-item><nc:prefix-list-item><nc:name>172.16.3.32</nc:name></nc:prefix-list-item>"
#             "</nc:prefix-list><nc:prefix-list><nc:name>Test1</nc:name><nc:dynamic-db/></nc:prefix-list>"
#             "<nc:prefix-list><nc:name>Test2</nc:name><nc:prefix-list-item><nc:name>172.16.2.32</nc:name>"
#             "</nc:prefix-list-item><nc:prefix-list-item><nc:name>172.16.7.32</nc:name></nc:prefix-list-item>"
#             "<nc:prefix-list-item><nc:name>172.16.9.32</nc:name></nc:prefix-list-item>"
#             "</nc:prefix-list></nc:policy-options>"
"""
RETURN = """
before:
  description: The configuration prior to the model invocation.
  returned: always
  sample: >
    The configuration returned will always be in the same format
     of the parameters above.
  type: list
after:
  description: The resulting configuration model invocation.
  returned: when changed
  sample: >
    The configuration returned will always be in the same format
     of the parameters above.
  type: list
commands:
  description: The set of commands pushed to the remote device.
  returned: always
  type: list
  sample: ['<nc:policy-options xmlns:nc=\"urn:ietf:params:xml:ns:netconf:base:1.0\">
            "<nc:prefix-list delete=\"delete\"/></nc:policy-options>"', 'xml 2', 'command 3']
"""


from ansible.module_utils.basic import AnsibleModule

from ansible_collections.junipernetworks.junos.plugins.module_utils.network.junos.argspec.prefix_lists.prefix_lists import (
    Prefix_listsArgs,
)
from ansible_collections.junipernetworks.junos.plugins.module_utils.network.junos.config.prefix_lists.prefix_lists import (
    Prefix_lists,
)


def main():
    """
    Main entry point for module execution

    :returns: the result form module invocation
    """
    required_if = [
        ("state", "merged", ("config",)),
        ("state", "replaced", ("config",)),
        ("state", "rendered", ("config",)),
        ("state", "overridden", ("config",)),
        ("state", "parsed", ("running_config",)),
    ]
    module = AnsibleModule(
        argument_spec=Prefix_listsArgs.argument_spec,
        required_if=required_if,
        supports_check_mode=True,
    )
    result = Prefix_lists(module).execute_module()
    module.exit_json(**result)


if __name__ == "__main__":
    main()
