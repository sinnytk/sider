"""Imperative shell of Sider"""
from core import Sider
from typing import Optional

AVAILABLE_COMMANDS = [
    "GET <key>",
    "SET <key> <value>",
    "UNSET <key>",
    "NUMEQUALTO <value>",
    "END",
]


def print_available_commands():
    for ac in AVAILABLE_COMMANDS:
        print(ac)
    print()


def run():
    sider = Sider()
    print_available_commands()

    while True:
        command = input().split(" ")
        if command[0] == "GET":
            _, key = command
            value: Optional[str] = sider.get(key)
            print(value if value else "NULL")
            print()

        elif command[0] == "SET":
            _, key, value = command
            sider = sider.set(key, value)
            print()

        elif command[0] == "UNSET":
            _, key = command
            sider = sider.unset(key)
            print()

        elif command[0] == "NUMEQUALTO":
            _, val = command
            count = sider.value_count(val)
            print(count)
            print()

        elif command[0] == "END":
            print()
            break

        else:
            print("error")
            print()


if __name__ == "__main__":
    run()
