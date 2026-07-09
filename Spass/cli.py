import sys

AVAILABLE_OPTIONS = {
    "help": {
        "short": "h",
        "has_value": False,
        "description": "Show help message",
    },
    "hashing": {
        "short": "H",
        "has_value": False,
        "description": "Hash a password",
    },
    "make-password": {
        "short": "m",
        "has_value": False,
        "description": "Generate passwords",
    },
    "password-crack": {
        "short": "c",
        "has_value": False,
        "description": "Crack a password hash",
    },
    "password": {
        "short": "p",
        "has_value": True,
        "description": "Password to hash",
    },
    "algorithm": {
        "short": "a",
        "has_value": True,
        "description": "Hash algorithm(s)",
    },
    "file": {
        "short": "f",
        "has_value": True,
        "description": "Password list file",
    },
}

argv = sys.argv

def check_cli_args():
    if len(argv) == 1:
        return False

    parsed = {}

    i = 1
    while i < len(argv):
        arg = argv[i]

        if arg.startswith("--"):
            name = arg[2:]

        elif arg.startswith("-"):
            short = arg[1:]

            name = None
            for key, value in AVAILABLE_OPTIONS.items():
                if value["short"] == short:
                    name = key
                    break

        else:
            print(f"Unknown argument: {arg}")
            show_help()
            return True

        if name not in AVAILABLE_OPTIONS:
            print(f"Unknown option: {arg}")
            show_help()
            return True

        option = AVAILABLE_OPTIONS[name]

        if option["has_value"]:
            if i + 1 >= len(argv):
                print(f"{arg} requires a value.")
                show_help()
                return True

            parsed[name] = argv[i + 1]
            i += 2

        else:
            parsed[name] = True
            i += 1


    if "help" in parsed:
        show_help()
        return True

    if "hashing" in parsed:
        print("Run hashing...")
        print(parsed)

    elif "make-password" in parsed:
        print("Run password generator...")
        print(parsed)

    elif "password-crack" in parsed:
        print("Run cracker...")
        print(parsed)

    else:
        print("No mode selected.")
        show_help()

    return True

def show_help():
    print("Usage:")
    print("  python main.py [options]\n")

    print("Options:")

    for name, option in AVAILABLE_OPTIONS.items():
        print(
            f"  -{option['short']}, --{name:<18}"
            f"{option['description']}"
        )
