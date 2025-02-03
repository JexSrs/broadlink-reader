import json

from colorama import Fore


class FileGenerator:
    def __init__(self, args):
        self._required_args = {
            # Max MUST be grater than min
            "min_temp": lambda x: isinstance(x, float) and x >= 0,
            "max_temp": lambda x: isinstance(x, float) and x >= 0,
            "precision": lambda x: isinstance(x, float) and x > 0,
            "operations": lambda x: isinstance(x, list) and bool(x),
            "fan": lambda x: isinstance(x, list) and bool(x),
        }
        self._args = vars(args)
        self._init_args()
        self._file_name = self._args["name"] if '.json' in self._args["name"] else f'{self._args["name"]}.json'

    def _init_args(self):
        default_values = {
            "operations": ["cool", "heat", "dry", "fan_only", "auto"],
            "fan": ["auto", "low", "mid", "high"]
        }

        for arg, default in default_values.items():
            if not self._args.get(arg):
                self._args[arg] = default

    def validate(self):
        for arg, validate in self._required_args.items():
            value = self._args.get(arg)
            if not validate(value):
                raise ValueError(f"Invalid value for --{arg}: {value}")

        return True

    def to_json(self):
        data = {
            "manufacturer": "",
            "supportedModels": [],
            "commandsEncoding": "Base64",
            "supportedController": "Broadlink",
            "minTemperature": self._args.get("min_temp"),
            "maxTemperature": self._args.get("max_temp"),
            "precision": self._args.get("precision"),
            "operationModes": self._args.get("operations"),
            "fanModes": self._args.get("fan"),
            "commands": {
                "off": "",
                "on": ""
            }
        }

        operations = self._args.get("operations")
        fan_modes = self._args.get("fan")
        for operation in operations:
            data["commands"][operation] = {}
            for fan_mode in fan_modes:
                data["commands"][operation][fan_mode] = {}

                i = self._args.get('min_temp')
                while i < self._args.get('max_temp') + 1:
                    formatted_temp = int(i) if i.is_integer() else i
                    data["commands"][operation][fan_mode][formatted_temp] = ''
                    i += self._args.get("precision")

        # WHEN PRECISION IS INT, DONT PRINT .0 (+min, max)
        with open(self._file_name, "w") as file:
            json.dump(data, file, indent=4)
            print(Fore.GREEN + f'Successfully created "{self._file_name}"!')
