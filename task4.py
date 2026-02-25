import sys
from functools import wraps
from typing import Dict, Callable, Any

from colorama import Fore, init

from exception_utils import InvalidCommandException, CommandExecutionException

init(autoreset=True)
GREETING_TEXT = "Hello, how can I help you today?"

CommandMap = Dict[str, Callable[..., None]]

def handle_input_error(rethrow_exception: bool = False):
    def wrapper(func: Callable) -> Callable:
        @wraps(func)
        def inner(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except (InvalidCommandException, CommandExecutionException) as e:
                if rethrow_exception:
                    raise
                print(Fore.RED + str(e))
                main()
        return inner
    return wrapper


@handle_input_error()
def main():
    phone_book: Dict[str, str] = {}

    commands: CommandMap = {
        "hello": lambda: print(GREETING_TEXT),
        "add": lambda *args: upsert_contact(phone_book, *args),
        "change": lambda *args: upsert_contact(phone_book, *args),
        "show": lambda *args: show_phone(phone_book, *args),
        "all": lambda: show_all(phone_book),
        "close": lambda: handle_exit(),
        "exit": lambda: handle_exit(),
    }

    while True:
        parts = input("Enter your command: ").split()
        if not parts:
            raise InvalidCommandException

        command_name = parts[0].lower()
        arguments = parts[1:]

        handler = commands.get(command_name)
        if handler is None:
            raise InvalidCommandException()

        try:
            handler(*arguments)
        except TypeError:
            raise InvalidCommandException("Missing arguments for this command.")
        except (IndexError, ValueError) as e:
            raise InvalidCommandException(f"Invalid arguments: {e}")


@handle_input_error()
def upsert_contact(phone_book: Dict[str, str], name: str, phone_number: str) -> None:
    try:
        phone_book[name] = phone_number
        print(f"{Fore.GREEN}{name} has been successfully added to the phone book.")
    except KeyError:
        raise CommandExecutionException(message="Contact does not exist.", command_name=upsert_contact.__name__)


@handle_input_error()
def show_phone(phone_book: Dict[str, str], name: str) -> None:
    phone_number = phone_book.get(name)
    if phone_number is not None:
        print(f"{phone_number}")
    else:
        raise CommandExecutionException(message="Such phone number does not exist.", command_name=show_phone.__name__)


@handle_input_error()
def show_all(phone_book: Dict[str, str]) -> None:
    if not phone_book:
        raise CommandExecutionException(message="No contacts saved.", command_name=show_all.__name__)
    for name, number in phone_book.items():
        print(f"Name: {name}; Number: {number}")


def handle_exit() -> None:
    print("Good bye!")
    sys.exit()


if __name__ == "__main__":
    main()