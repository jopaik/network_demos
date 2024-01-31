## Return to Demo Menu
 - [Menu of Demos](../README.md)

# Summary of steps
1. Launch the Network ACLS Deploy job-template
2. Verify the new ACL was `merged` and applied to rtr1 and rtr3
3. Modify an ACL entry from the CLI
4. Launch the Network ACLs Detect job-template
5. Review AAP output to determine the Configuration drift
6. Launch the Network ACLs Remediate Template
8. Verify that the ACL entry is returned to it's original configuration

# Network Backups GIT

[Table of Contents](#table-of-contents)
- [Step 1 - Launch the Network ACLS Deploy job-template](#step-1---credential)
- [Step 2 - Verify the new ACL](#step-2---job-template)
- [Step 3 - Modify an ACL](#step-3---modify-an-acl)
- [Step 4 - Launch the Network ACLs Detect job-template](#step-4-launch-the-network-acls-detect-job-template)
- [Step 5 -  Launch the Network ACLs Remediate Template](#step-5-launch-the-network-acls-remediate-job-template)
- [Step 6 - Verify the ACL change](#step-6-verify-the-acl-change)
- [Step 7 - Change an existing entry](#step-7-change-an-existing-entry)
- [Step 8 - Launch the Network ACLs Remediate Template](#step-8-launch-the-network-acls-remediate-template)



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
    "10 permit tcp host 192.168.1.1 host 192.168.3.3 eq www log",
    "20 permit tcp host 192.168.1.1 host 192.168.3.3 eq 443 log",
    "30 permit tcp host 192.168.1.1 host 192.168.3.3 eq 22 log",
    "40 permit tcp host 192.168.1.1 host 192.168.3.3 eq 830 log",
    "50 permit tcp host 192.168.1.1 host 192.168.3.3 range 32766 65535 log",
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
                "host": "192.168.1.1"
              },
              "destination": {
                "host": "192.168.3.3",
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
                "host": "192.168.1.1"
              },
              "destination": {
                "host": "192.168.3.3",
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
                "host": "192.168.1.1"
              },
              "destination": {
                "host": "192.168.3.3",
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
                "host": "192.168.1.1"
              },
              "destination": {
                "host": "192.168.3.3",
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
                "host": "192.168.1.1"
              },
              "destination": {
                "host": "192.168.3.3",
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
1. Modify rtr1's ansible acl from the VSCode CLI
This will simulate a mistake made outside of automation.

~~~
$ ssh rtr1
conf t
ip access-list extended ansible
no 10
10 permit tcp host 192.168.10.1 host 192.168.30.3 eq 8080 log
~~~

## Step 4 - Launch the Network ACLs Detect job-template
This playbook will identify if the ACL entry drifts away from the Single Source of Truth (SSOT) `host_vars`

Ouptut
~~~
TASK [network.base.resource_manager : Retrieve a repository from a distant location and make it available locally] ***
fatal: [rtr1]: FAILED! => {"changed": false, "msg": "configuration drift is found in cisco.ios.ios_acl_interfaces Resource"}
~~~

## Step 5 -  Launch the Network ACLs Remediate Template
This playbook will push the ACL configurations from the host_vars to the device. Remediate uses the state `overridden` for network.acls.run.

Output:
~~~
{
  "commands": [
    "ip access-list extended ansible",
    "no 10 permit tcp host 192.168.10.1 host 192.168.30.3 eq 8080 log",
    "10 permit tcp host 192.168.1.1 host 192.168.3.3 eq www log"
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
          "name": "ansible",
          "acl_type": "extended",
          "aces": [
            {
              "sequence": 10,
              "grant": "permit",
              "protocol": "tcp",
              "source": {
                "host": "192.168.10.1"
              },
              "destination": {
                "host": "192.168.30.3",
                "port_protocol": {
                  "eq": "8080"
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
                "host": "192.168.1.1"
              },
              "destination": {
                "host": "192.168.3.3",
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
                "host": "192.168.1.1"
              },
              "destination": {
                "host": "192.168.3.3",
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
                "host": "192.168.1.1"
              },
              "destination": {
                "host": "192.168.3.3",
                "port_protocol": {
                  "eq": "830"
                }
              },
              "log": {
                "set": true
              }
            },
            {
              "sequence": 50,
              "grant": "permit",
              "protocol": "tcp",
              "source": {
                "host": "192.168.1.1"
              },
              "destination": {
                "host": "192.168.3.3",
                "port_protocol": {
                  "range": {
                    "start": 32766,
                    "end": 65535
                  }
                }
              },
              "log": {
                "set": true
              }
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
                "host": "192.168.1.1"
              },
              "destination": {
                "host": "192.168.3.3",
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
                "host": "192.168.1.1"
              },
              "destination": {
                "host": "192.168.3.3",
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
                "host": "192.168.1.1"
              },
              "destination": {
                "host": "192.168.3.3",
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
                "host": "192.168.1.1"
              },
              "destination": {
                "host": "192.168.3.3",
                "port_protocol": {
                  "eq": "830"
                }
              },
              "log": {
                "set": true
              }
            },
            {
              "sequence": 50,
              "grant": "permit",
              "protocol": "tcp",
              "source": {
                "host": "192.168.1.1"
              },
              "destination": {
                "host": "192.168.3.3",
                "port_protocol": {
                  "range": {
                    "start": 32766,
                    "end": 65535
                  }
                }
              },
              "log": {
                "set": true
              }
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
          ]
        }
~~~

## Step 6 - Verify the ACL change
1. Access rtr1 to verfify the new ACL `ansible`

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
## Step 7 - Change an existing entry
1. Make a change to host_vars/rtr1/acls.yaml

Modify sequence 10 to use tcp port 8080
~~~
 -   aces:
        -   destination:
                host: 192.168.3.3
                port_protocol:
                    eq: 8080
            grant: permit
            log:
                set: true
            protocol: tcp
            sequence: 10
            source:
                host: 192.168.1.1
~~~
Make sure you save the file and push to gitea.

2. Complete the git steps for your change. You must save, commit the file in the VSCode IDE and "sync" push to gitea after fixing the file.
![Save](../../images/save_commit.png)

or update from the terminal
~~~
git add --all
git commit -m "deploy"
git push
~~~

## Step 8 - Launch the Network ACLs Remediate Template
Since we are modifing an existing entry we would use remediate. `override`. If it were a new entry we could use deploy `merge`

1. Review the changed tasks in hte output.

~~~
{
  "commands": [
    "ip access-list extended ansible",
    "no 10 permit tcp host 192.168.1.1 host 192.168.3.3 eq www log",
    "10 permit tcp host 192.168.1.1 host 192.168.3.3 eq 8080 log"
~~~

# Key Takeaways
* 

## Return to Demo Menu
 - [Menu of Demos](../README.md)