import json
import typing

from MaTM.helpers import process
from MaTM.theming import AppThemeManager, ThemeManager


class SpicetifyThemeHandler(AppThemeManager):
    __appname__ = 'spotify'

    def __init__(self):
        super().__init__()
        # TODO: Allow specifying xdotool path
        # TODO: Add optional dependencies:
        # spicetify, xdotool, i3

    def on_startup(self, manager: ThemeManager):
        pass

    def on_apply_theme(self, manager: ThemeManager):
        # TODO: Actually write the template file
        process.run(['spicetify', 'update'])
        self._safe_reload_spotify_windows()

    def _safe_reload_spotify_windows(self):
        active_window = self._get_active_window()
        active_workspaces = self._get_active_workspaces()

        for spotify_window in self._get_spotify_windows():
            self._set_active_window(spotify_window)
            self._reload_spotify_window(spotify_window)

        self._set_active_window(active_window)
        for num in active_workspaces.values():
            process.run(['i3-msg', 'workspace', str(num)])

    def _xdotool(self, args: typing.List[str]):
        process.run(['xdotool'] + args)

    def _get_active_workspaces(self) -> typing.Dict[str, int]:
        active_workspaces = {}
        json_str = process.get_output([
            'i3-msg', '-t', 'get_workspaces'
        ])
        workspaces = json.loads(json_str)
        for workspace in workspaces:
            num = workspace['num']
            visible = workspace['visible']
            output = workspace['output']
            if visible:
                active_workspaces[output] = num

        return active_workspaces

    def _get_active_window(self) -> int:
        return int(process.get_output(['xdotool', 'getactivewindow']))

    def _get_spotify_windows(self) -> typing.List[int]:
        return process.get_list_output([
            'xdotool', 'search',
            '--class', 'spotify'
        ])

    def _set_active_window(self, window):
        self._xdotool(['windowactivate', str(window)])

    def _reload_spotify_window(self, window):
        self._xdotool([
            'key', '-window', window,
            'ctrl+shift+r'
        ])
