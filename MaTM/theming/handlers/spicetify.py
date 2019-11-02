from subprocess import CalledProcessError
import json
import typing

from MaTM.helpers import files, process
from MaTM.theming import AppThemeManager, ThemeManager


class SpicetifyThemeHandler(AppThemeManager):
    __appname__ = 'spotify'

    def __init__(self):
        super().__init__()

    def on_config_loaded(self, manager: ThemeManager):
        CFG_KEY = 'spotify'
        cfg = manager.config
        section = cfg[CFG_KEY] if CFG_KEY in cfg else {}

        self.spicetify_path = files.get_program_path(section, 'spicetify')
        self.xdotool_path = files.get_program_path(section, 'xdotool')
        self.i3msg_path = files.get_program_path(section, 'i3-msg')

        self.is_active = all(map(
            lambda p: p is not None, [
                self.spicetify_path,
                self.xdotool_path,
                self.i3msg_path
            ]
        ))

    def on_startup(self, manager: ThemeManager):
        pass

    def on_apply_theme(self, manager: ThemeManager):
        # TODO: Actually write the template file
        process.call([self.spicetify_path, 'update'])
        self._safe_reload_spotify_windows()

    def _safe_reload_spotify_windows(self):
        spotify_windows = self._get_spotify_windows()
        if len(spotify_windows) == 0:
            return
        active_window = self._get_active_window()
        active_workspaces = self._get_active_workspaces()

        for window in spotify_windows:
            self._set_active_window(window)
            self._reload_spotify_window(window)

        for num in active_workspaces.values():
            process.call([self.i3msg_path, 'workspace', str(num)])
        self._set_active_window(active_window)

    def _get_active_workspaces(self) -> typing.Dict[str, int]:
        active_workspaces = {}
        json_str = process.get_output([
            self.i3msg_path, '-t', 'get_workspaces'
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
        return int(process.get_output([self.xdotool_path, 'getactivewindow']))

    def _get_spotify_windows(self) -> typing.List[int]:
        try:
            return process.get_list_output([
                self.xdotool_path, 'search',
                '--class', 'spotify'
            ])
        except CalledProcessError:
            return []

    def _set_active_window(self, window):
        process.call([self.xdotool_path, 'windowactivate', str(window)])

    def _reload_spotify_window(self, window):
        process.call([
            self.xdotool_path,
            'key', '-window', window,
            'ctrl+shift+r'
        ])
