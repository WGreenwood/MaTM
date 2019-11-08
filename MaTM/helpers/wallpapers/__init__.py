import random
from enum import Enum
from MaTM.helpers.wallpapers.colours import random_colours  # noqa:F401


class TilingType(Enum):
    Square = 1
    Triangle = 2
    Hexagon = 3

    @staticmethod
    def get_random():
        return TilingType(random.randint(1, 3))

    def call_generator(self, width, height):
        if self == TilingType.Square:
            from MaTM.helpers.wallpapers.tiling import generate_squares
            return generate_squares(width, height)
        elif self == TilingType.Triangle:
            from MaTM.helpers.wallpapers.tiling import generate_triangles
            return generate_triangles(width, height)
        elif self == TilingType.Hexagon:
            from MaTM.helpers.wallpapers.tiling import generate_hexagons
            return generate_hexagons(width, height)
        else:
            return TilingType.Square.call_generator()
