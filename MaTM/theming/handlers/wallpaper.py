from os import path

from PIL import Image, ImageDraw

from MaTM.theming import AppThemeManager, ThemeManager
from MaTM.helpers import environ, process
from MaTM.helpers.wallpapers import random_colours, TilingType


class WallpaperThemeHandler(AppThemeManager):
    __appname__ = 'wallpaper'

    def __init__(self):
        super().__init__()

    def on_config_loaded(self, manager: ThemeManager):
        pass

    def on_startup(self, manager: ThemeManager):
        output_file = path.join(environ.APP_CONFIG_DIR, 'wallpaper.png')

        self.create_wallpaper(manager, TilingType.Hexagon, output_file)

    def on_apply_theme(self, manager: ThemeManager):
        self.on_startup(manager)

    def create_wallpaper(self, manager: ThemeManager,
                         tilingType: TilingType,
                         output_file: str):
        width, height = self.get_resolution()
        img = Image.new(mode='RGB', size=(width, height))

        polygons = tilingType.call_generator(width, height)
        colours = self.get_wallpaper_colours(manager)

        for polygon, colour in zip(polygons, colours):
            ImageDraw.Draw(img).polygon(polygon, fill=colour)

        img.save(output_file)
        process.call([
            'feh',
            '--bg-fill',
            output_file,
            '--no-fehbg'
        ])

    def get_wallpaper_colours(self, manager: ThemeManager):
        theme = manager.current_theme
        accent_idx = theme.brightness.to_accent_idx()

        primary = theme.primary_colour
        secondary = theme.secondary_colour
        if primary == secondary:
            primary, secondary = primary[accent_idx], secondary[accent_idx+200]
        else:
            primary, secondary = primary[accent_idx], secondary[accent_idx]
        return random_colours(primary, secondary)

    def get_resolution(self):
        xdpyout = process.get_list_output(['xdpyinfo'])
        res = [line for line in xdpyout if 'dimensions' in line][0]
        res = list(filter(None, res.split(' ')))
        width, height = res[1].split('x')
        return int(width), int(height)
