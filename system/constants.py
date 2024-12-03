ETHERNET_CONNECTION = 'ETHERNET_CONNECTION'
WIRELESS_CONNECTION = 'WIRELESS_CONNECTION'

DEVICE_MODE_FILE_PATH = 'DEVICE_MODE_FILE_PATH'

REBOOT_SYSTEM = "sudo reboot"
SHUTDOWN_SYSTEM = "sudo shutdown now"

NMCLI_GET_IP4_ADDRESS = "nmcli -f IP4.ADDRESS connection show {}"
NMCLI_GET_CONNECTION_SSID_AND_PASSWORD = "nmcli connection show {} --show-secrets"

NMCLI_SSID_KEY = "802-11-wireless.ssid"
NMCLI_PASSWORD_KEY = "802-11-wireless-security.psk"

NMAP_SCAN = "sudo nmap -sn {}"

NMAP_IP_PATTERN = r"Nmap scan report for (\d{1,3}(?:\.\d{1,3}){3})"
NMAP_MAC_PATTERN = r"MAC Address: ([0-9A-F:]+)"

MAC_PREFIX_FOR_RASPBERRY = "B8:27:EB"

DAUGHTERBOX_WEBSERVER_PORT = ":81"
