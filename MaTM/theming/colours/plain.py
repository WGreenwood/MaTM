from enum import Enum
from MaTM.helpers import normalized


class Brightness(Enum):
    Light = 0
    Dark = 1

    def find(name: str):
        for b in Brightness:
            if b.name.lower() == name.lower():
                return b
        return None

    def get_colour(self):
        if self == Brightness.Light:
            return Colours.light()
        elif self == Brightness.Dark:
            return Colours.dark()
        else:
            raise ValueError('Unknown brightness value')

    def get_negative_colour(self):
        if self == Brightness.Light:
            return Colours.dark()
        elif self == Brightness.Dark:
            return Colours.light()
        else:
            raise ValueError('Unknown brightness value')


class Colour(object):
    _alpha: int
    _red: int
    _green: int
    _blue: int

    def __init__(self, alpha, red, green, blue):
        self._alpha = alpha
        self._red = red
        self._green = green
        self._blue = blue

    def get_brightness(self):
        def parse_colour(c):
            c = c/255
            if c <= 0.03928:
                return c / 12.92
            return pow((c + 0.055) / 1.055, 2.4)
        r, g, b = map(
            parse_colour,
            [self.red, self.green, self.blue]
        )
        L = (0.2126 * r) + (0.7152 * g) + (0.0722 * b)
        return Brightness.Dark if L > 0.179 else Brightness.Light

    def to_hex(self):
        hex_fmt = '{:02x}'

        alpha_hex = ''
        red_hex = hex_fmt.format(self.red)
        green_hex = hex_fmt.format(self.green)
        blue_hex = hex_fmt.format(self.blue)

        if self.alpha < 255:
            alpha_hex = hex_fmt.format(self.alpha)

        return '#' + ''.join([
            alpha_hex,
            red_hex,
            green_hex,
            blue_hex
        ])

    @staticmethod
    def from_hex(hexstr: str):
        def hexstr_chunks(toint=False):
            # Break into tuples, each with {size} characters
            z = zip(*[iter(hexstr)]*2)
            # Append the tuples into strings
            z = map(''.join, z)
            if toint:
                # Convert them from hex to int
                return map(lambda s: int(s, 16), z)
            return z

        hexlen = len(hexstr)
        if hexlen == 0:
            return None
        elif hexstr[0] == '#':
            hexstr = hexstr[1:]
            hexlen = hexlen - 1

        if hexlen == 3:  # #RGB -> #RRGGBB
            r, g, b = map(lambda c: int(c*2, 16), hexstr)
            return Colour(255, r, g, b)
        elif hexlen == 6:  # #RRGGBB
            r, g, b = hexstr_chunks(toint=True)
            return Colour(255, r, g, b)
        elif hexlen == 8:  # #AARRGGBB
            a, r, g, b = hexstr_chunks(toint=True)
            return Colour(a, r, g, b)

        MSG = 'Colour::from_hex "{}" is not a recognized colour format'
        raise ValueError(MSG.format(hexstr))

    def _clamp(value: int, smallest: int, largest: int) -> int:
        return max(smallest, min(largest, value))

    @property
    def alpha(self):
        return self._alpha

    @property
    def red(self):
        return self._red

    @property
    def green(self):
        return self._green

    @property
    def blue(self):
        return self._blue

    @alpha.setter
    def set_alpha(self, value):
        self._alpha = Colour._clamp(value, 0, 255)

    @red.setter
    def set_red(self, value):
        self._red = Colour._clamp(value, 0, 255)

    @green.setter
    def set_green(self, value):
        self._green = Colour._clamp(value, 0, 255)

    @blue.setter
    def set_blue(self, value):
        self._blue = Colour._clamp(value, 0, 255)

    def __repr__(self):
        return 'Colour<{}>'.format(self.to_hex())


class Colours(object):
    ALL = {
        "White": Colour.from_hex('FFF'),
        "Black": Colour.from_hex('000'),
        "Transparent": Colour.from_hex('00000000'),
        "Light": Colour.from_hex('F5F5F5'),
        "Dark": Colour.from_hex('252525'),
        "Amber": Colour.from_hex('FFB300'),
        "Blue": Colour.from_hex('1E88E5'),
        "Blue Gray": Colour.from_hex('546E7A'),
        "Brown": Colour.from_hex('6D4C41'),
        "Cyan": Colour.from_hex('00ACC1'),
        "Deep Orange": Colour.from_hex('F4511E'),
        "Deep Purple": Colour.from_hex('5E35B1'),
        "Green": Colour.from_hex('43A047'),
        "Gray": Colour.from_hex('757575'),
        "Indigo": Colour.from_hex('3949AB'),
        "Light Blue": Colour.from_hex('039BE5'),
        "Light Green": Colour.from_hex('7CB342'),
        "Lime": Colour.from_hex('C0CA33'),
        "Orange": Colour.from_hex('FB8C00'),
        "Pink": Colour.from_hex('D81B60'),
        "Purple": Colour.from_hex('8E24AA'),
        "Red": Colour.from_hex('E53935'),
        "Teal": Colour.from_hex('00897B'),
        "Yellow": Colour.from_hex('FDD835')
    }

    def get(name: str) -> Colour:
        return normalized.find(Colours.ALL, name)

    def white() -> Colour:
        return Colours.get('white')

    def black() -> Colour:
        return Colours.get('black')

    def transparent() -> Colour:
        return Colours.get('transparent')

    def light() -> Colour:
        return Colours.get('light')

    def dark() -> Colour:
        return Colours.get('dark')

    def amber() -> Colour:
        return Colours.get('amber')

    def blue() -> Colour:
        return Colours.get('blue')

    def blue_gray() -> Colour:
        return Colours.get('blue_gray')

    def brown() -> Colour:
        return Colours.get('brown')

    def cyan() -> Colour:
        return Colours.get('cyan')

    def deep_orange() -> Colour:
        return Colours.get('deep_orange')

    def deep_purple() -> Colour:
        return Colours.get('deep_purple')

    def green() -> Colour:
        return Colours.get('green')

    def gray() -> Colour:
        return Colours.get('gray')

    def indigo() -> Colour:
        return Colours.get('indigo')

    def light_blue() -> Colour:
        return Colours.get('light_blue')

    def light_green() -> Colour:
        return Colours.get('light_green')

    def lime() -> Colour:
        return Colours.get('lime')

    def orange() -> Colour:
        return Colours.get('orange')

    def pink() -> Colour:
        return Colours.get('pink')

    def purple() -> Colour:
        return Colours.get('purple')

    def red() -> Colour:
        return Colours.get('red')

    def teal() -> Colour:
        return Colours.get('teal')

    def yellow() -> Colour:
        return Colours.get('yellow')
