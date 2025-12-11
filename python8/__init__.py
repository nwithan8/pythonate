from importlib import import_module

from python8.internal import constants
from ._version import __version__

__all__ = [
    "__version__",
].extend(constants.MODULES)

# Load core elements
from python8.core import (
    checks as checks,
    crypto as crypto,
    dictionaries as dictionaries,
    enums as enums,
    files as files,
    general as general,
    logs as logs,
    objects as objects,
    random as random,
    selector as selector,
    sorting as sorting,
    time as time,
    uuid as uuid,
    yaml as yaml,
)


# Attempt to load each subpackage, but fail gracefully if it cannot be loaded
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
