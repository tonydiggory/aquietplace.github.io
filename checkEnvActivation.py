import os


def is_virtualenv_activated():
    return "VIRTUAL_ENV" in os.environ


if is_virtualenv_activated():
    print("Virtual environment is activated.")
else:
    print("Virtual environment is not activated.")
