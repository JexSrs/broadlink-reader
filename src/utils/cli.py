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


def split_to_chunks(texts, size=5):
    chunks = [texts[i:i + size] for i in range(0, len(texts), size)]
    if len(chunks[-1]) < size:
        chunks[-1].extend([''] * (size - len(chunks[-1])))

    return chunks


def insert_pipe(text, index):
    index += 1
    if text and len(text) != 0:
        char_to_insert = "| "

        if index >= len(text):
            text = text.ljust(index, " ")

        return f'{text[:index] + Fore.MAGENTA + char_to_insert}'
    return ''


def print_keys(actions: dict, max_keys=10):
    keys = list(actions.keys())
    display_texts = []
    max_length = -1
    for index, action in enumerate(keys):
        color = get_action_color(actions, action)
        display_text = color + f"{index}: {action}"
        # Find the largest string when keys >= 10
        if len(keys) >= max_keys:
            if len(display_text) >= max_length:
                max_length = len(display_text)

            display_texts.append(display_text)
        else:
            print(display_text)

    # Print in 'table' mode
    if len(keys) >= max_keys:
        chunks = split_to_chunks(display_texts)
        for values in zip(*chunks):
            mapped_values = map(lambda x: insert_pipe(str(x), max_length), values)
            print("".join(mapped_values))

    return keys
