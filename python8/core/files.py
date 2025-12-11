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


def save_file(file, folder: str, file_name: str = None) -> str:
    """
    Save a file to a specified folder with an optional file name.
    :param file: The file object to be saved.
    :param folder: The folder where the file will be saved.
    :param file_name: The name of the file. If None, a random name will be used.
    :return: The path to the saved file.
    """
    # Ensure the directory exists
    os.makedirs(folder, exist_ok=True)

    # If no file name is provided, generate a random name
    file_name = file_name or os.urandom(16).hex()

    # Create the full path for the file
    file_path = os.path.join(folder, file_name)

    # Save the file
    with open(file_path, 'wb') as f:
        f.write(file.read())

    return file_path


def delete_file(file_path: str) -> None:
    """
    Delete a file if it exists.
    :param file_path: The path to the file to be deleted.
    """
    if os.path.exists(file_path):
        try:
            os.remove(file_path)
        except Exception as e:
            print(f"Failed to delete file {file_path}: {str(e)}")
    else:
        print(f"File {file_path} does not exist, nothing to delete.")
