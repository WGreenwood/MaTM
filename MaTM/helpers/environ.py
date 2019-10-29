from enum import Enum
from os import environ, path
from subprocess import check_output

APP_NAME = 'MaTM'

HOME: str = environ['HOME']
XDG_CONFIG_HOME: str = environ.get(
    'XDG_CONFIG_HOME', default=path.join(
        HOME, '.config'
    )
)

APP_CONFIG_DIR: str = path.join(XDG_CONFIG_HOME, APP_NAME)
APP_CONFIG_INI_PATH: str = path.join(APP_CONFIG_DIR, 'config.ini')
APP_LOGS_DIR: str = path.join(APP_CONFIG_DIR, 'logs')


def xdg_cfg_dir(name: str):
    return path.join(XDG_CONFIG_HOME, name)


class XdgUserDir(Enum):
    Desktop = 0
    Documents = 1
    Downloads = 2
    Music = 3
    Pictures = 4
    PublicShare = 5
    Templates = 6
    Videos = 7


def xdg_dir(xdgdir: XdgUserDir) -> str:
    args = ['xdg-user-dir', xdgdir.name.upper()]
    return check_output(args).decode('utf-8').rstrip()
