import os

from cryptography.fernet import Fernet

import python8.core.files as files


# Encryption (Fernet) #
def get_raw_fernet_key(key_file) -> str:
    """
    Get raw key from file
    :param key_file: File containing key
    :return: Raw key
    :rtype: str
    """
    return files.read_from_file(key_file)


def get_fernet_key_from_file(key_file) -> 'Fernet':
    """
    Get Fernet key from file
    WARNING: New key will be made (and potentially overwrite old file) if key cannot be loaded
    :param key_file: File containing key
    :return: Fernet key
    :rtype: Fernet
    """
    try:
        key = files.read_from_file(key_file)
    except:
        key = make_fernet_key()
        save_fernet_key(key, key_file)
    return Fernet(key)


def make_fernet_key() -> bytes:
    """
    Generate Fernet key
    :return: Fernet key
    :rtype: bytes
    """
    return Fernet.generate_key()


def save_fernet_key(key: bytes, filename: str) -> None:
    """
    Save Fernet key to file
    :param key: Key to save
    :type key: bytes
    :param filename: File to save key to
    :type filename: str
    :return: None
    :rtype: None
    """
    files.write_to_file(text=key.decode('utf-8'), filename=filename)


class Encryption:
    def __init__(self, key: Fernet = None, key_file: str = None):
        """
        Initialize Encryption class
        :param key: Key to use
        :type key: Fernet
        :param key_file: File containing key
        :type key_file: str
        """
        self.key = key
        self.key_file = key_file
        if not key:
            if not key_file:
                self.key = make_fernet_key()
            else:
                self.key = get_fernet_key_from_file(key_file)

    def encrypt_text(self, text: str) -> str:
        """
        Encrypt text
        :param text: Text to encrypt
        :type text: str
        :return: Encrypted text
        :rtype: str
        """
        token = self.key.encrypt(bytes(text, encoding='utf8'))
        return token.decode('utf-8')

    def decrypt_text(self, text: str) -> str:
        """
        Decrypt text
        :param text: Text to decrypt
        :type text: str
        :return: Decrypted text
        :rtype: str
        """
        text = self.key.decrypt(bytes(text, encoding='utf8'))
        return text.decode('utf-8')

    def encrypt_file(self, text: str, filename: str) -> None:
        """
        Encrypt file
        :param text: Text to encrypt
        :type text: str
        :param filename: File to encrypt
        :type filename: str
        :return: None
        :rtype: None
        """
        text = self.encrypt_text(text)
        files.write_to_file(text=text, filename=filename)

    def encrypt_file_in_place(self, filename: str) -> None:
        """
        Encrypt file in-place
        :param filename: File to encrypt
        :type filename: str
        :return: None
        :rtype: None
        """
        text = files.read_from_file(filename)
        os.remove(filename)
        self.encrypt_file(text=text, filename=filename)

    def decrypt_file(self, filename: str) -> str:
        """
        Decrypt file
        :param filename: File to decrypt
        :type filename: str
        :return: Decrypted file contents
        :rtype: str
        """
        text = files.read_from_file(filename=filename)
        return self.decrypt_text(text)

    def decrypt_file_in_place(self, filename: str) -> None:
        """
        Decrypt file in-place
        :param filename: File to decrypt
        :type filename: str
        :return: None
        :rtype: None
        """
        text = self.decrypt_file(filename=filename)
        os.remove(filename)
        files.write_to_file(text=text, filename=filename)

    def _make_temporary_file(self, permanent_file_name: str, temporary_file_name: str) -> None:
        """
        Make temporary file
        :param permanent_file_name: Permanent file name
        :type permanent_file_name: str
        :param temporary_file_name: Temporary file name
        :type temporary_file_name: str
        :return: None
        :rtype: None
        """
        text = files.read_from_file(permanent_file_name)
        text = self.decrypt_text(text)
        files.write_to_file(text=text, filename=temporary_file_name)

    def _back_to_permanent_file(self, permanent_file_name: str, temporary_file_name: str, delete_temp_file: bool = False) -> None:
        """
        Back to permanent file
        :param permanent_file_name: Permanent file name
        :type permanent_file_name: str
        :param temporary_file_name: Temporary file name
        :type temporary_file_name: str
        :param delete_temp_file: Delete temporary file
        :type delete_temp_file: bool
        :return: None
        :rtype: None
        """
        text = files.read_from_file(temporary_file_name)
        text = self.encrypt_text(text)
        files.write_to_file(text=text, filename=permanent_file_name)
        if delete_temp_file:
            os.remove(temporary_file_name)
