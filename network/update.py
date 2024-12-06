import display.config as config
import time
from network.ap import get_ap_ssid_and_password
from system.constants import BRIDGE_CONNECTION
from utils.get_ip import get_ip_address

def update_ip():
    """
    Update the IP address of the Ethernet interface in the global data.
    """
    # Continuously check for changes in the ethernet IP address
    while True:
        full_ip = get_ip_address(BRIDGE_CONNECTION, True)
        current_ip = full_ip['ip']
        current_mask = full_ip['mask']

        # Update IP in db if it has changed
        if config.data['mh']["ip"] != current_ip:
            config.data['mh']["ip"] = current_ip

        # Update mask in db if it has changed
        if config.data['mh']["mask"] != current_mask:
            config.data['mh']["mask"] = current_mask
        time.sleep(10)  # Check every 10 seconds for changes
        
def update_ssid_and_password():
    """
    Update the SSID and password of the AP in the global data.
    """
    # Continuously check for changes in the AP SSID
    while True:
        item = get_ap_ssid_and_password()
        current_ssid = item['ssid']
        current_password = item['password']

        # Update SSID in db if it has changed
        if config.data['mh']["ssid"] != current_ssid:
            config.data['mh']["ssid"] = current_ssid
        if config.data['mh']["password"] != current_password:
            config.data['mh']["password"] = current_password
        time.sleep(10)  # Check every 10 seconds for changes
