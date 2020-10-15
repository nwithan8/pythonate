import os

from cryptography.fernet import Fernet

import pythonate.files as files


# Encryption (Fernet) #
def get_raw_fernet_key(key_file):
    return files.read_from_file(key_file)


def get_fernet_key_from_file(key_file):
    """
    WARNING: New key will be made (and potentially overwrite old file) if key cannot be loaded
    """
    try:
        key = files.read_from_file(key_file)
    except:
        key = make_fernet_key()
        save_fernet_key(key, key_file)
    return Fernet(key)


def make_fernet_key():
    return Fernet.generate_key()


def save_fernet_key(key, filename):
    files.write_to_file(text=key.decode('utf-8'), filename=filename)


class Encryption:
    def __init__(self, key: Fernet = None, key_file: str = None):
        self.key = key
        self.key_file = key_file
        if not key:
            if not key_file:
                self.key = make_fernet_key()
            else:
                self.key = get_fernet_key_from_file(key_file)

    def encrypt_text(self, text):
        token = self.key.encrypt(bytes(text, encoding='utf8'))
        return token.decode('utf-8')

    def decrypt_text(self, text):
        text = self.key.decrypt(bytes(text, encoding='utf8'))
        return text.decode('utf-8')

    def encrypt_file(self, text, filename):
        text = self.encrypt_text(text)
        files.write_to_file(text=text, filename=filename)

    def encrypt_file_in_place(self, filename):
        text = files.read_from_file(filename)
        os.remove(filename)
        self.encrypt_file(text=text, filename=filename)

    def decrypt_file(self, filename):
        text = files.read_from_file(filename=filename)
        return self.decrypt_text(text)

    def decrypt_file_in_place(self, filename):
        text = self.decrypt_file(filename=filename)
        os.remove(filename)
        files.write_to_file(text=text, filename=filename)

    def _make_temporary_file(self, permanent_file_name, temporary_file_name):
        text = files.read_from_file(permanent_file_name)
        text = self.decrypt_text(text)
        files.write_to_file(text=text, filename=temporary_file_name)

    def _back_to_permanent_file(self, permanent_file_name, temporary_file_name, delete_temp_file: bool = False):
        text = files.read_from_file(temporary_file_name)
        text = self.encrypt_text(text)
        files.write_to_file(text=text, filename=permanent_file_name)
        if delete_temp_file:
            os.remove(temporary_file_name)
