## Return to Day 2 Exercises
* [Day 2 ](../../README.md)

# Network Backups GIT

[Table of Contents](#table-of-contents)
- [Step 1 - Collect Backup Configurations](#step-1---credential)
- [Step 2 - Job-template](#step-2---job-template)
- [Step 3 - Review](#step-3---review)
- [Step 4 - Backups and Restore Job-Templates](#step-4---backups-and-restore-job-templates)
- [Step 5 - Network - Backup and Restore Workflow](#step-5---network---backup-and-restore-workflow)

## Objective

To enable multi-vendor router configuration backups to Gitea and subsequently restoral of them if needed. We will also explore managing configuration drift in this demo.

## Overview

This demo uses the ansible.scm collection and the network.backup role from Validated Content to backup router configurations to git branches in Gitea. Additionally we will check for configuration drift and restore configurations when appropriate.

### Step 1 - Collect Backup Configurations
Access your AAP Controller from your RHDP POD and run the 'Network-Backups-Git' job template 

Output - Network-Backups-Git `backups.yml` with explanations
```
Identity added: /runner/artifacts/404/ssh_key_data (/runner/artifacts/404/ssh_key_data)

PLAY [Backup Cisco Configs to Gitea in Branches] *******************************

TASK [Retrieve a repository from a distant location and make it available to the local EE] ***
changed: [localhost] `This task clones the network-demos-rep from the gitea repository`

TASK [Network Backup and Resource Manager] *************************************

TASK [network.backup.run : Include tasks] **************************************
included: /usr/share/ansible/collections/ansible_collections/network/backup/roles/run/includes/validation.yaml for rtr1, rtr2, rtr4, rtr3

TASK [network.backup.run : Set supported platform list] ************************
ok: [rtr1]
ok: [rtr3]
ok: [rtr4]
ok: [rtr2]

TASK [network.backup.run : Run the platform specific tasks] ********************
included: /usr/share/ansible/collections/ansible_collections/network/backup/roles/run/includes/backup.yaml for rtr1, rtr2, rtr4, rtr3 => (item=/usr/share/ansible/collections/ansible_collections/network/backup/roles/run/includes/backup.yaml)

TASK [network.backup.run : Build Local Backup Dir Path] ************************
included: /usr/share/ansible/collections/ansible_collections/network/backup/roles/run/includes/path.yaml for rtr2, rtr1, rtr4, rtr3

TASK [network.backup.run : Set local backup path] ******************************
ok: [rtr4]
ok: [rtr1]
ok: [rtr2]
ok: [rtr3]

TASK [network.backup.run : Include tasks] **************************************
included: /usr/share/ansible/collections/ansible_collections/network/backup/roles/run/includes/network.yaml for rtr1, rtr2, rtr4, rtr3

TASK [network.backup.run : Invoke backup task] *********************************
included: /usr/share/ansible/collections/ansible_collections/network/backup/roles/run/includes/cli_backup.yaml for rtr1, rtr2, rtr4, rtr3

TASK [network.backup.run : configurable backup path] ***************************
changed: [rtr1]
changed: [rtr3]
changed: [rtr2]
changed: [rtr4]

TASK [Publish the changes] *****************************************************
changed: [localhost]

PLAY [Prepare Branches for Intent and Restore] *********************************

TASK [Retrieve a repository from a distant location and make it available to the local EE] ***
changed: [localhost]

TASK [List the Branches] *******************************************************
changed: [localhost]

TASK [Create a job-template - Network-Git-Intent] ******************************
changed: [localhost]

TASK [Create a job-template - Network-Git-Restore] *****************************
changed: [localhost]

PLAY RECAP *********************************************************************
localhost                  : ok=6    changed=6    unreachable=0    failed=0    skipped=1    rescued=0    ignored=0   
rtr1                       : ok=8    changed=1    unreachable=0    failed=0    skipped=11   rescued=0    ignored=0   
rtr2                       : ok=8    changed=1    unreachable=0    failed=0    skipped=9    rescued=0    ignored=0   
rtr3                       : ok=8    changed=1    unreachable=0    failed=0    skipped=9    rescued=0    ignored=0   
rtr4                       : ok=8    changed=1    unreachable=0    failed=0    skipped=9    rescued=0    ignored=0   
```
### Step 2 - Review 

1. Open your 'network-demos-repo' url on gitea in new browser tab and review the repository and files.

https://<student_number>.<pod_number.example.opentlc.com>/gitea/gitea/network-demos-repo  `<--change to your pod_id and student number` This will be the same url used to access the Ansible Controller in your POD with the Gitea Repo information appended.

*For example:
~~~
https://student1.hr96x.example.opentlc.com/gitea/gitea/network-demos-repo
~~~

2. Click branches under "network-demos-repo", and locate the branch with the latest timestamp from Network-Backups-git job-template. As you run the job-temaplate a new branch with the backups and timestamp is committed and pushed to gitea. These branches will be used later for config-drift and restore actions.

![Branch](../../images/branch.png)

- Navigate to the network_backup_files folder and review the router config files.
**day2/1-opportunistic/2-backup-and-restore/backups/**

![Branch](../../images/backups.png)

* Additionally the new branch could be merged into master/main branch, but we will not do that for this demo. We will only save our router configs to a non master/main branch so we can toggle between timestamps etc. Thus we can go back in time across many backups to rebuild our infrastructure. 



## Next Exercise
* [Dynamic Documentation ](../3-dynamic-documentation/README.md)

[Click Here to return to the Ansible Network Automation Workshop](../README.md)