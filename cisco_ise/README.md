
## Return to Demo Menu
 - [Menu of Demos](../README.md)

# Summary of steps
## Cisco ISE

[Table of Contents](#table-of-contents)
- [Step 1 - SNOW user/pass](#step-1-snow-user/pass)
- [Step 2 - Collect user/pass](#step-2-collect-user/pass)
- [Step 3 - Launch the Workflow Template ](#step-3-launch-the-workflow-template)
- [Step 4 - Note the Workflow job-ID](#step-4-note-the-workflow-job-ID)
- [Step 5 - SNOW incident](#step-5-snow-incident)

## Objective
To integrate Ansible workflows with the ISE to glean endpoint and device configuration state info.

## Overview
Cisco ISE contains configuration, posture, and policy state info. This information can be accessed by AAPand used for instucture as code. AAP is also an alternative to the GUI to configure ISE.

## Step 1 - Launch the Network-Cisco-ISE- Workflow 
This workflow includes the following job templates

users:
~~~
{
  "result": {
    "changed": false,
    "ise_response": [
      {
        "id": "a176c430-8c01-11e6-996c-525400b48521",
        "name": "ALL_ACCOUNTS (default)",
        "description": "Default ALL_ACCOUNTS (default) User Group",
        "link": {
          "rel": "self",
          "href": "https://devnetsandboxise.cisco.com/ers/config/identitygroup/a176c430-8c01-11e6-996c-525400b48521",
          "type": "application/json"
        }
      },
      {
        "id": "a1740510-8c01-11e6-996c-525400b48521",
        "name": "Employee",
        "description": "Default Employee User Group",
        "link": {
          "rel": "self",
          "href": "https://devnetsandboxise.cisco.com/ers/config/identitygroup/a1740510-8c01-11e6-996c-525400b48521",
          "type": "application/json"
        }
      },
      {
        "id": "a1bb2030-8c01-11e6-996c-525400b48521",
        "name": "GROUP_ACCOUNTS (default)",
        "description": "Default GROUP_ACCOUNTS (default) User Group",
        "link": {
          "rel": "self",
          "href": "https://devnetsandboxise.cisco.com/ers/config/identitygroup/a1bb2030-8c01-11e6-996c-525400b48521",
          "type": "application/json"
        }
      },
      {
        "id": "9f048bb0-8c01-11e6-996c-525400b48521",
        "name": "GuestType_Contractor (default)",
        "description": "Identity group mirroring the guest type ",
        "link": {
          "rel": "self",
          "href": "https://devnetsandboxise.cisco.com/ers/config/identitygroup/9f048bb0-8c01-11e6-996c-525400b48521",
          "type": "application/json"
        }
      },
      {
        "id": "9eee92b0-8c01-11e6-996c-525400b48521",
        "name": "GuestType_Daily (default)",
        "description": "Identity group mirroring the guest type ",
        "link": {
          "rel": "self",
          "href": "https://devnetsandboxise.cisco.com/ers/config/identitygroup/9eee92b0-8c01-11e6-996c-525400b48521",
          "type": "application/json"
        }
      },
      {
        "id": "359a5240-4fbe-11ed-a871-0050568f5811",
        "name": "GuestType_SocialLogin (default)",
        "description": "Identity group mirroring the guest type ",
        "link": {
          "rel": "self",
          "href": "https://devnetsandboxise.cisco.com/ers/config/identitygroup/359a5240-4fbe-11ed-a871-0050568f5811",
          "type": "application/json"
        }
      },
      {
        "id": "9efe2310-8c01-11e6-996c-525400b48521",
        "name": "GuestType_Weekly (default)",
        "description": "Identity group mirroring the guest type ",
        "link": {
          "rel": "self",
          "href": "https://devnetsandboxise.cisco.com/ers/config/identitygroup/9efe2310-8c01-11e6-996c-525400b48521",
          "type": "application/json"
        }
      },
      {
        "id": "a19d5f00-8c01-11e6-996c-525400b48521",
        "name": "OWN_ACCOUNTS (default)",
        "description": "Default OWN_ACCOUNTS (default) User Group",
        "link": {
          "rel": "self",
          "href": "https://devnetsandboxise.cisco.com/ers/config/identitygroup/a19d5f00-8c01-11e6-996c-525400b48521",
          "type": "application/json"
        }
      }
~~~

Groups:
~~~
{
  "result": {
    "changed": false,
    "ise_response": [
      {
        "id": "a176c430-8c01-11e6-996c-525400b48521",
        "name": "ALL_ACCOUNTS (default)",
        "description": "Default ALL_ACCOUNTS (default) User Group",
        "link": {
          "rel": "self",
          "href": "https://devnetsandboxise.cisco.com/ers/config/identitygroup/a176c430-8c01-11e6-996c-525400b48521",
          "type": "application/json"
        }
      },
      {
        "id": "a1740510-8c01-11e6-996c-525400b48521",
        "name": "Employee",
        "description": "Default Employee User Group",
        "link": {
          "rel": "self",
          "href": "https://devnetsandboxise.cisco.com/ers/config/identitygroup/a1740510-8c01-11e6-996c-525400b48521",
          "type": "application/json"
        }
      },
      {
        "id": "a1bb2030-8c01-11e6-996c-525400b48521",
        "name": "GROUP_ACCOUNTS (default)",
        "description": "Default GROUP_ACCOUNTS (default) User Group",
        "link": {
          "rel": "self",
          "href": "https://devnetsandboxise.cisco.com/ers/config/identitygroup/a1bb2030-8c01-11e6-996c-525400b48521",
          "type": "application/json"
        }
      },
      {
        "id": "9f048bb0-8c01-11e6-996c-525400b48521",
        "name": "GuestType_Contractor (default)",
        "description": "Identity group mirroring the guest type ",
        "link": {
          "rel": "self",
          "href": "https://devnetsandboxise.cisco.com/ers/config/identitygroup/9f048bb0-8c01-11e6-996c-525400b48521",
          "type": "application/json"
        }
      },
      {
        "id": "9eee92b0-8c01-11e6-996c-525400b48521",
        "name": "GuestType_Daily (default)",
        "description": "Identity group mirroring the guest type ",
        "link": {
          "rel": "self",
          "href": "https://devnetsandboxise.cisco.com/ers/config/identitygroup/9eee92b0-8c01-11e6-996c-525400b48521",
          "type": "application/json"
        }
      },
      {
        "id": "359a5240-4fbe-11ed-a871-0050568f5811",
        "name": "GuestType_SocialLogin (default)",
        "description": "Identity group mirroring the guest type ",
        "link": {
          "rel": "self",
          "href": "https://devnetsandboxise.cisco.com/ers/config/identitygroup/359a5240-4fbe-11ed-a871-0050568f5811",
          "type": "application/json"
        }
      },
      {
        "id": "9efe2310-8c01-11e6-996c-525400b48521",
        "name": "GuestType_Weekly (default)",
        "description": "Identity group mirroring the guest type ",
        "link": {
          "rel": "self",
          "href": "https://devnetsandboxise.cisco.com/ers/config/identitygroup/9efe2310-8c01-11e6-996c-525400b48521",
          "type": "application/json"
        }
      },
      {
        "id": "a19d5f00-8c01-11e6-996c-525400b48521",
        "name": "OWN_ACCOUNTS (default)",
        "description": "Default OWN_ACCOUNTS (default) User Group",
        "link": {
          "rel": "self",
          "href": "https://devnetsandboxise.cisco.com/ers/config/identitygroup/a19d5f00-8c01-11e6-996c-525400b48521",
          "type": "application/json"
        }
~~~

Network Devices
~~~
{
  "result_id": {
    "results": [
      {
        "changed": false,
        "ise_response": {
          "id": "199770a0-6dfe-11ee-965b-6aa0f144a1be",
          "name": "CSR1000v",
          "description": "",
          "authenticationSettings": {
            "enableKeyWrap": false,
            "dtlsRequired": false,
            "keyEncryptionKey": "",
            "messageAuthenticatorCodeKey": "",
            "keyInputFormat": "ASCII",
            "enableMultiSecret": "false"
          },
          "profileName": "Cisco",
          "coaPort": 1700,
          "link": {
            "rel": "self",
            "href": "https://devnetsandboxise.cisco.com/ers/config/networkdevice/199770a0-6dfe-11ee-965b-6aa0f144a1be",
            "type": "application/json"
          },
          "NetworkDeviceIPList": [
            {
              "ipaddress": "10.10.20.48",
              "mask": 32
            }
          ],
          "NetworkDeviceGroupList": [
            "Location#All Locations",
            "IPSEC#Is IPSEC Device#No",
            "Device Type#All Device Types"
          ]
        },
        "result": "",
        "failed": false,
        "item": "199770a0-6dfe-11ee-965b-6aa0f144a1be",
        "ansible_loop_var": "item"
      },
      {
        "changed": false,
        "ise_response": {
          "id": "dfe3b620-6dfd-11ee-965b-6aa0f144a1be",
          "name": "Cat8000",
          "description": "Catalyst 8000",
          "authenticationSettings": {
            "enableKeyWrap": false,
            "dtlsRequired": false,
            "keyEncryptionKey": "",
            "messageAuthenticatorCodeKey": "",
            "keyInputFormat": "ASCII",
            "enableMultiSecret": "false"
          },
          "profileName": "Cisco",
          "coaPort": 1700,
          "link": {
            "rel": "self",
            "href": "https://devnetsandboxise.cisco.com/ers/config/networkdevice/dfe3b620-6dfd-11ee-965b-6aa0f144a1be",
            "type": "application/json"
          },
          "NetworkDeviceIPList": [
            {
              "ipaddress": "10.10.20.148",
              "mask": 32
            }
          ],
          "NetworkDeviceGroupList": [
            "Location#All Locations",
            "IPSEC#Is IPSEC Device#No",
            "Device Type#All Device Types"
          ]
        },
        "result": "",
        "failed": false,
        "item": "dfe3b620-6dfd-11ee-965b-6aa0f144a1be",
        "ansible_loop_var": "item"
      }
~~~
Endpoint Groups:
~~~
{
  "msg": [
    "End Point Groups:",
    "Group: [Blocked List]['aa000c30-8bff-11e6-996c-525400b48521']",
    "Group: [Profiled]['aa10ae00-8bff-11e6-996c-525400b48521']",
    "Group: [GuestEndpoints]['aa178bd0-8bff-11e6-996c-525400b48521']"
  ],
~~~

Endpoints:
~~~

  "msg": [
    "name: 00:01:02:03:04:05",
    "mac: 00:01:02:03:04:05",
    "description: __omit_place_holder__1ec7efd7e4d1e431fc87eadffa562395ad44045d",
    "id: 2b2d8180-6e47-11ee-8978-005056bfe5f4",
    "group_id: aa10ae00-8bff-11e6-996c-525400b48521"
  ],
  "_ansible_verbose_always": true,
  "_ansible_no_log": null,
  "changed": false,
  "item": {
    "changed": false,
    "ise_response": {
      "id": "2b2d8180-6e47-11ee-8978-005056bfe5f4",
      "name": "00:01:02:03:04:05",
      "mac": "00:01:02:03:04:05",
      "profileId": "fed21140-8bff-11e6-996c-525400b48521",
      "staticProfileAssignment": false,
      "staticProfileAssignmentDefined": true,
      "groupId": "aa10ae00-8bff-11e6-996c-525400b48521",
      "staticGroupAssignment": false,
      "staticGroupAssignmentDefined": true,
      "portalUser": "",
      "identityStore": "",
      "identityStoreId": "",
      "customAttributes": {
        "customAttributes": {}
      },
      "link": {
        "rel": "self",
~~~