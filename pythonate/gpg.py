import pgp


# GPG Keys #
class GPG:
    def __init__(self, key_server: str = "hkp://pgp.key-server.io/"):
        self.server = key_server

    def search(self, search_string: str):
        return pgp.keyserver.get_keyserver(self.server).search(search_string)
