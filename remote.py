import base64
from time import sleep

import broadlink
from broadlink import Device
from colorama import Fore


def get_device(ip_address: str, port: int, timeout: int) -> Device | None:
    print(f'Connecting to device using IP address: "{ip_address}"...')
    try:
        device = broadlink.hello(ip_address=ip_address, port=port, timeout=timeout)
        print(f'Found device "{device.manufacturer} {device.model} ({device.name})". Attempting to authenticate...')
        device.auth()
        return device
    except Exception as e:
        print(Fore.RED + f'Could not connect to device using IP address: "{ip_address}", Reason: {e}.')
        return None


def read_action(device: Device, type: str, read_timeout: int) -> str:
    if type == 'ir':
        print('Point to the device and short press the button to be captured...')
        device.enter_learning()

        # Wait for the user to point the remote
        sleep(read_timeout)

        print('Retrieving packets...')
        packet = device.check_data()
    elif type == 'rf':
        print('Point to the device and long press the button to be captured (step 1)...')
        device.sweep_frequency()

        # Wait for the user to point the remote
        sleep(read_timeout)

        ok = device.check_frequency()
        if not ok:
            raise IOError('Failed to acquire frequency')

        print('Point again to the device and short press the button to be captured (step 2)...')
        device.find_rf_packet()

        # Wait for the user to point the remote
        sleep(read_timeout)

        packet = device.check_data()
    else:
        raise TypeError('Unknown action type')

    # Convert bytes to Base64
    base64_encoded = base64.b64encode(packet)
    base64_string = base64_encoded.decode('utf-8')
    return base64_string
