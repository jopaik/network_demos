## Return to Demo Menu
 - [Menu of Demos](../README.md)

# Summary of steps
1. Collect Backup configurations from routers and save them to Gitea branches
2. Verify Branches in GIT `git checkout`
3. Modify the Routers from the CLI
4. Verify Job-template(s) exist
5. Launch the Network-Intended Job-Template
6. Review the Diff between the backup up configs and the running configs on the routers
7. Launch the Network Restore Job Template
8. Verify how the retore will merge the running configuration back to the original

# Network Backups GIT

[Table of Contents](#table-of-contents)
- [Step 1 - Collect Backup Configurations](#step-1---credential)
- [Step 2 - Review](#step-2---job-template)

## Objective
To enable multi-vendor router configuration backups to Gitea and subsequently restoral of them if needed. We will also explore managing configuration drift in this demo.

## Overview
This demo uses the ansible.scm collection and the network.backup role from Validated Content to backup router configurations to git branches in Gitea. Additionally we will check for configuration drift and restore configurations when appropriate.

### Step 1 - Collect Backup Configurations
Access your AAP Controller from your RHDP POD and run the 'Network-Backups-Git' job template 


* 1-check_acl.yml: This playbook provides a check to identify the "meetup" ACL is present on both the Cisco and Jumiper routers. It uses Gather and Assertions.
* 2-gather_acls: This playbook gathers the existing ACLs and ACE entries and saves them as a YAML host variable file to run playbooks against
* 3-gather_drift.yml: This playbook creates a diff file to identify deltas between the intended ACL configuration in the host_vars versus the actual running configuration
* 4-merge.yml: This playbook pushes ACL configuration additions to the routers
* 5-replace.yml: This playbook changes existing ACL/ACE entries on the router.
* 6-overwrite.yml: This playbook adds or removes "overwrites" sections of the ACLs
* 7-delete.yml: This plabook removes the entire ACLs
* 8-rendered: This playbook converts the structure data in vars files to the native configs that are sent the router. (ie., CLI or netconf etc.). This is read only.
