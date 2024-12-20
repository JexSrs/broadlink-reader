# Broadlink Reader

Broadlink Reader is a Python command-line interface (CLI) tool designed to interact with
Broadlink remotes to learn and capturing IR commands.
This tool allows users to connect to a Broadlink device, learn commands, and save
them to a file for future use.

## Features

- Connect to Broadlink remote over a network.
- Learn and capture IR commands
- Save captured commands to a specified file in JSON format (can be passed to [SmartIR](https://github.com/smartHomeHub/SmartIR) later.

## Installation

To get started with Broadlink Reader, clone the repository from GitHub:

```
git clone https://github.com/JexSrs/broadlink-reader.git
cd broadlink-reader
```

## Usage

You can run the Broadlink Reader using the `main.py` script. The following options are available to customize your
interaction with the Broadlink device:

```
python main.py --ip 192.168.1.100 # Remote's IP address
```

Options:

- `-h, --help`: Show the help message and exit.
- `--ip <ip>`: Specify the IP Address of the Broadlink device (required).
- `--port <port`: Specify the port of the Broadlink device (default: 80).
- `--timeout <timeout>`: Set the timeout for device connection in seconds (default: 10).
- `--file <filename>`: Specify the output file for saving learned commands (default: commands.json).
- `--read <seconds>`: Set the time to wait for the user to send the command in seconds (default: 2).

The default input file, [commands.json](./commands.json), can be extended under the commands key to provide the program with additional IR actions.   

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue if you have any ideas, feature
requests, or bugs.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
