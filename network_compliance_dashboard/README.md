## Return to Demo Menu
 - [Menu of Demos](../README.md)

# Summary of steps
1. Deploy a Podman container with nginx for a dashboard
2. Create some configurations for devices 
3. Use Network facts to create dynamic documentation
4. Compare desired configurations in a jinja2 html template
5. Mark in red compliance violations on the dashboard
6. Resolve compiance conficts
7. Update Dashboard
8. Optional - Create a schedule to automatically update the dashboard

# Network Compliance Dashboard

  [Table of Contents](#table-of-contents)
  - [Step 1 - Job-templates](#step-1---job-templates)
  - [Step 1 - Run the Network-Config](#step-2-run-the-network-config)
  - [Step 2 - Run the Network-Compliance-Dashboard](#step-3-run-the-network-compliance-dashboard)
  - [Step 4 - Display the Dashboard](#step-4-display-the-dashboard)
  - [Step 5 - Review the files for the Dashboard](#step-5-review-the-files-for-the-dashboard)
  - [Step 7 - Change the Variables](#step-6-change-the-variables)
  - [Step 8 - Run again](#step-8-run-again)
  - [Step 9 - Optional Challenge](#step-9-optional-challenge)

## Objective
Create a web based compliance dashboard and update with Ansible. 

## Overview
In this demo you will explore a `jinja2` template used to organize compliance focused data collected with network `facts` using ansible. The compliance violations are highlighted in red. 
For this demo we will also utilize a role to install a podman container with a nginx web service to view our dashboard with the lab pod's public IP Address on tcp port 8088. As an optional bonus this job-template can be ran from a job scheduler to periodically update the dashboard.   

### Step 1 - Run the Network-Config
This job-template will run a playbook to configure some router items that fall under the scope of compliance.

### Step 2 - Run the Network-Compliance-Dashboard
Copy the IP address for the dashboard in the job output.

`example output`
~~~
TASK [../roles/build_report_container : Display link to inventory report] ******
ok: [ansible-1] => {
    "msg": [
        "Please go to http://18.221.253.245:8088"
~~~

### Step 3 - Display the Dashboard
Open a tab from your own browser and paste the url from the previous step. You will see the dashboard highlighted in red for elements that are out of compliance.Take a few minutes to explore the dashboard and associated dropdown menus to locate any compliance issues.

![Dash](../images/dash1.png)

### Step 4 - Review the files for the Dashboard

~~~
 $ cat network_compliance_dashboard/roles/build_report_container/templates/report.j2
~~~

 Note, that the `mark` tag is used to highlight elements that are not in compliance. Notice how the mark is used in the following example.

~~~
<td class="sub_net_info">{% if hostvars[network_switch]['ansible_net_version'] != desired_ios_version and hostvars[network_switch]['ansible_network_os'] == 'ios' %}<mark>{{hostvars[network_switch]['ansible_net_version']}}</mark>{% elif hostvars[network_switch]['ansible_net_version'] != desired_eos_version and hostvars[network_switch]['ansible_network_os'] == 'eos' %}<mark>{{hostvars[network_switch]['ansible_net_version']}}</mark>{% elif hostvars[network_switch]['ansible_net_version'] != desired_junos_version and hostvars[network_switch]['ansible_network_os'] == 'junos' %}<mark>{{hostvars[network_switch]['ansible_net_version']}}</mark>{% else %}{{hostvars[network_switch]['ansible_net_version']}}{% endif %}</td>
~~~     
         
 The vars/main.yml file includes the `desired_ios_version` and other variables used for the `jinja2` configuration.
- The file is located here: `network_compliance_dashboard/roles/build_report_container/vars/main.yml`

 ~~~
desired_ios_version: "17.03.06"
desired_eos_version: "4.27.1F-cloud"
desired_junos_version: "22.3R2.11"
desired_snmp: "student1"
desired_logging_host: "192.168.0.254"
~~~

This is the current contents of the network_report.yml playbook. Please note the two roles 
that are included:
* facts
* build_report_container

`network_compliance_dashboard/network_report.yml`
~~~
---
- name: Compliance Dashboard
  hosts: network
  gather_facts: false
  
  tasks:
    - name: Load read facts role
      ansible.builtin.include_role:
        name: "../roles/facts"

- name: Build report with facts
  hosts: ansible-1
  become: true
  gather_facts: false

  tasks:

    - name: Build a report
      ansible.builtin.include_role:
        name: "../roles/build_report_container"
~~~

### Step 7 - Change the Variables
The variables for the desired configs can be changed by running the solution. The solution changes the network_report.yml playbook to the a file with updated variables. Edit and launch the Network-Compliance-Dashboard after revising. See below..

![solution](../images/dashsolution.png)

Variables
~~~
desired_ios_version: "17.06.06a"
desired_eos_version: "4.27.3F-cloud"
desired_junos_version: "22.3R2.12"
desired_snmp: "student1"
desired_logging_host: "192.168.0.1"
~~~

### Step 7 - Run again
Run the `Network-Compliance-Dashboard` job-template and reload the dashboard tab on your browser.
* Note, at this point no red highlights are displayed because all configurations are compliant.
- note the url-ip address for the dashboard in the job output.

![Dash](../images/dash2.png)

### Step 8 - Optional Challenge
Create a schedule in the AAP controller to run the Network-Compliance-Dashboard job-template periodically. No screen shots available.

## Key Takeaways
* Network Facts are an easy method to discover and collect the network device configurations
* Dashboards and Reports are easy to populate with Network Facts
* THe html template is easy to modify

## Return to Demo Menu
 - [Menu of Demos](../README.md)

