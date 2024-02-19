#!/usr/bin/env python
import os
from functions import (
    clear_screen,
    generate_yaml,
    create_inventory
)

if __name__ == "__main__":
    clear_screen()
    
    # get username and password for ISE
    ise_user = 'readonly'
    ise_password = 'ISEisC00L'

    inventory = create_inventory(ise_user, ise_password)

    generate_yaml(inventory)


