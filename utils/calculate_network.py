import ipaddress

def calculate_network(ip: str, mask: str) -> str:
    """
    Calculates the network address given an IP address and a subnet mask.

    Args:
        ip (str): The IP address in the format 'x.x.x.x'.
        mask (str): The subnet mask in the format 'x.x.x.x'.

    Returns:
        str: The network address in the format 'x.x.x.x/mask'.
    """
    try:
        # Create an IP network object using the IP address and mask
        network = ipaddress.IPv4Network(f'{ip}/{mask}', strict=False)
        return f"{network.network_address}/{mask}"
    except ValueError as e:
        # Return an empty string if there's an issue with the calculation
        print(f"Error in network calculation: {e}")
        return ""