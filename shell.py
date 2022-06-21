"""Imperative shell of Sider"""
from core import Sider
from typing import Optional

AVAILABLE_COMMANDS = [
    "GET <key>",
    "SET <key> <value>",
    "UNSET <key>",
    "NUMEQUALTO <value>",
    "END",
    "BEGIN",
    "COMMIT",
    "ROLLBACK",
]


def print_available_commands():
    for ac in AVAILABLE_COMMANDS:
        print(ac)
    print()


def handle_input(current_sider: Sider) -> Sider:
    """Handles user input to manipulate Sider state.

    Args:
        current_sider (Sider): Currently used state of Sider
    Returns:
        Sider: a new instance of sider with updates (if there were any)
    """

    sider = Sider.from_sider(current_sider)
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

        elif command[0] == "BEGIN":
            # NOTE: this is kinda dangerous/sweet. can reach a big depth if transactions are opened inside transactions
            # https://en.wikipedia.org/wiki/Nested_transaction
            print()
            sider = handle_input(sider)  # recursively handle transactions

        elif command[0] == "COMMIT":
            print()
            return sider  # return the new updated store

        elif command[0] == "ROLLBACK":
            print()
            return current_sider  # return the old store without any updates

        else:
            print("error")
            print()

    return sider


def run():
    sider = Sider()  # empty instance of Sider
    print_available_commands()

    sider = handle_input(sider)  # take input from user and update instance

    # now we do not do anything with the copy of sider
    # in a real scenario, this would be persisted.


if __name__ == "__main__":
    run()
