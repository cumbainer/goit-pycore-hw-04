from colorama import Fore


class GenericCommandException(Exception):
    def __init__(self, message: str):
        super().__init__(message)
        self.message = message


class InvalidCommandException(GenericCommandException):
    def __init__(self, message: str="Invalid Command.") -> None:
        super().__init__(message)
        self.message = message

class CommandExecutionException(GenericCommandException):
    def __init__(
        self,
        command_name: str="unknown",
        message: str = "Something unexpected happened while executing command."
    ) -> None:
        self.command_name = command_name
        self.message = message
        super().__init__(f"{message} (command: {command_name})")