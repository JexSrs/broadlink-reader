import argparse

from colorama import Fore

from utils.file_generator import FileGenerator


def main():
    parser = argparse.ArgumentParser(description='writer')
    parser.add_argument('--min-temp', type=float, default=16, help='Minimum temperature (default: 16)')
    parser.add_argument('--max-temp', type=float, default=30, help='Maximum temperature (default: 30)')
    parser.add_argument('--precision', type=float, default=1, help='Precision temperature (default: 1)')
    parser.add_argument('--operations', nargs="*", type=str, help='Operations to execute (default: all)')
    parser.add_argument('--fan', nargs="*", type=str, help='Time to wait for the user to send the command (default: 2 seconds)')
    parser.add_argument('--name', nargs='?', default='commands.json', type=str, help="Init command to generate 'commands.json' file'")

    args = parser.parse_args()
    if args.name:
        commands_args = FileGenerator(args)
        if commands_args.validate():
            try:
                commands_args.to_json()
            except Exception as e:
                print(Fore.RED + 'Failed to create commands file!')
    else:
        print(Fore.RED + '--name argument is required!')


if __name__ == '__main__':
    main()
