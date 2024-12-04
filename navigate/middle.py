import time
import display.config as config
from display.menu import display_current_menu

from system.constants import BRIDGE_CONNECTION
from utils.calculate_network import calculate_network
from utils.get_ip import get_ip_address
from utils.refresh import refresh_daughters
from system.actions import change_mode, reboot_system, shutdown_system

def push_button():
    """Handle button press."""
    current_state = config.data['current_state']
    selected_button = config.data['selected_button']
    selected_confirm_button = config.data['selected_confirm_button']
    selected_digit_index = config.data['selected_digit_index']
    
    if current_state == "menu":
        # Initialize the selected index for the digit (start with the first digit selected)
        config.data['selected_digit_index'] = 0
        config.data['current_state'] = "config"
    elif current_state == "info_mh_password":
        config.data['reveal_password'] = not config.data['reveal_password']
    elif current_state == "config":
        if selected_digit_index == 0:
            if selected_button == 0:
                config.data['current_state'] = "system_reboot"
            elif selected_button == 1:  
                config.data['current_state'] = "system_shutdown"
            elif selected_button == 2:
                config.data['current_state'] = "system_change_mode"
        elif selected_digit_index == 1:
            config.data['current_state'] = "menu"
        config.data['selected_button'] = 0
        config.data['selected_digit_index'] = 0
    elif current_state == "system_reboot":
        if selected_confirm_button == 1:
            reboot_system()
        elif selected_confirm_button == 0:
            config.data['current_state'] = "config"
            config.data['selected_button'] = 0
    elif current_state == "system_shutdown":
        if selected_confirm_button == 1:
            shutdown_system()   
        elif selected_confirm_button == 0:
            config.data['current_state'] = "config"
            config.data['selected_button'] = 1
    elif current_state == "system_change_mode":
        if selected_confirm_button == 1:
            config.data['current_state'] = "confirm_change_mode"
            config.data['selected_confirm_button'] = 0
        elif selected_confirm_button == 0:
            config.data['current_state'] = "config"
            config.data['selected_button'] = 2
    elif current_state == "confirm_change_mode":
        if selected_confirm_button == 1:
            change_mode()
        elif selected_confirm_button == 0:
            config.data['selected_confirm_button'] = 0
            config.data['current_state'] = "system_change_mode"
    elif current_state == "daughters_info" or current_state == "no_daughters":
        ip = config.data['mh']['ip']
        mask = config.data['mh']['mask']
        network = calculate_network(ip, mask)
        config.data['dbs'] = refresh_daughters(network)
        config.data['mh']['linked'] = len(config.data['dbs'])
    elif current_state == "no_ip":
        full_ip = get_ip_address(BRIDGE_CONNECTION)
        ip= full_ip['ip']
        mask = full_ip['mask']
        config.data['mh']["ip"] = ip
        config.data['mh']["mask"] = mask
        if config.data['mh']['ip'] and config.data['mh']['mask']:
            config.data['current_state'] = "ip_found"
    elif current_state == "ip_found":
        if config.data['mh']['linked'] > 0:
                config.data['current_state'] = "daughters_info"
        else:
            config.data['current_state'] = "no_daughters"
    display_current_menu()