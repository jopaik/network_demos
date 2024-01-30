## Return to Demo Menu
 - [Menu of Demos](../README.md)

# Summary of steps
1. Launch the Network ACLS Deploy job-template
2. Verify the new ACL was `merged` and applied to rtr1 and rtr3
3. Modify an ACL entry from the CLI
4. Launch the Network ACLs Detect job-template
5. Review AAP output to determine the Configuration drift
6. Launch the Network ACLs Remediate Template
8. Verify the ACL entry is `replaced` to it's original configuration

# Network Backups GIT

[Table of Contents](#table-of-contents)
- [Step 1 - Collect Backup Configurations](#step-1---credential)
- [Step 2 - Review](#step-2---job-template)

## Objective
To deploy and change ACLs and ACL entries using valadated collection content.

## Overview
This demo uses the network.acs collection and the network.acls role from Validated Content to deploy or modify router access list configurations. 

### Step 1 - Launch the Network ACLS Deploy job-template
Launch the Network ACLS Deploy job-template

Review the `changed` tasks from the AAP output 

#### JSON Output for the rtr1 ACL
~~~
{
  "commands": [
    "ip access-list extended ansible",
    "10 permit tcp host 192.168.3.3 host 192.168.1.1 eq www log",
    "20 permit tcp host 192.168.3.3 host 192.168.1.1 eq 443 log",
    "30 permit tcp host 192.168.3.3 host 192.168.1.1 eq 22 log",
    "40 permit tcp host 192.168.3.3 host 192.168.1.1 eq 830 log",
    "50 permit tcp host 192.168.3.3 host 192.168.1.1 range 32766 65535 log",
    "60 permit ospf any any log",
    "70 permit icmp any any log"
    
  ],
  "before": [
    {
      "afi": "ipv4",
      "acls": [
        {
          "name": "GS_NAT_ACL",
          "acl_type": "standard",
          "aces": [
            {
              "sequence": 10,
              "grant": "permit",
              "source": {
                "address": "192.168.35.0",
                "wildcard_bits": "0.0.0.255"
              }
            }
          ]
        },
        {
          "name": "meraki-fqdn-dns",
          "acl_type": "extended"
        }
      ]
    }
  ],
  "after": [
    {
      "afi": "ipv4",
      "acls": [
        {
          "name": "GS_NAT_ACL",
          "acl_type": "standard",
          "aces": [
            {
              "sequence": 10,
              "grant": "permit",
              "source": {
                "address": "192.168.35.0",
                "wildcard_bits": "0.0.0.255"
              }
            }
          ]
        },
        {
          "name": "ansible",
          "acl_type": "extended",
          "aces": [
            {
              "sequence": 10,
              "grant": "permit",
              "protocol": "tcp",
              "source": {
                "host": "192.168.3.3"
              },
              "destination": {
                "host": "192.168.1.1",
                "port_protocol": {
                  "eq": "www"
                }
              },
              "log": {
                "set": true
              }
            },
            {
              "sequence": 20,
              "grant": "permit",
              "protocol": "tcp",
              "source": {
                "host": "192.168.3.3"
              },
              "destination": {
                "host": "192.168.1.1",
                "port_protocol": {
                  "eq": "443"
                }
              },
              "log": {
                "set": true
              }
            },
            {
              "sequence": 30,
              "grant": "permit",
              "protocol": "tcp",
              "source": {
                "host": "192.168.3.3"
              },
              "destination": {
                "host": "192.168.1.1",
                "port_protocol": {
                  "eq": "22"
                }
              },
              "log": {
                "set": true
              }
            },
            {
              "sequence": 40,
              "grant": "permit",
              "protocol": "tcp",
              "source": {
                "host": "192.168.3.3"
              },
              "destination": {
                "host": "192.168.1.1",
                "port_protocol": {
                  "eq": "830"
                }
              },
              "log": {
                "set": true
              }
            },
            {
              "sequence": 70,
              "grant": "permit",
              "protocol": "tcp",
              "source": {
                "host": "192.168.3.3"
              },
              "destination": {
                "host": "192.168.1.1",
                "port_protocol": {
                  "range": {
                    "start": 32766,
                    "end": 65535
                  },
            {
              "sequence": 60,
              "grant": "permit",
              "protocol": "ospf",
              "source": {
                "any": true
              },
              "destination": {
                "any": true
              },
              "log": {
                "set": true
              }
            },
            {
              "sequence": 70,
              "grant": "permit",
              "protocol": "icmp",
              "source": {
                "any": true
              },
              "destination": {
                "any": true
              },
              "log": {
                "set": true
              }
            }
                }
              },
              "log": {
                "set": true
              }
            }
          ]
        },
        {
          "name": "meraki-fqdn-dns",
          "acl_type": "extended"
        }
      ]
    }
~~~
## Step 2 - Verify the new ACL
1. Access rtr1 and rtr3 to verfify the new ACL `ansible`

rtr1
~~~
rtr1#sh ip access-lists ansible
Extended IP access list ansible
    10 permit tcp host 192.168.1.1 host 192.168.3.3 eq www log
    20 permit tcp host 192.168.1.1 host 192.168.3.3 eq 443 log
    30 permit tcp host 192.168.1.1 host 192.168.3.3 eq 22 log
    40 permit tcp host 192.168.1.1 host 192.168.3.3 eq 830 log
    50 permit tcp host 192.168.1.1 host 192.168.3.3 range 32766 65535 log
    60 permit ospf any any log
    70 permit icmp any any log
~~~

rtr3
~~~
ec2-user@rtr3> show configuration firewall family inet filter ansible | display set 
set firewall family inet filter ansible term web from source-address 192.168.3.3/32
set firewall family inet filter ansible term web from destination-address 192.168.1.1/32
set firewall family inet filter ansible term web from protocol tcp
set firewall family inet filter ansible term web from destination-port 80
set firewall family inet filter ansible term web then accept
set firewall family inet filter ansible term https from source-address 192.168.3.3/32
set firewall family inet filter ansible term https from destination-address 192.168.1.1/32
set firewall family inet filter ansible term https from protocol tcp
set firewall family inet filter ansible term https from destination-port 443
set firewall family inet filter ansible term https then accept
set firewall family inet filter ansible term ssh from source-address 192.168.3.3/32
set firewall family inet filter ansible term ssh from destination-address 192.168.1.1/32
set firewall family inet filter ansible term ssh from protocol tcp
set firewall family inet filter ansible term ssh from destination-port 22
set firewall family inet filter ansible term ssh then accept
set firewall family inet filter ansible term netconf from source-address 192.168.3.3/32
set firewall family inet filter ansible term netconf from destination-address 192.168.1.1/32
set firewall family inet filter ansible term netconf from protocol tcp
set firewall family inet filter ansible term netconf from destination-port 830
set firewall family inet filter ansible term netconf then accept
set firewall family inet filter ansible term ephem from source-address 192.168.3.3/32
set firewall family inet filter ansible term ephem from destination-address 192.168.1.1/32
set firewall family inet filter ansible term ephem from protocol tcp
set firewall family inet filter ansible term ephem from destination-port 32766-65535
set firewall family inet filter ansible term ephem then accept
set firewall family inet filter ansible term ospf from protocol ospf
set firewall family inet filter ansible term ospf then accept
set firewall family inet filter ansible term icmp from protocol icmp
set firewall family inet filter ansible term icmp then accept
~~~

## Step 3 - Modify an ACL 
1. Modify rtr1's ansible acl from hte CLI

~~~


* 1-check_acl.yml: This playbook provides a check to identify the "meetup" ACL is present on both the Cisco and Jumiper routers. It uses Gather and Assertions.
* 2-gather_acls: This playbook gathers the existing ACLs and ACE entries and saves them as a YAML host variable file to run playbooks against
* 3-gather_drift.yml: This playbook creates a diff file to identify deltas between the intended ACL configuration in the host_vars versus the actual running configuration
* 4-merge.yml: This playbook pushes ACL configuration additions to the routers
* 5-replace.yml: This playbook changes existing ACL/ACE entries on the router.
* 6-overwrite.yml: This playbook adds or removes "overwrites" sections of the ACLs
* 7-delete.yml: This plabook removes the entire ACLs
* 8-rendered: This playbook converts the structure data in vars files to the native configs that are sent the router. (ie., CLI or netconf etc.). This is read only.
