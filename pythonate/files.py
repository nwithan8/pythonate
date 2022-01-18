import os
from enum import Enum


class FileMode(Enum):
    """
    Enum for file modes.
    """
    READ = 'r'
    WRITE = 'w',
    APPEND = 'a',
    READ_BYTES = 'rb',
    WRITE_BYTES = 'wb',
    APPEND_BYTES = 'ab',
    READ_WRITE = 'r+',
    READ_WRITE_BYTES = 'rb+',
    WRITE_READ = 'w+',
    WRITE_READ_BYTES = 'wb+',
    APPEND_READ = 'a+',
    APPEND_READ_BYTES = 'ab+'


def split_file_path(file_path) -> str:
    """
    Get path of parent directory of file
    :param file_path: File path
    :type file_path: str
    :return: Path of parent directory
    :rtype: str
    """
    return '/'.join(file_path.split('/')[:-1])


def make_path(file_path) -> None:
    """
    Make path for file if it doesn't exist
    :param file_path: Path to file
    :type file_path: str
    :return: None
    :rtype: None
    """
    working_path = split_file_path(file_path)
    if not os.path.exists(working_path):
        os.makedirs(working_path)


def write_to_file(text, filename, write_mode: FileMode = FileMode.WRITE_READ) -> None:
    """
    Write text to file
    :param text: Text to write
    :type text: str
    :param filename: File to write to
    :type filename: str
    :param write_mode: Mode to write file in
    :type write_mode: FileMode
    :return: None
    :rtype: None
    """
    make_path(filename)
    f = open(filename, write_mode.value)
    f.write(text)
    f.close()


def read_from_file(filename, read_mode: FileMode = FileMode.READ) -> str:
    """
    Read text from file
    :param filename: File to read from
    :type filename: str
    :param read_mode: Mode to read file in
    :type read_mode: FileMode
    :return: Text from file
    :rtype: str
    """
    with open(filename, read_mode.value) as f:
        text = f.read()
    return text


def backup_file(filename, suffix: str = ".bk") -> None:
    """
    Make a backup of a file
    :param filename: File to back up
    :type filename: str
    :param suffix: Suffix to add to file name
    :type suffix: str
    :return: None
    :rtype: None
    """
    copy_file(filename, f'{filename}{suffix}')


def copy_file(filename, new_filename) -> None:
    """
    Make a copy of a file
    :param filename: File to copy
    :type filename: str
    :param new_filename: Name of new file
    :type new_filename: str
    :return: None
    :rtype: None
    """
    text = read_from_file(filename)
    write_to_file(text=text, filename=new_filename)
