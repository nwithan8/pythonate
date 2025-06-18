import gnupg
import python8.files as files


# GPG Keys #
class GPG:
    """
    GPG Keys
    """

    def __init__(self, key_path):
        """
        GPG Keys
        :param key_path: Path to the GPG Keyring
        :type key_path: str
        """
        self.gpg = gnupg.GPG(homedir=key_path)

    def generate(self, key_name: str = None, user_name: str = None, email: str = None, length: int = 2048,
                 key_type: str = 'RSA', protection: bool = True) -> str:
        """
        Generate a new key
        :param key_name: Name of the key
        :type key_name: str
        :param user_name: Name of the user
        :type user_name: str
        :param email: Email of the user
        :type email: str
        :param length: Length of the key
        :type length: int
        :param key_type: Type of the key
        :type key_type: str
        :param protection: Use key protection
        :type protection: bool
        :return: Generated key
        :rtype: str
        """
        kwargs = {
            'no_protection': not protection
        }
        if key_type:
            kwargs['Key-Type'] = key_type
        if length:
            kwargs['Key-Length'] = length
        if key_name:
            kwargs['Name-Real'] = key_name
        if user_name and email:
            kwargs['Name-Email'] = f"{user_name}@{email}"
        return self.gpg.gen_key_input(**kwargs)

    def encrypt(self, data, recipients, **kwargs) -> str:
        """
        Encrypt data
        :param data: Data to encrypt
        :type data: str
        :param recipients: Recipients
        :type recipients: list
        :param kwargs: Extra keyword arguments to pass to gnupg.GPG.encrypt
        :type kwargs: dict
        :return: Encrypted data
        :rtype: str
        """
        return self.gpg.encrypt(data=data, recipients=recipients, **kwargs).data

    def encrypt_file(self, file: str, recipients: list) -> None:
        """
        Encrypt a file in-place
        :param file: File to encrypt
        :type file: str
        :param recipients: Recipients
        :type recipients: list
        :return: None
        :rtype: None
        """
        contents = files.read_from_file(file)
        encrypted_text = self.encrypt(data=contents, recipients=recipients)
        files.write_to_file(text=encrypted_text, filename=file)

    def decrypt(self, data, **kwargs) -> str:
        """
        Decrypt data
        :param data: Data to decrypt
        :type data: str
        :param kwargs: Extra keyword arguments to pass to gnupg.GPG.decrypt
        :type kwargs: dict
        :return: Decrypted data
        :rtype: str
        """
        return self.gpg.decrypt(message=data, **kwargs).data

    def decrypt_file(self, file: str, always_trust=False, passphrase=None) -> str:
        """
        Decrypt a file in-place
        :param file: File to decrypt
        :type file: str
        :param always_trust: Always trust the key
        :type always_trust: bool
        :param passphrase: Passphrase to use
        :type passphrase: str
        :return: Decrypted data
        :rtype: str
        """
        return self.gpg.decrypt_file(filename=file, always_trust=always_trust, passphrase=passphrase, output=file).data

    def sign(self, data, **kwargs) -> 'gnupg.Sign':
        """
        Sign data
        :param data: Data to sign
        :type data: str
        :param kwargs: Extra keyword arguments to pass to gnupg.GPG.sign
        :type kwargs: dict
        :return: Signed data
        :rtype: gnupg.Sign
        """
        return self.gpg.sign(data=data, **kwargs)

    def verify(self, data) -> 'gnupg.Verify':
        """
        Verify data
        :param data: Data to verify
        :type data: str
        :return: Data verification
        :rtype: gnupg.Verify
        """
        return self.gpg.verify(data=data)

    def list_keys(self, secret=False) -> 'gnupg.ListKeys':
        """
        List keys
        :param secret: List keys
        :type secret: bool
        :return: keys
        :rtype: gnupg.ListKeys
        """
        return self.gpg.list_keys(secret=secret)

    def import_key(self, key_data) -> None:
        """
        Import a key
        :param key_data: Key data
        :type key_data: str
        :return: None
        :rtype: None
        """
        self.gpg.import_keys(key_data=key_data)

    def export_key(self, key_id: str, export_secrets: bool = False, export_subkeys: bool = False) -> None:
        """
        Export a key
        :param key_id: Key ID
        :type key_id: str
        :param export_secrets: Export secret keys
        :type export_secrets: bool
        :param export_subkeys: Export subkeys
        :type export_subkeys: bool
        :return: None
        :rtype: None
        """
        self.gpg.export_keys(keyids=key_id, secret=export_secrets, subkeys=export_subkeys)

    def delete_keys(self, fingerprints: list, delete_secret: bool = False, delete_subkeys: bool = False) -> None:
        """
        Delete keys
        :param fingerprints: Fingerprints
        :type fingerprints: list
        :param delete_secret: Delete secret keys
        :type delete_secret: bool
        :param delete_subkeys: Delete subkeys
        :type delete_subkeys: bool
        :return: None
        :rtype: None
        """
        self.gpg.delete_keys(fingerprints=fingerprints, secret=delete_secret, subkeys=delete_subkeys)
