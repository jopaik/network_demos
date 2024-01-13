## Return to Day 2 Exercises
* [Day 2 ](../../README.md)

# Network Backups GIT

[Table of Contents](#table-of-contents)
- [Step 1 - Credential](#step-1---credential)
- [Step 2 - Job-template](#step-2---job-template)
- [Step 3 - Review](#step-3---review)
- [Step 4 - Backups and Restore Job-Templates](#step-4---backups-and-restore-job-templates)
- [Step 5 - Network - Backup and Restore Workflow](#step-5---network---backup-and-restore-workflow)

## Objective

Backup multi-vendor router configurations to Gitea and be able to restore them if needed.

## Overview

This demo uses the ansible.scm collection and the network.backup role from Validated Content to backup router configurations to git branches in Gitea. Additionally we will check for configuration drift and restore configurations when appropriate.

### Step 1 - Collect Backup Configurations
Access your AAP Controller from your POD and run the 'Network-Backups-Git' job template 

Output - Network-Backups-Git
```
Identity added: /runner/artifacts/4/ssh_key_data (/runner/artifacts/4/ssh_key_data)

PLAY [Backup Cisco Configs to gitlab] ******************************************

TASK [Retrieve a repository from a distant location and make it available tothe local EE] ***
skipping: [rtr2]
skipping: [rtr4] 
skipping: [rtr1]
skipping: [rtr3]
changed: [localhost]

TASK [Backup ios configurations for selected devices] **************************
skipping: [localhost]
skipping: [rtr2]
skipping: [rtr4]
skipping: [rtr3]
changed: [rtr1]

TASK [Backup eos configurations for selected devices] **************************
skipping: [localhost]
skipping: [rtr1]
skipping: [rtr3]
changed: [rtr2]
changed: [rtr4]

TASK [Backup junos configurations for selected devices] ************************
skipping: [localhost]
skipping: [rtr2]
skipping: [rtr4]
skipping: [rtr1]
changed: [rtr3]

TASK [Publish the changes] *****************************************************
skipping: [rtr2]
skipping: [rtr4]
skipping: [rtr1]
skipping: [rtr3]
changed: [localhost]

PLAY RECAP *********************************************************************
localhost                  : ok=2    changed=2    unreachable=0    failed=0    skipped=3    rescued=0    ignored=0   
rtr1                       : ok=1    changed=1    unreachable=0    failed=0    skipped=4    rescued=0    ignored=0   
rtr2                       : ok=1    changed=1    unreachable=0    failed=0    skipped=4    rescued=0    ignored=0   
rtr3                       : ok=1    changed=1    unreachable=0    failed=0    skipped=4    rescued=0    ignored=0   
rtr4                       : ok=1    changed=1    unreachable=0    failed=0    skipped=4    rescued=0    ignored=0   
```
### Step 3 - Review 

1. Open your 'student-repo' url on gitlab.com and review the repository and files
    - https://gitlab.com/username/student-repo.git  `<--change to your username this is just a placeholder here`
1. Click branches under "student-repo", and locate the branch with the latest timestamp from Network-Backups-git job-template.

![Branch](../../images/branch.png)

- Navigate to the backups folder and review the router config files.
**day2/1-opportunistic/2-backup-and-restore/backups/**

![Branch](../../images/backups.png)

* Additionally the new branch could be merged into main, but we will table the use of 'git merge' for now as we will utilize a mrge rquest later as part of the capstone exercise-6.

### Step 4 - Backups and Restore Job-Templates
In this step you will create a workflow to access the saved router backups such that the configs can rollback based on a timestamp. Hint, you can copy from other job-templates but take care to configure them exactly like the bellow screen shots. Also you will need to remove any existing surveys from copied job-emplates.

1. Go to Resources > Templates, click on **Add** at the top of the screen, and select **Add job template** 
- Name: **Network-Backups-Server**
- Job Type: **Run**
- Inventory: **Workshop Inventory**
- Project: **Student Project**
- Playbook: **day2/1-opportunistic/2-backup-and-restore/2-backups.yml**
- Credential: **Type:'Machine' Credential:'Workshop Credential**
- Credential: **Type:'Red Hat Ansible Automation Platform' Credential:'Controller Credential'**
- Execution Environment: **Validated Network**

 ![Job-template](../../images/jobtemplatebackupserver.png)
 Review the contents of 2-backups.yml in VSCode

2. Go to Resources > Templates, click on **Add** at the top of the screen, and select **Add job template** 
- Name: **Network-Change**
- Job Type: **Run**
- Inventory: **Workshop Inventory**
- Project: **Student Project**
- Playbook: **day2/1-opportunistic/2-backup-and-restore/3-change.yml**
- Credential: **Type:'Machine' Credential:'Workshop Credential**
- Execution Environment: **Validated Network**

![Job-template](../../images/job-template-change.png)
Review the contents of 3-check.yml in VSCode
> Note: an interface description of `student1` is added to the loopback0 interfaces. 


3. Go to Resources > Templates, click on **Add** at the top of the screen, and select **Add job template** 
- Name: **Network-Automation-Restore**
- Job Type: **Run**
- Inventory: **Workshop Inventory**
- Project: **Student Project**
- Playbook: **day2/1-opportunistic/2-backup-and-restore/4-network_restore.yml**
- Credential: **Type:'Machine' Credential:'Workshop Credential**
- Credential: **Type:'Red Hat Ansible Automation Platform' Credential:'Controller Credential**
- Execution Environment: **Validated Network**

![Job-template](../../images/job-template-restore.png)
Review the contents of 4-network_restore.yml in VSCode


4. Go to Resources > Templates, click on **Add** at the top of the screen, and select **Add job template** 
- Name: **Network-Verify**
- Job Type: **Run**
- Inventory: **Workshop Inventory**
- Project: **Student Project**
- Playbook: **day2/1-opportunistic/2-backup-and-restore/5-verify.yml**
- Credential: **Type:'Machine' Credential:'Workshop Credential**
- Execution Environment: **Validated Network**

![Job-template](../../images/jobtemplateverify.png)
Review the contents of 5-verify.yml in VSCode

> Note: this playbook will verify the rollback removed the loopback0 interface description `student1` from each router.

### Step 5 - Network - Backup and Restore Workflow
Workflows provide a method to orchestrate running multiple job-templates with (pass, fail, and always) conditionals and logic. In fact, workflows can also run multiple workflows!
In this step we will stitch together our job-templates. In this scenario, the workflow will backup configurations, make a change to the devices, simulate making a mistake and rolling back to the backup configuration.


- The following is the visualiation of the afore mentioned workflow.

![Workflow](../../images/backupworkflow1.png)

Configure the `Network - Backup and Restore Workflow`  \
Go to Resources > Templates, click on **Add** at the top of the screen, and select **Add workflow template** 
- Name: **Network - Backup and Restore Workflow**
- Organization: **Red Hat network organization**
- Inventory: **Workshop Inventory**

Click **Save** to save the workflow template.  This will drop you into the visualizer for the workflow.  
![Workflow](../../images/addworkflowbackup.png)

![Workflow](../../images/configbackupworkflow.png)

![Start](../../images/start.png)

Click the **Start** button to begin.

Complete the workflow by adding the Network-Backups-Server, Network-Change, Restore, and Verify with "success" condition links.

Select:
- Node Type: Job Template
- Job Template: Network-Backups-Server

Hover over "Network-Backupds-Server" node, and select the **+**, and select **On Success** \
- Node Type: Job Template
- Job Template: Network-Change

Hover over "Network-Change" node, and select the **+**, and select **On Success** \
- Node Type: Job Template
- Job Template: Network-Automation-Restore

Hover over "Network-Automation-Restore" node, and select the **+**, and select **On Success** \
- Node Type: Job Template
- Job Template: Network-Verify

Click **Save** to save the workflow template.

On the Templates > Network - Backup and Restore Workflow details page, click the **Launch** button.

Output Network-Backups-Server \
To see the individual job-template ouput you can click on the node box within the workflow or click on jobs in the left frame.

```
Identity added: /runner/artifacts/15/ssh_key_data (/runner/artifacts/15/ssh_key_data)

PLAY [retrieve network configurations] *****************************************

TASK [determine that both AAP and Machine credentials are set] *****************
ok: [rtr4] => {
    "changed": false,
    "msg": "All assertions passed"
}
ok: [rtr1] => {
    "changed": false,
    "msg": "All assertions passed"
}
ok: [rtr2] => {
    "changed": false,
    "msg": "All assertions passed"
}
ok: [rtr3] => {
    "changed": false,
    "msg": "All assertions passed"
}

TASK [determine that both AAP and Machine credentials are set] *****************
ok: [rtr2] => {
    "msg": [
        "admin",
        "emk0kx3j",
        "student1.hh6sd.example.opentlc.com"
    ]
}
ok: [rtr4] => {
    "msg": [
        "admin",
        "emk0kx3j",
        "student1.hh6sd.example.opentlc.com"
    ]
}
ok: [rtr3] => {
    "msg": [
        "admin",
        "emk0kx3j",
        "student1.hh6sd.example.opentlc.com"
    ]
}
ok: [rtr1] => {
    "msg": [
        "admin",
        "emk0kx3j",
        "student1.hh6sd.example.opentlc.com"
    ]
}

TASK [backup configuration] ****************************************************

TASK [roles/backup : backup network device config] *****************************
included: /runner/project/day2/1-opportunistic/2-backup-and-restore/roles/backup/tasks/eos.yml for rtr2, rtr4 => (item=/runner/project/day2/1-opportunistic/2-backup-and-restore/roles/backup/tasks/eos.yml)
included: /runner/project/day2/1-opportunistic/2-backup-and-restore/roles/backup/tasks/ios.yml for rtr1 => (item=/runner/project/day2/1-opportunistic/2-backup-and-restore/roles/backup/tasks/ios.yml)
included: /runner/project/day2/1-opportunistic/2-backup-and-restore/roles/backup/tasks/junos.yml for rtr3 => (item=/runner/project/day2/1-opportunistic/2-backup-and-restore/roles/backup/tasks/junos.yml)

TASK [roles/backup : backup arista configuration] ******************************
changed: [rtr2]
changed: [rtr4]

TASK [roles/backup : backup cisco ios configuration] ***************************
changed: [rtr1]

TASK [roles/backup : debug] ****************************************************
ok: [rtr1] => {
    "config_output": {
        "backup_path": "/tmp/rtr1.txt",
        "changed": true,
        "date": "2023-08-16",
        "failed": false,
        "time": "21:44:12"
    }
}

TASK [roles/backup : remove non config lines - regexp] *************************
changed: [rtr1 -> localhost]

TASK [roles/backup : ensure netconf is running] ********************************
ok: [rtr3]

TASK [roles/backup : backup junos configuration] *******************************
changed: [rtr3]

TASK [create time stamp for play] **********************************************
ok: [rtr2 -> backup-server(18.220.179.198)]

TASK [Create a directory if it does not exist] *********************************
ok: [rtr2 -> backup-server(18.220.179.198)]

TASK [save configuration to backup server] *************************************
changed: [rtr2 -> backup-server(18.220.179.198)]
changed: [rtr4 -> backup-server(18.220.179.198)]
changed: [rtr1 -> backup-server(18.220.179.198)]
changed: [rtr3 -> backup-server(18.220.179.198)]

TASK [find backups] ************************************************************
ok: [rtr2 -> backup-server(18.220.179.198)]

TASK [create restore job template] *********************************************
[WARNING]: You are running collection version 4.4.0 but connecting to Red Hat
Ansible Automation Platform version 4.3.1
changed: [rtr2]

PLAY RECAP *********************************************************************
rtr1                       : ok=7    changed=3    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
rtr2                       : ok=9    changed=3    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
rtr3                       : ok=6    changed=2    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
rtr4                       : ok=5    changed=2    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0     
```
Output Network-Change
- Note, an interface description of `student1` is added to the loopback0 interfaces. 

```
Identity added: /runner/artifacts/17/ssh_key_data (/runner/artifacts/17/ssh_key_data)

PLAY [Make a quick change on the routers] **************************************

TASK [Merge provided configuration IOS device configuration] *******************
skipping: [rtr2]
skipping: [rtr4]
skipping: [rtr3]
changed: [rtr1]

TASK [ansible.builtin.debug] ***************************************************
skipping: [rtr2]
skipping: [rtr4]
skipping: [rtr3]
ok: [rtr1] => {
    "output": {
        "after": [
            {
                "enabled": true,
                "name": "GigabitEthernet1"
            },
            {
                "description": "student1",
                "enabled": true,
                "name": "Loopback0"
            },
            {
                "enabled": true,
                "name": "Tunnel0"
            },
            {
                "enabled": true,
                "name": "Tunnel1"
            },
            {
                "enabled": true,
                "name": "VirtualPortGroup0"
            }
        ],
        "before": [
            {
                "enabled": true,
                "name": "GigabitEthernet1"
            },
            {
                "enabled": true,
                "name": "Loopback0"
            },
            {
                "enabled": true,
                "name": "Tunnel0"
            },
            {
                "enabled": true,
                "name": "Tunnel1"
            },
            {
                "enabled": true,
                "name": "VirtualPortGroup0"
            }
        ],
        "changed": true,
        "commands": [
            "interface loopback0",
            "description student1"
        ],
        "failed": false
    }
}

TASK [Merge provided configuration EOS device configuration] *******************
skipping: [rtr1]
skipping: [rtr3]
changed: [rtr2]
changed: [rtr4]

TASK [ansible.builtin.debug] ***************************************************
skipping: [rtr1]
skipping: [rtr3]
ok: [rtr2] => {
    "output": {
        "after": [
            {
                "enabled": true,
                "mode": "layer3",
                "name": "Ethernet1"
            },
            {
                "enabled": true,
                "mode": "layer3",
                "name": "Ethernet100"
            },
            {
                "description": "student1",
                "enabled": true,
                "name": "Loopback0"
            },
            {
                "enabled": true,
                "mtu": 1394,
                "name": "Tunnel0"
            },
            {
                "enabled": true,
                "name": "Tunnel1"
            }
        ],
        "before": [
            {
                "enabled": true,
                "mode": "layer3",
                "name": "Ethernet1"
            },
            {
                "enabled": true,
                "mode": "layer3",
                "name": "Ethernet100"
            },
            {
                "enabled": true,
                "name": "Loopback0"
            },
            {
                "enabled": true,
                "mtu": 1394,
                "name": "Tunnel0"
            },
            {
                "enabled": true,
                "name": "Tunnel1"
            }
        ],
        "changed": true,
        "commands": [
            "interface Loopback0",
            "description student1"
        ],
        "failed": false
    }
}
ok: [rtr4] => {
    "output": {
        "after": [
            {
                "enabled": true,
                "mode": "layer3",
                "name": "Ethernet1"
            },
            {
                "enabled": true,
                "mode": "layer3",
                "name": "Ethernet100"
            },
            {
                "description": "student1",
                "enabled": true,
                "name": "Loopback0"
            },
            {
                "enabled": true,
                "mtu": 1394,
                "name": "Tunnel0"
            }
        ],
        "before": [
            {
                "enabled": true,
                "mode": "layer3",
                "name": "Ethernet1"
            },
            {
                "enabled": true,
                "mode": "layer3",
                "name": "Ethernet100"
            },
            {
                "enabled": true,
                "name": "Loopback0"
            },
            {
                "enabled": true,
                "mtu": 1394,
                "name": "Tunnel0"
            }
        ],
        "changed": true,
        "commands": [
            "interface Loopback0",
            "description student1"
        ],
        "failed": false
    }
}

TASK [Merge provided configuration Junos device configuration] *****************
skipping: [rtr2]
skipping: [rtr4]
skipping: [rtr1]
changed: [rtr3]

TASK [ansible.builtin.debug] ***************************************************
skipping: [rtr2]
skipping: [rtr4]
skipping: [rtr1]
ok: [rtr3] => {
    "output": {
        "after": [
            {
                "enabled": true,
                "name": "gr-0/0/0"
            },
            {
                "description": "student1",
                "enabled": true,
                "name": "lo0"
            },
            {
                "enabled": true,
                "name": "fxp0"
            }
        ],
        "before": [
            {
                "enabled": true,
                "name": "gr-0/0/0"
            },
            {
                "enabled": true,
                "name": "lo0"
            },
            {
                "enabled": true,
                "name": "fxp0"
            }
        ],
        "changed": true,
        "commands": [
            "<nc:interfaces xmlns:nc=\\"urn:ietf:params:xml:ns:netconf:base:1.0\\"><nc:interface><nc:name>lo0</nc:name><nc:description>student1</nc:description><nc:enable/></nc:interface></nc:interfaces>"
        ],
        "failed": false
    }
}

PLAY RECAP *********************************************************************
rtr1                       : ok=2    changed=1    unreachable=0    failed=0    skipped=4    rescued=0    ignored=0   
rtr2                       : ok=2    changed=1    unreachable=0    failed=0    skipped=4    rescued=0    ignored=0   
rtr3                       : ok=2    changed=1    unreachable=0    failed=0    skipped=4    rescued=0    ignored=0   
rtr4                       : ok=2    changed=1    unreachable=0    failed=0    skipped=4    rescued=0    ignored=0   
```
Output Network-Automation-Restore

```
Identity added: /runner/artifacts/19/ssh_key_data (/runner/artifacts/19/ssh_key_data)

PLAY [restore router configurations] *******************************************

TASK [retreive configuration from backup-server to execution environment] ******
changed: [rtr4 -> backup-server(18.220.179.198)]
changed: [rtr2 -> backup-server(18.220.179.198)]
changed: [rtr3 -> backup-server(18.220.179.198)]
changed: [rtr1 -> backup-server(18.220.179.198)]

TASK [load restore role] *******************************************************

TASK [roles/restore : load platform module for restore] ************************
included: /runner/project/day2/1-opportunistic/2-backup-and-restore/roles/restore/tasks/eos.yml for rtr2, rtr4 => (item=/runner/project/day2/1-opportunistic/2-backup-and-restore/roles/restore/tasks/eos.yml)
included: /runner/project/day2/1-opportunistic/2-backup-and-restore/roles/restore/tasks/ios.yml for rtr1 => (item=/runner/project/day2/1-opportunistic/2-backup-and-restore/roles/restore/tasks/ios.yml)
included: /runner/project/day2/1-opportunistic/2-backup-and-restore/roles/restore/tasks/junos.yml for rtr3 => (item=/runner/project/day2/1-opportunistic/2-backup-and-restore/roles/restore/tasks/junos.yml)

TASK [roles/restore : debug] ***************************************************
ok: [rtr2] => {
    "msg": "restoring from /backup/2023-08-16-21-32/rtr2.txt"
}
ok: [rtr4] => {
    "msg": "restoring from /backup/2023-08-16-21-32/rtr4.txt"
}

TASK [roles/restore : restore the config] **************************************
[WARNING]: To ensure idempotency and correct diff the input configuration lines
should be similar to how they appear if present in the running configuration on
device including the indentation
changed: [rtr4]
changed: [rtr2]

TASK [roles/restore : print to terminal window] ********************************
ok: [rtr2] => {
    "msg": "Restore is complete for device rtr2 is set to 2023-08-16-21-32 timestamp"
}
ok: [rtr4] => {
    "msg": "Restore is complete for device rtr4 is set to 2023-08-16-21-32 timestamp"
}

TASK [roles/restore : debug] ***************************************************
ok: [rtr1] => {
    "msg": "restoring from /backup/2023-08-16-21-32/rtr1.txt"
}

TASK [roles/restore : Include task list in play] *******************************
included: /runner/project/day2/1-opportunistic/2-backup-and-restore/roles/restore/tasks/ios/overwrite.yml for rtr1

TASK [roles/restore : copy file over to flash on network device] ***************
changed: [rtr1 -> localhost]

TASK [roles/restore : overwrite startup config - archive] **********************
[WARNING]: To ensure idempotency and correct diff the input configuration lines
should be similar to how they appear if present in the running configuration on
device
changed: [rtr1]

TASK [roles/restore : overwrite startup config - overwrite] ********************
ok: [rtr1]

TASK [roles/restore : print to terminal window] ********************************
ok: [rtr1] => {
    "msg": "Restore is complete for device rtr1 is set to 2023-08-16-21-32 timestamp, restored with restore_mode overwrite "
}

TASK [roles/restore : debug] ***************************************************
ok: [rtr3] => {
    "msg": "restoring from /backup/2023-08-16-21-32/rtr3.txt"
}

TASK [roles/restore : restore the config] **************************************
ok: [rtr3]

TASK [roles/restore : print to terminal window] ********************************
ok: [rtr3] => {
    "msg": "Restore is complete for device rtr3 is set to 2023-08-16-21-32 timestamp"
}

PLAY RECAP *********************************************************************
rtr1                       : ok=8    changed=3    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
rtr2                       : ok=5    changed=2    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
rtr3                       : ok=5    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
rtr4                       : ok=5    changed=2    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
```
Output Network-Verify
- Note, this playbook will verify the rollback removed the loopback0 interface description `student1` from each router.

```
Identity added: /runner/artifacts/21/ssh_key_data (/runner/artifacts/21/ssh_key_data)

PLAY [Verify Rollbacks] ********************************************************

TASK [Merge provided configuration IOS device configuration] *******************
skipping: [rtr2]
skipping: [rtr4]
skipping: [rtr3]
ok: [rtr1]

TASK [ansible.builtin.debug] ***************************************************
skipping: [rtr2]
skipping: [rtr4]
skipping: [rtr3]
ok: [rtr1] => {
    "output.gathered": [
        {
            "enabled": true,
            "name": "GigabitEthernet1"
        },
        {
            "enabled": true,
            "name": "Loopback0"
        },
        {
            "enabled": true,
            "name": "Tunnel0"
        },
        {
            "enabled": true,
            "name": "Tunnel1"
        },
        {
            "enabled": true,
            "name": "VirtualPortGroup0"
        }
    ]
}

TASK [Merge provided configuration EOS device configuration] *******************
skipping: [rtr3]
skipping: [rtr1]
ok: [rtr4]
ok: [rtr2]

TASK [ansible.builtin.debug] ***************************************************
skipping: [rtr1]
skipping: [rtr3]
ok: [rtr2] => {
    "output.gathered": [
        {
            "enabled": true,
            "mode": "layer3",
            "name": "Ethernet1"
        },
        {
            "enabled": true,
            "mode": "layer3",
            "name": "Ethernet100"
        },
        {
            "enabled": true,
            "name": "Loopback0"
        },
        {
            "enabled": true,
            "mtu": 1394,
            "name": "Tunnel0"
        },
        {
            "enabled": true,
            "name": "Tunnel1"
        }
    ]
}
ok: [rtr4] => {
    "output.gathered": [
        {
            "enabled": true,
            "mode": "layer3",
            "name": "Ethernet1"
        },
        {
            "enabled": true,
            "mode": "layer3",
            "name": "Ethernet100"
        },
        {
            "enabled": true,
            "name": "Loopback0"
        },
        {
            "enabled": true,
            "mtu": 1394,
            "name": "Tunnel0"
        }
    ]
}

TASK [Merge provided configuration Junos device configuration] *****************
skipping: [rtr2]
skipping: [rtr4]
skipping: [rtr1]
ok: [rtr3]

TASK [ansible.builtin.debug] ***************************************************
skipping: [rtr2]
skipping: [rtr4]
skipping: [rtr1]
ok: [rtr3] => {
    "output.gathered": [
        {
            "enabled": true,
            "name": "gr-0/0/0"
        },
        {
            "description": "student1",
            "enabled": true,
            "name": "lo0"
        },
        {
            "enabled": true,
            "name": "fxp0"
        }
    ]
}

PLAY RECAP *********************************************************************
rtr1                       : ok=2    changed=0    unreachable=0    failed=0    skipped=4    rescued=0    ignored=0   
rtr2                       : ok=2    changed=0    unreachable=0    failed=0    skipped=4    rescued=0    ignored=0   
rtr3                       : ok=2    changed=0    unreachable=0    failed=0    skipped=4    rescued=0    ignored=0   
rtr4                       : ok=2    changed=0    unreachable=0    failed=0    skipped=4    rescued=0    ignored=0   
```

# Congratulations, Exercise-2 is complete!

## Next Exercise
* [Dynamic Documentation ](../3-dynamic-documentation/README.md)

[Click Here to return to the Ansible Network Automation Workshop](../README.md)