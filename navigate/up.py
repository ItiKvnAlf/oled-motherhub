import display.config as config
from display.menu import display_current_menu

def navigate_up():
    """Navigate up in the menu."""
    current_state = config.data['current_state']
    selected_digit_index = config.data['selected_digit_index']
    selected_button = config.data['selected_button']
    
    if current_state == "config":
        if selected_digit_index == 0:
            if selected_button > 0:
                config.data['selected_button'] -= 1
            else:
                config.data['selected_button'] = len(config.data['system_config_options']) - 1
    elif current_state == "no_daughters" or current_state == "daughters_info" or current_state == "no_ip":
        config.data['current_state'] = "menu"
    elif current_state == "daughters_detected":
        config.data['current_state'] = "daughters_info"
    display_current_menu()