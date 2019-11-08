from MaTM.theming.data import ThemeData  # noqa:F401
from MaTM.theming.handler_base import AppThemeManager  # noqa:F401
from MaTM.theming.manager import ThemeManager  # noqa:F401


def create_default_manager() -> ThemeManager:
    tm = ThemeManager()

    from MaTM.theming.handlers import (
        PolybarThemeHandler,
        RofiThemeHandler,
        SpicetifyThemeHandler,
        UrxvtThemeHandler,
        WallpaperThemeHandler
    )
    tm.add_theme_handler(PolybarThemeHandler())
    tm.add_theme_handler(RofiThemeHandler())
    tm.add_theme_handler(SpicetifyThemeHandler())
    tm.add_theme_handler(UrxvtThemeHandler())
    tm.add_theme_handler(WallpaperThemeHandler())

    tm.load_config()

    return tm
