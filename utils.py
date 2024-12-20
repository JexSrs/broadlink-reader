from colorama import Fore


def get_action_color(current_actions: dict, action: str):
    """Check if the action exists, is a JSON object, and return the appropriate color based on its contents."""
    if action in current_actions:
        value = current_actions[action]

        # If the item is not an object and is populated
        if not isinstance(value, dict):
            return Fore.GREEN if value else Fore.WHITE

        # If the item is an object
        populated_count = 0
        total_count = len(value)

        for key, v in value.items():
            if isinstance(v, dict):
                # If the value is a dictionary, check it recursively
                nested_color = get_action_color(v, next(iter(v)))
                if nested_color == Fore.GREEN:
                    populated_count += 1
            elif isinstance(v, str) and v:
                populated_count += 1

        if populated_count == 0:
            return Fore.WHITE
        elif populated_count == total_count:
            return Fore.GREEN
        else:
            return Fore.YELLOW

    # If the action is not registered or is empty
    return Fore.WHITE


def print_keys(actions: dict):
    keys = list(actions.keys())
    for index, action in enumerate(keys):
        color = get_action_color(actions, action)
        print(color + f"{index}: {action}{' (select to expand)' if isinstance(actions[action], dict) else ''}")

    return keys
