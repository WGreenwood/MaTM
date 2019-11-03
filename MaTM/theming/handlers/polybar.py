from configparser import ConfigParser
from os import path

from MaTM.helpers import environ, process
from MaTM.theming import AppThemeManager, ThemeManager

_KEY = 'polybar'


class PolybarThemeHandler(AppThemeManager):
    __appname__ = _KEY
    polybar_dir: str
    launch_script: str

    def __init__(self):
        super().__init__()

    def _get_polybar_dir(self, cfg: ConfigParser):
        return cfg[_KEY] if _KEY in cfg else environ.xdg_cfg_dir(_KEY)

    def on_config_loaded(self, manager: ThemeManager):
        self.polybar_dir = self._get_polybar_dir(manager.config)
        self.launch_script = path.join(self.polybar_dir, 'launch2.sh')
        self.is_active = path.isdir(self.polybar_dir)\
            and path.isfile(self.launch_script)

    def on_startup(self, manager: ThemeManager):
        process.call([self.launch_script])

    def on_apply_theme(self, manager: ThemeManager):
        themeini_path = path.join(self.polybar_dir, 'theme2.ini')
        theme = manager.current_theme

        colourbase = theme.brightness.to_primary_idx()
        primary = theme.primary_colour
        secondary = theme.secondary_colour

        matm_icons = primary[colourbase]
        icons = secondary[colourbase]
        overline = primary[colourbase+200]
        workspaces = primary[colourbase]
        workspaces_text = workspaces.get_text_colour()

        inidata = {
            'background': theme.background,
            'foreground': theme.foreground,
            'matm-icons': matm_icons,
            'icons': icons,
            'overline': overline,
            'workspace-indicator': workspaces,
            'workspace-indicator-text': workspaces_text,
        }

        cfg = ConfigParser()
        cfg['theme'] = {
            k: v.to_hex()
            for k, v in inidata.items()
        }
        with open(themeini_path, 'wt') as f:
            cfg.write(f)
        self.on_startup(manager)
