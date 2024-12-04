import time
import RPi.GPIO as GPIO # type: ignore
from network.ap import get_ap_ssid_and_password
from system.constants import BRIDGE_CONNECTION
from utils.calculate_network import calculate_network
from utils.refresh import refresh_daughters
from display.menu import display_current_menu
from network.update import update_ip
from inputs.buttons import handle_buttons, setup_buttons
from utils.screen import blank_screen, display_screen
from utils.threading import start_thread
from utils.get_ip import get_ip_address
from views.loading import initial_screen_view
import display.config as config
from display.config import disp

# GPIO Button Pins (Up, Down, Left, Right, Middle) using BCM numbering
U_BTN, D_BTN, L_BTN, R_BTN, M_BTN = 5, 6, 13, 19, 26

# Setup GPIO
setup_buttons(U_BTN, D_BTN, L_BTN, R_BTN, M_BTN)

# Display initial screen
blank_screen()
time.sleep(0.1)
initial_screen_view()
time.sleep(2)

# Main loop
try:
    # Get IP address and mask
    full_ip = get_ip_address(BRIDGE_CONNECTION)
    ip = full_ip['ip']
    mask = full_ip['mask']

    # Get SSID and password
    ap = get_ap_ssid_and_password()
    ssid = ap['ssid']
    password = ap['password']

    # Update global data
    config.data['mh'] = {
        'ip': ip,
        'ssid': ssid,
        'password': password,
        'mask': mask,
        'linked': 0
    }

    ip = config.data['mh']['ip']
    mask = config.data['mh']['mask']
    if ip and mask:
        network = calculate_network(ip, mask)
        config.data['dbs'] = refresh_daughters(network)
        config.data['mh']['linked'] = len(config.data['dbs'])

    display_current_menu()

    # Start thread
    start_thread(update_ip)

    while True:
        time.sleep(0.1)
        handle_buttons(U_BTN, D_BTN, L_BTN, R_BTN, M_BTN)

except Exception as e:
    GPIO.cleanup()
    blank_screen()
    display_screen()
    disp.poweroff()
    print("An error occurred:", e)
