import uuid


def time_uuid():
    return uuid.uuid1()


def random_uuid():
    return uuid.uuid4()


def generate_uuid(use_random: bool = False):
    if use_random:
        return random_uuid()
    return time_uuid()
