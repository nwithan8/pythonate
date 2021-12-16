def make_enums(name: str, **enums):
    return type(name, (), enums)
