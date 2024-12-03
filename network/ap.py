import subprocess
from system.config import get_env_variable
from system.constants import NMCLI_GET_CONNECTION_SSID_AND_PASSWORD, NMCLI_PASSWORD_KEY, NMCLI_SSID_KEY, WIRELESS_CONNECTION


def get_ap_ssid_and_password() -> dict:
    """
    Retrieves the SSID and password of the Access Point (AP) using nmcli.

    Returns:
        dict: A dictionary containing the SSID and password of the AP.
    """
    try:
        # Get the wireless connection name from the environment
        connection_name = get_env_variable(WIRELESS_CONNECTION)

        # Run the nmcli command to get the AP information
        command = NMCLI_GET_CONNECTION_SSID_AND_PASSWORD.format(connection_name)
        result = subprocess.run(command, shell=True, capture_output=True, text=True, check=True)

        if result.returncode != 0:
            raise RuntimeError(f"Failed to execute command '{command}'. Error: {result.stderr}")

        # Parse the output to get SSID and password
        ap_info = {}
        for line in result.stdout.splitlines():
            if ':' in line:
                key, value = line.split(':', 1)
                key = key.strip()
                value = value.strip()
                if key == NMCLI_SSID_KEY:
                    ap_info["ssid"] = value
                elif key == NMCLI_PASSWORD_KEY:
                    ap_info["password"] = value

        return ap_info

    except subprocess.CalledProcessError as e:
        print(f"Error running nmcli: {e}")
        return {}

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return {}