from configparser import ConfigParser
from os import path, devnull
from subprocess import call

from MaTM.helpers import environ
from MaTM.theming import AppThemeManager, ThemeManager


class PolybarThemeHandler(AppThemeManager):
    __appname__ = 'polybar'

    def __init__(self):
        super().__init__()
        self.polybar_dir = environ.xdg_cfg_dir('polybar')
        self.is_active = path.isdir(self.polybar_dir)

    def on_startup(self, manager: ThemeManager):
        call([
            path.join(self.polybar_dir, 'launch.sh')
        ], stdout=devnull, stderr=devnull)

    def on_apply_theme(self, manager: ThemeManager):
        themeini_path = path.join(self.polybar_dir, 'theme2.ini')
        theme = manager.current_theme

        inidata = {
            'background': theme.background.to_hex(),
            'foreground': theme.foreground.to_hex()
        }
        inidata.update(theme.primary_colour.to_dict('primary-'))
        inidata.update(theme.primary_colour.to_dict('secondary-'))

        cfg = ConfigParser()
        cfg['theme'] = inidata
        with open(themeini_path, 'wt') as f:
            cfg.write(f)
