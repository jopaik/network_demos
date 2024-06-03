## Return to Demo Menu
 - [Menu of Demos](../README.md)

# Summary of steps
1. Install gdown
2. Download the two c8000v images to `network_upgrade_as_code` and push to gitea
3. Move the images out of the repo when done.
4. Run the Network-Upgrade-Workflow template and choose image
5. Approve the upgrade
6. Review the Network-Upgrade-Upgrade jog-template 

# Network Upgrade as Code

[Table of Contents](#table-of-contents)
- [Step 1 - Install gdown](#step-1-install-gdown)
- [Step 2 - Download Images](#step-2-download-images)
- [Step 3 - Temporarily modify](step-3-temporarily-modify)
- [Step 4 - Network-Upgrade-Workflow](#step-3-network-upgrade-workflow)
- [Step 5 - Approve the upgrade](#step-4-approve-the-upgrade)
- [Step 6 - Review the Network-Upgrade-Upgrade](#step-5-review-the-network-upgrade-upgrade)

## Objective
To stage firmware images and upgrade network devices with Ansible. Please note it takes several minutes to both stage files and upgrade.   

## Overview
Ansible can scp firmware images to network devices. The workflow includes an approval node to control when an upgrade will be activated based on change control.  

### Step 1 - Netbox Demo Server
Install gdown
~~~
pip install gdown
~~~

### Step 2 - Download Images
From the folder `network_upgrade_as_code/`
~~~
gdown https://drive.google.com/uc?id=1_MNn6pcDJ0AYNYExyGqJNgd_XCRNqIUx
gdown https://drive.google.com/uc?id=1Jt5HOe76_3ylk6uTaAQxAxMet_tSwUsK
~~~
### Step 3 - Move the images to the /home/student directory when done
1. mv
~~~
mv c8000v-universalk9.17.06.06a.SPA.bin /home/student  
mv c8000v-universalk9.17.07.01a.SPA.bin /home/student
~~~
This will take a few minutes due to the file size.
2. Run the Network-Upgrade-Workflow template twice and deny the approval each time. The idea is to just stage both files.
~~~
17.06.06a
17.07.01a
~~~
3. Move the image files out of the network-demos-repo to the home directory
~~~
[student@ansible-1 network_upgrade_as_code]$ ls
ansible-navigator.log                 README.md                                               staging.yml
c8000v-universalk9.17.06.06a.SPA.bin  setup.yml                                               upgrade-artifact-2024-05-29T16:59:06.427433+00:00.json
c8000v-universalk9.17.07.01a.SPA.bin  staging-artifact-2024-05-29T17:38:07.356799+00:00.json  upgrade.yml
[student@ansible-1 network_upgrade_as_code]$ mv c8000v-universalk9.17.0* ~student/
~~~

4. Edit and Push .gitignore by uncommiting out the c8000v
~~~
ansible-navigator.log
*artifact*
*.swp
*c8000v-universalk9*
~~~
This step is necessary due to the file size restriction for gitea etc. 

### Step 4 - Run the Network-Upgrade-Workflow
Run the Network-Upgrade-Workflow template and choose the image to stage and upgrade
*Select the version not already running on tr1
~~~
ssh rtr1
sh ver
Cisco IOS XE Software, Version 17.06.06a
~~~

Choices
~~~
17.06.06a
17.07.01a
~~~

### Step 5 - Approve the upgrade
Return to the AAP JOB for the Workflow and accept the approval node

### Step 6 - Review the Network-Upgrade-Upgrade Job-Template output
~~~
TASK [debug] *******************************************************************
ok: [rtr1] => {
    "install_activate_output.stdout_lines": [
        [
            "install_add_activate_commit: START Wed May 29 18:47:28 UTC 2024",
            "install_add_activate_commit: Adding PACKAGE",
            "install_add_activate_commit: Checking whether new add is allowed ....",
            "",
            "--- Starting Add ---",
            "Performing Add on Active/Standby",
            "  [1] Add package(s) on R0",
            "  [1] Finished Add on R0",
            "Checking status of Add on [R0]",
            "Add: Passed on [R0]",
            "Finished Add",
            "",
            "Image added. Version: 17.06.01a.0.1",
            "install_add_activate_commit: Activating PACKAGE",
~~~
~~~
ssh rtr1
sh ver
Cisco IOS XE Software, Version 17.07.01a
~~~

# Key Takeaways
* Ansible can scp firmware images to network devices. `netcommon.net_put` 
* Approval nodes can control when an upgrade will be activated based on change control. 

## Return to Demo Menu
 - [Menu of Demos](../README.md)