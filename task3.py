import pathlib
from plistlib import InvalidFileException

from colorama import Fore

SUFFIX_COLOR = Fore.RED
DIR_COLOR = Fore.BLUE
STEM_COLOR = Fore.YELLOW
FILE_INDENT = "  "


def print_directory_contents(path: str, indent="") -> None:
    directory = pathlib.Path(path)
    if not directory.exists() or not directory.is_dir():
        print(Fore.RED + f"{directory} is not a valid directory.")
        return

    for file in sorted(directory.iterdir()):
        if file.is_dir():
            print(DIR_COLOR, file.name)
            new_indent = indent + FILE_INDENT
            print_directory_contents(str(file), new_indent)
        elif file.is_file():
            colorized_file = get_colorized_file(file, indent)
            print(colorized_file)


def get_colorized_file(file: pathlib.Path, indent: str) -> str:
    if not file.is_file():
        raise InvalidFileException(f"{file} is not a valid file.")
    return STEM_COLOR + indent + file.stem + SUFFIX_COLOR + file.suffix