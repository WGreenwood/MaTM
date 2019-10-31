from configparser import ConfigParser
from os import path
import typing

from MaTM.helpers import environ
from MaTM.theming import ThemeData
from MaTM.theming.colours import Brightness, MaterialColours


class ThemeManager(object):
    change_handlers: typing.List
    current_theme: ThemeData

    config: ConfigParser

    def __init__(self):
        self.change_handlers = []
        self.config = ConfigParser()

    def load_config(self):
        self.config.clear()
        if path.isfile(environ.APP_CONFIG_INI_PATH):
            self.config.read(environ.APP_CONFIG_INI_PATH)
        self.current_theme = ThemeData.from_cfg(self.config)

        for handler in self.change_handlers:
            handler.config_loaded(self)

    def save_config(self):
        self.current_theme.to_cfg(self.config)
        with open(environ.APP_CONFIG_INI_PATH, 'wt') as f:
            self.config.write(f)

    def add_theme_handler(self, handler):
        self.change_handlers.append(handler)

    def on_startup(self):
        for handler in self.change_handlers:
            handler.startup(self)

    def find_and_apply(self,
                       brightness: str = None,
                       primary_colour: str = None,
                       secondary_colour: str = None):
        t = self.current_theme

        b = Brightness.find(brightness or '') or t.brightness
        p = MaterialColours.find(primary_colour or '') or t.primary_colour
        s = MaterialColours.find(secondary_colour or '') or t.secondary_colour

        # Don't apply the exact same theme again
        if b == t.brightness\
            and p == t.primary_colour\
                and s == t.secondary_colour:
            return

        self.apply_theme(ThemeData(b, p, s))

    def apply_theme(self, theme: ThemeData):
        self.current_theme = theme
        self.current_theme.to_cfg(self.config)
        self.save_config()

        for handler in self.change_handlers:
            handler.apply_theme(self)
