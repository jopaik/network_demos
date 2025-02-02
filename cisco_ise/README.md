
## Return to Demo Menu
 - [Menu of Demos](../README.md)

# Summary of steps
1. Launch the Network-Cisco-ISE-Workflow 
2. Review the json output from each job-template
 * Users
 * Groups
 * Devices 
 * Endpoints

## Cisco ISE

[Table of Contents](#table-of-contents)
- [Step 1 - Launch the Workflow Template ](#step-1-launch-the-workflow-template)
- [Step 2 - Note the Workflow job-ID](#step-2-note-the-workflow-job-ID)
- Step 3 - Review the Network-Cisco-Ise-Groups job-template output (#step-3-Review the Network-Cisco-Ise-Groups job-template output)
- Step 4 - Review the Network-Cisco-Ise-Network-Devices job-template output
- Step 5 - Review the Network-Cisco-Ise-Endpoints job-template output
- Key Takeaways

## Objective
To integrate Ansible workflows with the ISE to glean endpoint and device configuration state info.

## Overview
Cisco ISE contains configuration, posture, and policy state information. This information is directly accessable to AAP for instucture as code. Secondly, AAP is a configuration alteernative to the ISE GUI.

## Step 1 - Launch the Network-Cisco-ISE-Workflow 
The following depicts the workflow visualization:

![visialization](../images/ise_workflow.png)

This workflow includes the following job templates:

![templates](../images/Ise_templates.png)


## Step 2 - Review the Network-Cisco-Ise-Users job-template output
The Network-Cisco-Ise-Users job-template returns the following output: 
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
## Step 3 - Review the Network-Cisco-Ise-Groups job-template output
The Network-Cisco-Ise-Groups job-template returns the following output: 
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
## Step 4 - Review the Network-Cisco-Ise-Network-Devices job-template output
The Network-Cisco-Ise-Network-Devices job-template returns the following output: 
#### Note, the network devices are another potential source for a dynamic inventory script.
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
## Step 5 - Review the Network-Cisco-Ise-Endpoints job-template output
The Network-Cisco-Ise-Endpoints job-template returns the following output: 
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

# Key Takeaways
* ISE and AAP are better together!!!
* APP can configure ISE as an alternative to the GUI
* AAP has access to device and endpoint configuration, policy and posture state in ISE
* AAP can pass ISE configuration data to ITSM CMDB
* ISE devices can be used as a dynamic inventory source
* AAP is an alternative to pxgrid for provisioning non-Cisco devices 

## Return to Demo Menu
 - [Menu of Demos](../README.md)