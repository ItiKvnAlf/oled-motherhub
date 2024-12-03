import display.config as config
from display.menu import display_current_menu

def navigate_left():
    """Navigate left in the menu."""
    current_state = config.data['current_state']
    selected_digit_index = config.data['selected_digit_index']
    selected_confirm_button = config.data['selected_confirm_button']
    current_index = config.data['current_index']
    daughters = config.data['dbs']
    
    if current_state == "info_mh":
        config.data['current_state'] = "menu"
    elif current_state == "info_mh_password":
        config.data['reveal_password'] = False
        config.data['current_state'] = "info_mh"
    elif current_state == "config":
        if selected_digit_index == 1:
            config.data['selected_digit_index'] = 0
    elif current_state == "system_reboot" or current_state == "system_shutdown" or current_state == "system_change_mode" or current_state == "confirm_change_mode" :
        if selected_confirm_button == 1:
            config.data['selected_confirm_button'] -= 1
    elif current_state == "daughters_detected":
        config.data['current_index'] = (current_index - 1) % len(daughters)
    display_current_menu()