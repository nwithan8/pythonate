import os
from typing import List, Union, Tuple


# Files #
def split_file_path(file_path):
    return '/'.join(file_path.split('/')[:-1])


def make_path(file_path):
    working_path = split_file_path(file_path)
    if not os.path.exists(working_path):
        os.makedirs(working_path)


def write_to_file(text, filename, write_mode: str = "w+"):
    make_path(filename)
    f = open(filename, write_mode)
    f.write(text)
    f.close()


def read_from_file(filename, read_mode: str = 'r'):
    with open(filename, read_mode) as f:
        text = f.read()
    return text


def backup_file(filename, suffix: str = ".bk"):
    copy_file(filename, f'{filename}{suffix}')


def copy_file(filename, new_filename):
    text = read_from_file(filename)
    write_to_file(text=text, filename=new_filename)
