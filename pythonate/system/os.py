import platform
from enum import Enum


class OS(Enum):
    LINUX = 'Linux'
    WINDOWS = 'Windows'
    MAC = 'Darwin'
    MAC_SERVER = 'MacOS X Server'
    SOLARIS = 'Solaris'
    FREEBSD = 'FreeBSD'
    OPENBSD = 'OpenBSD'
    NETBSD = 'NetBSD'
    AIX = 'AIX'
    HPUX = 'HP-UX'
    IRIX = 'IRIX'
    OSF1 = 'OSF1'
    SCO = 'SCO'
    UNKNOWN = 'Unknown'


def get_os() -> OS:
    name = platform.system()
    if name == 'Linux':
        return OS.LINUX
    elif name == 'Windows':
        return OS.WINDOWS
    elif name == 'Darwin':
        return OS.MAC
    elif name in ['Solaris', 'SunOS']:
        return OS.SOLARIS
    elif name == 'FreeBSD':
        return OS.FREEBSD
    elif name == 'OpenBSD':
        return OS.OPENBSD
    elif name == 'NetBSD':
        return OS.NETBSD
    elif name == 'AIX':
        return OS.AIX
    elif name == 'HP-UX':
        return OS.HPUX
    elif name == 'IRIX':
        return OS.IRIX
    elif name == 'OSF1':
        return OS.OSF1
    elif name == 'SCO':
        return OS.SCO
    elif name == "MacOS X Server":
        return OS.MAC_SERVER
    else:
        raise Exception(f'Unknown OS: {name}')


def get_os_release() -> str:
    return platform.release()


def get_os_version() -> str:
    return platform.version()
