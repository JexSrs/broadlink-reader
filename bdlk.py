from time import sleep
from broadlink import Device

import broadlink
import base64

from colorama import Fore


def get_device(ip_address: str, port: int, timeout: int) -> Device | None:
    print(f'Searching for device in {ip_address}...')
    try:
        device = broadlink.hello(ip_address=ip_address, port=port, timeout=timeout)
        print(f'Found device "{device.manufacturer} {device.model} ({device.name})". Attempting to authenticate...')
        device.auth()
        return device
    except Exception as e:
        print(Fore.RED + f'Could not find device in {ip_address}.')
        return None


def handle_action(device: Device, read_timeout: int):
    print('Reading...')
    device.enter_learning()

    # Wait for the user to point the remote
    sleep(read_timeout)

    print('Getting packets...')
    packet = device.check_data()

    # Convert bytes to Base64
    base64_encoded = base64.b64encode(packet)
    base64_string = base64_encoded.decode('utf-8')
    return base64_string
