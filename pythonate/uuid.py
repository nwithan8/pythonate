import uuid


def time_uuid() -> uuid.UUID:
    """
    Generate a UUID based on the current time (UUID version 1).
    :return: UUID
    :rtype: uuid.UUID
    """
    return uuid.uuid1()


def random_uuid() -> uuid.UUID:
    """
    Generate a random UUID (UUID version 4).
    :return: UUID
    :rtype: uuid.UUID
    """
    return uuid.uuid4()


def generate_uuid(use_random: bool = False) -> uuid.UUID:
    """
    Generate a UUID.
    :param use_random: Get random UUID (rather than time-based UUID).
    :type use_random: bool
    :return: UUID
    :rtype: uuid.UUID
    """
    if use_random:
        return random_uuid()
    return time_uuid()
