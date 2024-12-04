import time
import display.config as config
from display.icons import draw_icons_bottom_right
from utils.screen import blank_screen, display_screen
from views.available_networks import daughters_detected_view, daughters_info_view, ip_found_view, no_daughters_view, no_ip_view
from views.confirm import confirm_view
from views.devices_info import mother_info_password_view, mother_info_view, mother_info_view
from views.main_menu import menu_view
from views.system_config import system_config_view

def display_current_menu():
    """
    Display the current menu on the screen.
    """
    blank_screen()
    draw_icons_bottom_right()

    current_state = config.data['current_state']
    if current_state == "menu":
        menu_view()
    elif current_state == "info_mh":
        time.sleep(0.1)
        mother_info_view()
    elif current_state == "info_mh_password":
        mother_info_password_view()
    elif current_state == "config":
        time.sleep(0.1)
        system_config_view(config.data['system_config_options'])
    elif current_state == "system_reboot" or current_state == "system_shutdown" or current_state == "system_change_mode" or current_state == "confirm_change_mode":
        confirm_view()
    elif current_state == "daughters_info":
        daughters_info_view()
    elif current_state == "daughters_detected":
        time.sleep(0.1)
        daughters_detected_view()
    elif current_state == "no_daughters":
        no_daughters_view()
    elif current_state == "no_ip":
        no_ip_view()
    elif current_state == "ip_found":
        ip_found_view()

    if current_state != "info_mh":
        display_screen()
