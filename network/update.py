import display.config as config
import time
from system.config import get_env_variable
from system.constants import WIRELESS_CONNECTION
from utils.get_ip import get_ip_address

def update_ip():
    """
    Update the IP address of the Ethernet interface in the global data.
    """
    # Continuously check for changes in the ethernet IP address
    while True:
        current_ip = get_ip_address(get_env_variable(WIRELESS_CONNECTION))['ip']
        current_mask = get_ip_address(get_env_variable(WIRELESS_CONNECTION))['mask']
        # Update IP in db if it has changed
        if config.data['mh']["ip"] != current_ip:
            config.data['mh']["ip"] = current_ip

        # Update mask in db if it has changed
        if config.data['mh']["mask"] != current_mask:
            config.data['mh']["mask"] = current_mask
        time.sleep(10)  # Check every 10 seconds for changes
        
