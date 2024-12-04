import subprocess
import time

from display import config
from system.constants import NMCLI_GET_IP4_ADDRESS
from views.loading import getting_ip_view

def get_ip_address(connection: str, is_thread: bool = False) -> dict:
    """
    Retrieves the IP address and subnet mask for the specified network interface.

    Args:
        connection (str): The name of the network connection (e.g., 'WLAN', 'ETH').

    Returns:
        dict: A dictionary containing the IP address and subnet mask with the key 'ip'.
    """
    # Display the scanning daughters view if the current state is no_ip
    if config.data['current_state'] == "no_ip" and not is_thread:
        getting_ip_view()
        time.sleep(1)

    command = NMCLI_GET_IP4_ADDRESS.format(connection)

    result = subprocess.run(command, shell=True, capture_output=True, text=True)

    if result.returncode != 0:
        print(f"Failed to execute command '{command}'. Error: {result.stderr}")

    ip, mask = None, None

    for line in result.stdout.splitlines():
        parts = line.split(':')
        ip_mask = parts[1].strip()
        ip, mask = ip_mask.split('/')

    if ip is None or mask is None:
        print(f"Failed to find IP address and mask in output: {result.stdout}")

    return {'ip': ip, 'mask': mask}