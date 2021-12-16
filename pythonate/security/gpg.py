import gnupg


# GPG Keys #
class GPG:
    def __init__(self, key_path):
        self.gpg = gnupg.GPG(gnupghome=key_path)

    def generate(self, key_name: str = None, user_name: str = None, email: str = None, length: int = 2048, key_type: str = 'RSA', protection: bool = True):
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

    def encrypt(self, data, recipients, **kwargs):
        return self.gpg.encrypt(data=data, recipients=recipients, **kwargs)

    def encrypt_file(self, file, recipients: list, sign=None, always_trust=False, passphrase=None, armor=True, output=None, symmetric=False, extra_args=None):
        return self.gpg.encrypt_file(file=file, recipients=recipients, sign=sign, always_trust=always_trust, passphrase=passphrase, armor=armor, output=output, symmetric=symmetric, extra_args=extra_args)

    def decrypt(self, data, **kwargs):
        return self.gpg.decrypt(message=data, **kwargs)

    def decrypt_file(self, file, always_trust=False, passphrase=None, output=None, extra_args=None):
        return self.gpg.decrypt_file(file=file, always_trust=always_trust, passphrase=passphrase, output=output, extra_args=extra_args)

    def sign(self, data, **kwargs):
        return self.gpg.sign(message=data, **kwargs)

    def verify(self, data, **kwargs):
        return self.gpg.verify(data=data, **kwargs)

    def list_keys(self, secret=False, keys=None, sigs=False):
        return self.gpg.list_keys(secret=secret, keys=keys, sigs=sigs)

    def scan_keys(self, filename: str):
        return self.gpg.scan_keys(filename=filename)

    def import_keys(self, key_data, extra_args=None, passphrase=None):
        return self.gpg.import_keys(key_data=key_data, extra_args=extra_args, passphrase=passphrase)

    def export_keys(self, key_ids: list, secret=False, armor=True, minimal=False, passphrase=None, expect_passphrase=True):
        return self.gpg.export_keys(keyids=key_ids, secret=secret, armor=armor, minimal=minimal, passphrase=passphrase, expect_passphrase=expect_passphrase)

    def send_keys(self, keyserver='pgp.mit.edu', *key_ids):
        return self.gpg.send_keys(keyserver=keyserver, *key_ids)

    def delete_keys(self, fingerprints: list, secret=False, passphrase=None, expect_passphrase=True):
        return self.gpg.delete_keys(fingerprints=fingerprints, secret=secret, passphrase=passphrase, expect_passphrase=expect_passphrase)

    def search_for_key(self, query, keyserver='pgp.mit.edu'):
        return self.gpg.search_keys(query=query, keyserver=keyserver)





