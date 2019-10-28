from MaTM.theming.data import ThemeData  # noqa:F401
from MaTM.theming.handler_base import AppThemeManager  # noqa:F401
from MaTM.theming.manager import ThemeManager  # noqa:F401


def create_default_manager() -> ThemeManager:
    tm = ThemeManager()

    from MaTM.theming.handlers import PolybarThemeHandler
    tm.add_theme_handler(PolybarThemeHandler())

    return tm
