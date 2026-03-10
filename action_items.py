import re

def extract_action_items(text):

    patterns = [
        r"(\w+)\s+will\s+([^.]+)",
        r"(\w+)\s+shall\s+([^.]+)",
        r"(\w+)\s+to\s+([^.]+)"
    ]

    actions = []

    for pattern in patterns:

        matches = re.findall(pattern, text, re.IGNORECASE)

        for match in matches:

            person = match[0]
            task = match[1]

            actions.append(f"{person} -> {task}")

    return actions