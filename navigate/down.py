import display.config as config
from display.menu import display_current_menu

def navigate_down():
    """Navigate down in the menu."""
    current_state = config.data['current_state']
    selected_digit_index = config.data['selected_digit_index']
    selected_button = config.data['selected_button']
    daughters = config.data['dbs']
    
    if current_state == "menu":
        if config.data['mh']['ip'] is not None:
            if len(daughters) > 0:
                config.data['current_state'] = "daughters_info"
            else:
                config.data['current_state'] = "no_daughters"
        else:
            config.data['current_state'] = "no_ip"
    elif current_state == "config":
        if selected_digit_index == 0:
            if selected_button < len(config.data['system_config_options']) - 1:
                config.data['selected_button'] += 1
            else:
                config.data['selected_button'] = 0
    elif current_state == "daughters_info":
        config.data['current_index'] = 0
        config.data['current_state'] = "daughters_detected"
    display_current_menu()