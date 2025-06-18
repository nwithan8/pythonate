import enum
from functools import wraps

from flask import (
    request,
    make_response,
    jsonify,
)

from python8.rest_api.database.base_database import BaseDatabase
from python8.rest_api.repositories.secrets import SecretRepository
from python8.utilities.crypto import hash_matches, generate_hash, generate_random_alphanumeric_string


class AuthenticationType(enum.Enum):
    """
    Authentication type.
    """
    ADMIN = "admin"
    USER = "user"


def _get_admin_api_key(database: BaseDatabase) -> None | str:
    """
    Get the admin API key from the database.

    :return: The admin API key.
    """
    return SecretRepository(database=database).get_admin_api_key_from_database()


def _generate_and_save_admin_api_key(database: BaseDatabase) -> str | None:
    """
    Generate an admin API key and save it to the database.

    :return: True if the API key was saved to the database, False otherwise.
    """
    api_key: str = generate_random_alphanumeric_string()

    hashed_api_key: str = generate_hash(secret=api_key)
    if not SecretRepository(database=database).add_admin_api_key_to_database(api_key=hashed_api_key):
        print("Could not save API key to database")
        return None

    return api_key


def setup_authentication(database: BaseDatabase) -> tuple[None | str, bool]:
    """
    Setup authentication.

    :return: The admin API key and `True` if it was generated, `None` and `False` otherwise.
    """
    if not _get_admin_api_key(database=database):
        return _generate_and_save_admin_api_key(database=database), True
    return None, False


def require_authentication(database: BaseDatabase, auth_type: AuthenticationType = AuthenticationType.ADMIN):
    """
    Require authentication for a function.
    """

    def check_authentication(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            """
            Check authentication (API key in as Bear token in headers)
            """
            headers: dict = dict(request.headers)

            api_key = headers.get("Authorization")
            if api_key and api_key.startswith("Bearer "):
                api_key = api_key[7:]

            if not api_key:
                return make_response(jsonify({"error": "No API key provided"}), 400)

            if auth_type == AuthenticationType.ADMIN:
                hashed_admin_api_key = _get_admin_api_key(database=database)
                if not hashed_admin_api_key:
                    return make_response(jsonify({"error": "Could not access admin keys"}), 500)

                if not hash_matches(_input=api_key, hashed=hashed_admin_api_key):  # type: ignore
                    return make_response(jsonify({"error": "Invalid admin API key"}), 401)

                return func(*args, **kwargs)

            else:
                raise Exception(f'Invalid auth type: {auth_type}')

        return wrapper

    return check_authentication
