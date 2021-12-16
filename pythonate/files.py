import os
from enum import Enum


class FileMode(Enum):
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


def split_file_path(file_path):
    return '/'.join(file_path.split('/')[:-1])


def make_path(file_path):
    working_path = split_file_path(file_path)
    if not os.path.exists(working_path):
        os.makedirs(working_path)


def write_to_file(text, filename, write_mode: FileMode = FileMode.WRITE_READ):
    make_path(filename)
    f = open(filename, write_mode.value)
    f.write(text)
    f.close()


def read_from_file(filename, read_mode: FileMode = FileMode.READ):
    with open(filename, read_mode.value) as f:
        text = f.read()
    return text


def backup_file(filename, suffix: str = ".bk"):
    copy_file(filename, f'{filename}{suffix}')


def copy_file(filename, new_filename):
    text = read_from_file(filename)
    write_to_file(text=text, filename=new_filename)
