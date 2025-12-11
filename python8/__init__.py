from importlib import import_module

from internal import constants
from ._version import __version__

__all__ = [
    "__version__",
].extend(constants.MODULES)


def _try_load_subpkg(name):
    try:
        return import_module(f"{__name__}.{name}")
    except Exception:
        return None


config = _try_load_subpkg(constants.CONFIG_MODULE)
conversions = _try_load_subpkg(constants.CONVERSIONS_MODULE)
database = _try_load_subpkg(constants.DATABASE_MODULE)
rest_api = _try_load_subpkg(constants.REST_API_MODULE)
security = _try_load_subpkg(constants.SECURITY_MODULE)
system = _try_load_subpkg(constants.SYSTEM_MODULE)
web = _try_load_subpkg(constants.WEB_MODULE)
