from configparser import ConfigParser
from os import path
import typing

from MaTM import environ
from MaTM.theming import ThemeData
from MaTM.theming.colours import Brightness, MaterialColours


class ThemeManager(object):
    change_handlers: typing.List
    current_theme: ThemeData

    config: ConfigParser

    def __init__(self):
        self.change_handlers = []
        self.config = ConfigParser()
        self.load_config()

    def load_config(self):
        self.config.clear()
        self.config_loaded = False
        if path.isfile(environ.APP_CONFIG_INI_PATH):
            self.config.read(environ.APP_CONFIG_INI_PATH)
        self.current_theme = ThemeData.from_cfg(self.config)

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
                       brightness: str,
                       primary_colour: str,
                       secondary_colour: str):
        t = self.current_theme

        b = t.brightness if brightness is None\
            or len(brightness) == 0\
            else Brightness.find(brightness)
        p = t.primary_colour if primary_colour is None\
            or len(primary_colour) == 0\
            else MaterialColours.find(primary_colour)
        s = t.secondary_colour if secondary_colour is None\
            or len(secondary_colour) == 0\
            else MaterialColours.find(secondary_colour)

        ERRMSG = 'Unrecognized material colour: "{}"'
        if p is None:
            m = ERRMSG.format(primary_colour)
            raise ValueError(m)
        if s is None:
            m = ERRMSG.format(secondary_colour)
            raise ValueError(m)

        self.apply_theme(ThemeData(b, p, s))

    def apply_theme(self, theme: ThemeData):
        print('New Theme: {}'.format(theme))
        self.current_theme = theme
        theme.to_cfg(self.config)
        self.save_config()
        for handler in self.change_handlers:
            handlertype = type(handler)
            handlername = handlertype.__appname__\
                if hasattr(handlertype, '__appname__')\
                else handlertype.__name__
            print('Applying theme to {}'.format(handlername))
            handler.apply_theme(self)
