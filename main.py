import argparse
import json
import os

from broadlink import Device
from colorama import Fore, init

import remote
from cli_utils import print_keys

init(autoreset=True)

data = {}
mFile = 'commands.json'
read_timeout = 2


def navigate_actions(device: Device, actions):
    current_path = []
    while True:
        if current_path:
            print(Fore.LIGHTBLUE_EX + f'\nCurrent path: {' > '.join(current_path)}')
        else:
            print(Fore.LIGHTBLUE_EX + '\nCurrent path: Home')
        print("Choose an action by index to register:")
        print(Fore.WHITE + "-1: " + ("Go back" if current_path else "Exit"))

        curr_actions = actions
        for path in current_path:
            curr_actions = curr_actions[path]
        action_keys = print_keys(curr_actions)

        try:
            choice = int(input("> "))
        except ValueError:
            print(Fore.RED + "Please enter a valid number.")
            continue

        if choice == -1:
            if current_path:
                # Go back one level
                current_path.pop()
            else:
                break
        elif 0 <= choice < len(action_keys):
            selected_action = action_keys[choice]
            if isinstance(curr_actions[selected_action], dict):
                current_path.append(selected_action)
            else:
                # If it's a leaf and read the packet
                try:
                    packet = remote.handle_action(device, read_timeout)
                except Exception as e:
                    print(Fore.RED + 'Failed to read from remote: ' + str(e))
                    continue

                # Save the packet in the nested structure
                curr_actions[selected_action] = packet

                # Save the updated data back to the output file
                with open(mFile, 'w') as file:
                    json.dump(data, file, indent=4)

                print(Fore.GREEN + f'Successfully handled "{selected_action}" and saved packet.')
        else:
            print(Fore.RED + "Invalid index. Please try again.")


def main():
    global data, mFile, read_timeout

    parser = argparse.ArgumentParser(description='Broadlink Device Command Learning')
    parser.add_argument('--ip', required=True, help='IP Address of the Broadlink device')
    parser.add_argument('--port', type=int, default=80, help='Port of the Broadlink device (default: 80)')
    parser.add_argument('--timeout', type=int, default=10, help='Timeout for device connection (default: 10)')
    parser.add_argument('--file', type=str, default='commands.json',
                        help='Output file for saving learned commands (default: commands.json)')
    parser.add_argument('--read', type=int, default=2,
                        help='Time to wait for the user to send the command (default: 2 seconds)')
    args = parser.parse_args()

    read_timeout = args.read
    mFile = args.file
    # Load existing data from the input file if it exists
    if os.path.exists(mFile):
        with open(mFile, 'r') as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                print(Fore.WHITE + "Could not read input file. Starting with empty data.")

    # Setup code
    device = remote.get_device(ip_address=args.ip, port=args.port, timeout=args.timeout)
    if not device:
        exit(1)

    # Start navigating actions
    navigate_actions(device, data.get('commands', {}))


if __name__ == '__main__':
    main()
