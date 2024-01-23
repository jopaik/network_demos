**Optional task:  List the installed Collections from an AAP Execution Environment**
- `skip to step 3 below if not interested` 

In the AAP Controller adhoc commands can be ran from an inventory group. In the below example we will limit the command to rtr1 from the group since we are actually running the command from the shell on the execution environment container, not the router, when `running` an adhoc command.

- Navigate to inventory/groups to run adhoc commands form the AAP controller. Notice the run command button below.
 ![adhoc](../../images/adhoc1.png)
 - Use the shell command module to run commands similar to the CLI
 - ansible-galaxy collection list will display the installed collections for an EE
 - Limit to a single device in the inventory to save time
 ![adhoc](../../images/adhoc2.png)
 - Select an execution environment. This EE includes the network.base collection
 ![adhoc](../../images/adhoc3.png)
- Select a credential
 ![adhoc](../../images/adhoc4.png)
- Run the adhoc command and locate the network.base in the output.
 ![adhoc](../../images/adhoc5.png)


