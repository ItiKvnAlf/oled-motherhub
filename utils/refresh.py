import re
import subprocess
import time
import display.config as config
from system.constants import MAC_PREFIX_FOR_RASPBERRY, NMAP_IP_PATTERN, NMAP_MAC_PATTERN, NMAP_SCAN
from views.loading import scanning_daughters_view

def refresh_daughters(network: str) -> list:
    """
    Runs nmap to discover devices on the specified network and retrieves their IP and MAC addresses,
    filtering only those whose MAC addresses start with the specified Raspberry Pi prefix.

    Args:
        network (str): The network address in CIDR format (e.g., '192.168.1.0/24').

    Returns:
        list: A list of dictionaries with the IP and MAC addresses of the discovered devices
              that match the Raspberry Pi MAC prefix.
              Example: [{"ip": "192.168.1.1", "mac": "B8:27:EB:AA:BB:CC"}, ...]
    """
    # Display the scanning daughters view if the current state is daughters_info or no_daughters
    if config.data['current_state'] == "daughters_info" or config.data['current_state'] == "no_daughters":
        scanning_daughters_view()
        time.sleep(1)
        
    try:
        # Run the nmap command to perform a ping scan on the specified network
        result = subprocess.run(
            NMAP_SCAN.format(network),
            shell=True,
            capture_output=True,
            text=True,
            check=True
        )

        devices = []  # List to store discovered devices matching the MAC prefix
        lines = result.stdout.splitlines()  # Split output into lines for processing

        # Compile regular expressions to match IP and MAC address patterns
        ip_pattern = re.compile(NMAP_IP_PATTERN)
        mac_pattern = re.compile(NMAP_MAC_PATTERN)

        current_ip = None  # Variable to hold the current IP address being processed

        for line in lines:
            # Look for IP address lines without parentheses (to exclude the scanning device's IP)
            if "(" not in line:
                ip_match = ip_pattern.search(line)
                if ip_match:
                    current_ip = ip_match.group(1)  # Extract the IP address

            # Look for MAC address lines following an IP address
            mac_match = mac_pattern.search(line)
            if mac_match and current_ip:
                mac = mac_match.group(1)  # Extract the MAC address
                #Check if the MAC address starts with the Raspberry Pi prefix
                if mac.startswith(MAC_PREFIX_FOR_RASPBERRY):
                    devices.append({"ip": current_ip, "mac": mac})  # Store the IP-MAC pair
                current_ip = None  # Reset the current IP after storing or discarding

        return devices

    except subprocess.CalledProcessError as e:
        # Handle errors that occur during the execution of the nmap command
        print(f"Error running nmap: {e}")
        return []