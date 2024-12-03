import time
import RPi.GPIO as GPIO # type: ignore
from network.ap import get_ap_ssid_and_password
from system.config import get_env_variable, load_env
from system.constants import WIRELESS_CONNECTION
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

# Load environment variables
load_env()

# GPIO Button Pins (Up, Down, Left, Right, Middle) using BCM numbering
U_BTN, D_BTN, L_BTN, R_BTN, M_BTN = 5, 6, 13, 19, 26

# Setup GPIO
setup_buttons(U_BTN, D_BTN, L_BTN, R_BTN, M_BTN)

# Update global data
config.data['mh'] = {
    'ip': get_ip_address(get_env_variable(WIRELESS_CONNECTION))['ip'],
    'ssid': get_ap_ssid_and_password()['ssid'],
    'password': get_ap_ssid_and_password()['password'],
    'mask': get_ip_address(get_env_variable(WIRELESS_CONNECTION))['mask'],
    'linked': 0
}

# Display initial screen
blank_screen()
time.sleep(0.1)
initial_screen_view()
time.sleep(2)

# # Main loop
# try:
#     config.data['dbs'] = refresh_daughters()
#     # Update global data
#     config.data['mh'] = {
#         'ip': get_ip_address("eth0"),
#         'name': get_hostname(),
#         'mask': get_mask("eth0"),
#     }
#     display_current_menu()

#     # Start threads
#     start_thread(update_ip)

#     while True:
#         time.sleep(0.1)
#         handle_buttons(U_BTN, D_BTN, L_BTN, R_BTN, M_BTN)

# except Exception as e:
#     GPIO.cleanup()
#     blank_screen()
#     display_screen()
#     disp.poweroff()
#     print("An error occurred:", e)

ip = config.data['mh']['ip']
mask = config.data['mh']['mask']
network = calculate_network(ip, mask)
config.data['dbs'] = refresh_daughters(network)
display_current_menu()

# Start threads
start_thread(update_ip)

while True:
    time.sleep(0.1)
    handle_buttons(U_BTN, D_BTN, L_BTN, R_BTN, M_BTN)
