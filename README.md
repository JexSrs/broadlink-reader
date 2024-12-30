# Broadlink Reader

Broadlink Reader is a Python command-line interface (CLI) tool designed to interact with
Broadlink remotes to learn and capture IR/RF commands.

## Features

- Connect to Broadlink remote over a network.
- Learn and capture IR/RF commands
- Save captured commands to a specified file in JSON format
- Generate "commands.json" file that can be integrated to [SmartIR](https://github.com/smartHomeHub/SmartIR).

## Installation

To get started with Broadlink Reader, clone the repository from GitHub:

```sh
git clone https://github.com/JexSrs/broadlink-reader.git
```

and install the project:

```sh
python3 setup.py install
# or
pip install -r requirements.txt
```

## Usage

You can run the Broadlink Reader using the `main.py` script. The following options are available to customize your
interaction with the Broadlink device:

```sh
python main.py --ip 192.168.1.100 # Remote's IP address
```

### Options

| Name                  | Required | Default           | Description                                                         |
|-----------------------|----------|-------------------|---------------------------------------------------------------------|
| `-h, --help`          | No       | N/A               | Show the help message and exit.                                     |
| `--ip <ip>`           | Yes      | N/A               | Specify the IP Address of the Broadlink device.                     |
| `--port <port>`       | No       | `80`              | Specify the port of the Broadlink device.                           |
| `--timeout <timeout>` | No       | `10`              | Set the timeout (in seconds) for device connection.                 |
| `--type <type>`       | No       | `"ir"`            | Specify the capture type: `"ir"` or `"rf"`.                         |
| `--file <filename>`   | No       | `./commands.json` | Specify the output file for saving learned commands.                |
| `--read <seconds>`    | No       | `2`               | Set the time to wait (in seconds) for the user to send the command. |

The default input file, [commands.json](./commands.json), can be extended under the commands key to provide the program
with additional IR actions.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue if you have any ideas, feature
requests, or bugs.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
