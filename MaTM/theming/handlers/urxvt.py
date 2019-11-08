from os import path, kill
import signal

from MaTM.helpers import files, process
from MaTM.theming import AppThemeManager, ThemeManager


class UrxvtThemeHandler(AppThemeManager):
    __appname__ = 'urxvt'
    output_file: str
    xresources_path: str

    def __init__(self):
        super().__init__()

    def on_config_loaded(self, manager: ThemeManager):
        CFG_KEY = UrxvtThemeHandler.__appname__
        cfg = manager.config
        section = cfg[CFG_KEY] if CFG_KEY in cfg else {}

        OUTPUT_KEY = 'output'
        if OUTPUT_KEY not in section:
            self.is_active = False
            return

        self.output_file = path.realpath(section[OUTPUT_KEY])
        self.xresources_path = path.expanduser('~/.Xresources')
        if not path.isfile(self.xresources_path):
            self.is_active = False
            return

    def on_startup(self, manager: ThemeManager):
        self.reload_resources()

    def on_apply_theme(self, manager: ThemeManager):
        theme = manager.current_theme

        colourbase = theme.brightness.to_primary_idx()
        primary = theme.primary_colour
        # secondary = theme.secondary_colour

        background = theme.background

        cursorColour = primary[colourbase+200]
        cursorColour2 = cursorColour.get_text_colour()

        data = {
            'background': background,
            'foreground': theme.foreground,
            'borderColor': background,
            'cursorColor': cursorColour,
            'cursorColor2': cursorColour2
        }

        files.write_lines(self.output_file, map(
            lambda i: '*.{}: {}'.format(i[0], i[1].to_hex()),
            data.items()
        ))
        self.reload_resources()
        self.notify_urxvt_processes()

    def reload_resources(self):
        process.run(['xrdb', self.xresources_path])

    def notify_urxvt_processes(self):
        pids = process.get_list_output([
            'get-pids', 'urxvt'
        ])
        for pid in pids:
            kill(int(pid), signal.SIGHUP)
