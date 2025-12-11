import hashlib
import hmac
import secrets


def _bytes_to_hash(_input: bytes) -> str:
    """
    Hash a string with SHA256.
    :param _input: string to hash.
    :return: hashed string.
    """
    return hashlib.sha256(_input).hexdigest()


def _string_to_hash(_input: str) -> str:
    """
    Hash a string with SHA256.
    :param _input: string to hash.
    :return: hashed string.
    """
    return _bytes_to_hash(_input.encode('utf-8'))


def generate_hash(secret: str) -> str:
    """
    Generate a hash from a string.
    :param secret: string to hash.
    :return: hashed string.
    """
    return _string_to_hash(secret)


def hash_matches(_input: str, hashed: str) -> bool:
    """
    Check if a string, when hashed, matches another string.
    :param _input: String to hash and compare to the hashed string.
    :param hashed: Hashed string to compare against.
    :return: True if the string, when hashed, matches the hashed string, False otherwise.
    """
    to_match = _string_to_hash(_input)
    return hmac.compare_digest(to_match, hashed)


def generate_random_alphanumeric_string() -> str:
    """
    Generate a random alphanumeric string.
    :return: random alphanumeric string.
    """
    return secrets.token_urlsafe(24)
