## Return to Demo Menu
 - [Menu of Demos](../README.md)

# Summary of steps
1. Install gdown
2. Download the two c8000v images to `network_upgrade_as_code` and push to gitea
3. Move the images out of the repo when done.
4. Run the Network-Upgrade-Workflow template and choose image and approve the upgrade
6. Review the Network-Upgrade-Upgrade jog-template 

# Network Upgrade as Code

[Table of Contents](#table-of-contents)
- [Step 1 - Install gdown](#step-1-install-gdown)
- [Step 2 - Download Images](#step-2-download-images)
- [Step 3 - Run the staging job template](step-3-run-the-staging-job-template)
- [Step 4 - Move Images](step-3-move-images)
- [Step 5 - Run the Demo](#step-4-run-the-demo)
- [Step 6 - Review the Network-Upgrade-Upgrade](#step-5-review-the-network-upgrade-upgrade)

## Objective
To stage firmware images and upgrade network devices with Ansible. Please note it takes several minutes to both stage files and upgrade.   

## Overview
Ansible can scp firmware images to network devices. The workflow includes an approval node to control when an upgrade will be activated based on change control.  

### Step 1 - Install gdown
Install gdown
~~~
pip install gdown
~~~

### Step 2 - Download Images
From the folder `network_upgrade_as_code/`
1. 
~~~
gdown https://drive.google.com/uc?id=1_MNn6pcDJ0AYNYExyGqJNgd_XCRNqIUx
gdown https://drive.google.com/uc?id=1Jt5HOe76_3ylk6uTaAQxAxMet_tSwUsK
~~~
2. Push to gitea repo
This way the image files will be available for Ansible.
Complete the git steps for your change. You must save, commit the file in the VSCode IDE and "sync" push to gitea after fixing the file.
![Save](../../images/save_commit.png)

or update from the terminal
~~~
git add --all
git commit -m "deploy"
git push
~~~
### Step 3 - Run the staging job template

This will take a few minutes due to the file size.
1. Run the Network-Upgrade-Workflow template twice and deny the approval each time. The idea is to just stage both files to save time during the demo.
~~~
17.06.06a
17.07.01a
~~~

### Step 4 Move Images
 Move the image files out of the network-demos-repo to the home directory
It's important to move the files to avoid the repo in Gitea taking a long time to update or fail. 

 mv the files
~~~
mv c8000v-universalk9.17.06.06a.SPA.bin /home/student  
mv c8000v-universalk9.17.07.01a.SPA.bin /home/student
~~~
~~~
[student@ansible-1 network_upgrade_as_code]$ ls
ansible-navigator.log                 README.md                                               staging.yml
c8000v-universalk9.17.06.06a.SPA.bin  setup.yml                                               upgrade-artifact-2024-05-29T16:59:06.427433+00:00.json
c8000v-universalk9.17.07.01a.SPA.bin  staging-artifact-2024-05-29T17:38:07.356799+00:00.json  upgrade.yml
[student@ansible-1 network_upgrade_as_code]$ mv c8000v-universalk9.17.0* ~student/
~~~
2. Push to gitea repo
This way the image files will no longer be in the repo.
Complete the git steps for your change. You must save, commit the file in the VSCode IDE and "sync" push to gitea after fixing the file.
![Save](../../images/save_commit.png)

or update from the terminal
~~~
git add --all
git commit -m "deploy"
git push
~~~
### Step 5 - Run the demo
This time run the Network-Upgrade-Workflow template and approve the upgrade

##### Remember to return to the AAP JOB for the Workflow and accept the approval node

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