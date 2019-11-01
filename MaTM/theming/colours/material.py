import typing

from MaTM.theming.colours import Colour
from MaTM.helpers import normalized


class MaterialColour(object):
    name: str
    colours: typing.Dict[str, Colour]

    def __init__(self, name: str, colours: typing.Dict[str, Colour] = {}):
        self.name = name
        self.colours = colours

    def __contains__(self, key):
        return key in self.colours

    def __getitem__(self, key) -> Colour:
        if type(key) is int:
            key = str(key)
        else:
            assert type(key) is str
        return self.colours[key]

    def __setitem__(self, key, item):
        assert type(key) is str
        assert type(item) is Colour
        self.colours[key] = item

    def __delitem__(self, key):
        assert type(key) is str
        del self.colours[key]

    def __repr__(self):
        return f'{{ MaterialColour:{self.name} }}>'


class MaterialColours(object):
    ALL = {
        'Amber': MaterialColour(
            'Amber', {
                '50': Colour.from_hex('FFF8E1'),
                '100': Colour.from_hex('FFECB3'),
                '200': Colour.from_hex('FFE082'),
                '300': Colour.from_hex('FFD54F'),
                '400': Colour.from_hex('FFC107'),
                '500': Colour.from_hex('FFC107'),
                '600': Colour.from_hex('FFA000'),
                '700': Colour.from_hex('FFA000'),
                '800': Colour.from_hex('FF8F00'),
                '900': Colour.from_hex('FF6F00'),
                'A100': Colour.from_hex('FFE57F'),
                'A200': Colour.from_hex('FFD740'),
                'A400': Colour.from_hex('FFC400'),
                'A700': Colour.from_hex('FFAB00')
            }
        ),
        'Blue': MaterialColour(
            'Blue', {
                '50': Colour.from_hex('E3F2FD'),
                '100': Colour.from_hex('BBDEFB'),
                '200': Colour.from_hex('90CAF9'),
                '300': Colour.from_hex('64B5F6'),
                '400': Colour.from_hex('42A5F5'),
                '500': Colour.from_hex('2196F3'),
                '600': Colour.from_hex('1E88E5'),
                '700': Colour.from_hex('1976D2'),
                '800': Colour.from_hex('1565C0'),
                '900': Colour.from_hex('0D47A1'),
                'A100': Colour.from_hex('82B1FF'),
                'A200': Colour.from_hex('448AFF'),
                'A400': Colour.from_hex('2979FF'),
                'A700': Colour.from_hex('2962FF')
            }
        ),
        'Blue Gray': MaterialColour(
            'Blue Gray', {
                '50': Colour.from_hex('ECEFF1'),
                '100': Colour.from_hex('CFD8DC'),
                '200': Colour.from_hex('B0BEC5'),
                '300': Colour.from_hex('90A4AE'),
                '400': Colour.from_hex('78909C'),
                '500': Colour.from_hex('607D8B'),
                '600': Colour.from_hex('546E7A'),
                '700': Colour.from_hex('455A64'),
                '800': Colour.from_hex('37474F'),
                '900': Colour.from_hex('263238'),
            }
        ),
        'Brown': MaterialColour(
            'Brown', {
                '50': Colour.from_hex('EFEBE9'),
                '100': Colour.from_hex('D7CCC8'),
                '200': Colour.from_hex('BCAAA4'),
                '300': Colour.from_hex('A1887F'),
                '400': Colour.from_hex('8D6E63'),
                '500': Colour.from_hex('795548'),
                '600': Colour.from_hex('6D4C41'),
                '700': Colour.from_hex('5D4037'),
                '800': Colour.from_hex('4E342E'),
                '900': Colour.from_hex('3E2723'),
            }
        ),
        'Cyan': MaterialColour(
            'Cyan', {
                '50': Colour.from_hex('E0F7FA'),
                '100': Colour.from_hex('B2EBF2'),
                '200': Colour.from_hex('80DEEA'),
                '300': Colour.from_hex('4DD0E1'),
                '400': Colour.from_hex('26C6DA'),
                '500': Colour.from_hex('00BCD4'),
                '600': Colour.from_hex('00ACC1'),
                '700': Colour.from_hex('0097A7'),
                '800': Colour.from_hex('00838F'),
                '900': Colour.from_hex('006064'),
                'A100': Colour.from_hex('84FFFF'),
                'A200': Colour.from_hex('18FFFF'),
                'A400': Colour.from_hex('00E5FF'),
                'A700': Colour.from_hex('00B8D4')
            }
        ),
        'Deep Orange': MaterialColour(
            'Deep Orange', {
                '50': Colour.from_hex('FBE9E7'),
                '100': Colour.from_hex('FFCCBC'),
                '200': Colour.from_hex('FFAB91'),
                '300': Colour.from_hex('FF8A65'),
                '400': Colour.from_hex('FF7043'),
                '500': Colour.from_hex('FF5722'),
                '600': Colour.from_hex('F4511E'),
                '700': Colour.from_hex('E64A19'),
                '800': Colour.from_hex('D84315'),
                '900': Colour.from_hex('BF360C'),
                'A100': Colour.from_hex('FF9E80'),
                'A200': Colour.from_hex('FF6E40'),
                'A400': Colour.from_hex('FF3D00'),
                'A700': Colour.from_hex('DD2C00')
            }
        ),
        'Deep Purple': MaterialColour(
            'Deep Purple', {
                '50': Colour.from_hex('EDE7F6'),
                '100': Colour.from_hex('D1C4E9'),
                '200': Colour.from_hex('B39DDB'),
                '300': Colour.from_hex('9575CD'),
                '400': Colour.from_hex('7E57C2'),
                '500': Colour.from_hex('673AB7'),
                '600': Colour.from_hex('5E35B1'),
                '700': Colour.from_hex('512DA8'),
                '800': Colour.from_hex('4527A0'),
                '900': Colour.from_hex('311B92'),
                'A100': Colour.from_hex('B388FF'),
                'A200': Colour.from_hex('7C4DFF'),
                'A400': Colour.from_hex('651FFF'),
                'A700': Colour.from_hex('6200EA')
            }
        ),
        'Green': MaterialColour(
            'Green', {
                '50': Colour.from_hex('E8F5E9'),
                '100': Colour.from_hex('C8E6C9'),
                '200': Colour.from_hex('A5D6A7'),
                '300': Colour.from_hex('81C784'),
                '400': Colour.from_hex('66BB6A'),
                '500': Colour.from_hex('4CAF50'),
                '600': Colour.from_hex('43A047'),
                '700': Colour.from_hex('388E3C'),
                '800': Colour.from_hex('2E7D32'),
                '900': Colour.from_hex('1B5E20'),
                'A100': Colour.from_hex('B9F6CA'),
                'A200': Colour.from_hex('69F0AE'),
                'A400': Colour.from_hex('00E676'),
                'A700': Colour.from_hex('00C853')
            }
        ),
        'Gray': MaterialColour(
            'Gray', {
                '50': Colour.from_hex('FAFAFA'),
                '100': Colour.from_hex('F5F5F5'),
                '200': Colour.from_hex('EEEEEE'),
                '300': Colour.from_hex('D4D4D4'),
                '400': Colour.from_hex('8D8D8D'),
                '500': Colour.from_hex('9E9E9E'),
                '600': Colour.from_hex('757575'),
                '700': Colour.from_hex('616161'),
                '800': Colour.from_hex('424242'),
                '900': Colour.from_hex('212121'),
            }
        ),
        'Indigo': MaterialColour(
            'Indigo', {
                '50': Colour.from_hex('E8EAF6'),
                '100': Colour.from_hex('C5CAE9'),
                '200': Colour.from_hex('9FA8DA'),
                '300': Colour.from_hex('7986CB'),
                '400': Colour.from_hex('5C6BC0'),
                '500': Colour.from_hex('3F51B5'),
                '600': Colour.from_hex('3949AB'),
                '700': Colour.from_hex('303F9F'),
                '800': Colour.from_hex('283593'),
                '900': Colour.from_hex('1A237E'),
                'A100': Colour.from_hex('8C9EFF'),
                'A200': Colour.from_hex('536DFE'),
                'A400': Colour.from_hex('3D5AFE'),
                'A700': Colour.from_hex('304FFE')
            }
        ),
        'Light Blue': MaterialColour(
            'Light Blue', {
                '50': Colour.from_hex('E1F5FE'),
                '100': Colour.from_hex('B3E5FC'),
                '200': Colour.from_hex('81D4FA'),
                '300': Colour.from_hex('4FC3F7'),
                '400': Colour.from_hex('29B6F6'),
                '500': Colour.from_hex('03A9F4'),
                '600': Colour.from_hex('039BE5'),
                '700': Colour.from_hex('0288D1'),
                '800': Colour.from_hex('0277BD'),
                '900': Colour.from_hex('01579B'),
                'A100': Colour.from_hex('80D8FF'),
                'A200': Colour.from_hex('40C4FF'),
                'A400': Colour.from_hex('00B0FF'),
                'A700': Colour.from_hex('0091EA')
            }
        ),
        'Light Green': MaterialColour(
            'Light Green', {
                '50': Colour.from_hex('F1F8E9'),
                '100': Colour.from_hex('DCEDC8'),
                '200': Colour.from_hex('C5E1A5'),
                '300': Colour.from_hex('AED581'),
                '400': Colour.from_hex('9CCC65'),
                '500': Colour.from_hex('8BC34A'),
                '600': Colour.from_hex('7CB342'),
                '700': Colour.from_hex('689F38'),
                '800': Colour.from_hex('558B2F'),
                '900': Colour.from_hex('33691E'),
                'A100': Colour.from_hex('CCFF90'),
                'A200': Colour.from_hex('B2FF59'),
                'A400': Colour.from_hex('76FF03'),
                'A700': Colour.from_hex('64DD17')
            }
        ),
        'Lime': MaterialColour(
            'Lime', {
                '50': Colour.from_hex('F9FBE7'),
                '100': Colour.from_hex('F0F4C3'),
                '200': Colour.from_hex('E6EE9C'),
                '300': Colour.from_hex('DCE775'),
                '400': Colour.from_hex('D4E157'),
                '500': Colour.from_hex('CDDC39'),
                '600': Colour.from_hex('C0CA33'),
                '700': Colour.from_hex('AFB42B'),
                '800': Colour.from_hex('9E9D24'),
                '900': Colour.from_hex('827717'),
                'A100': Colour.from_hex('F4FF81'),
                'A200': Colour.from_hex('EEFF41'),
                'A400': Colour.from_hex('EEFF41'),
                'A700': Colour.from_hex('AEEA00')
            }
        ),
        'Orange': MaterialColour(
            'Orange', {
                '50': Colour.from_hex('FFF3E0'),
                '100': Colour.from_hex('FFE0B2'),
                '200': Colour.from_hex('FFB74D'),
                '300': Colour.from_hex('FFB74D'),
                '400': Colour.from_hex('FFA726'),
                '500': Colour.from_hex('FF9800'),
                '600': Colour.from_hex('FB8C00'),
                '700': Colour.from_hex('F57C00'),
                '800': Colour.from_hex('EF6C00'),
                '900': Colour.from_hex('E65100'),
                'A100': Colour.from_hex('FFD180'),
                'A200': Colour.from_hex('FFAB40'),
                'A400': Colour.from_hex('FF9100'),
                'A700': Colour.from_hex('FF6D00')
            }
        ),
        'Pink': MaterialColour(
            'Pink', {
                '50': Colour.from_hex('FCE4EC'),
                '100': Colour.from_hex('F8BBD0'),
                '200': Colour.from_hex('F48FB1'),
                '300': Colour.from_hex('F06292'),
                '400': Colour.from_hex('EC407A'),
                '500': Colour.from_hex('E91E63'),
                '600': Colour.from_hex('D81B60'),
                '700': Colour.from_hex('C2185B'),
                '800': Colour.from_hex('AD1457'),
                '900': Colour.from_hex('880E4F'),
                'A100': Colour.from_hex('FF80AB'),
                'A200': Colour.from_hex('FF4081'),
                'A400': Colour.from_hex('F50057'),
                'A700': Colour.from_hex('C51162')
            }
        ),
        'Purple': MaterialColour(
            'Purple', {
                '50': Colour.from_hex('F3E5F5'),
                '100': Colour.from_hex('E1BEE7'),
                '200': Colour.from_hex('CE93D8'),
                '300': Colour.from_hex('BA68C8'),
                '400': Colour.from_hex('AB47BC'),
                '500': Colour.from_hex('9C27B0'),
                '600': Colour.from_hex('8E24AA'),
                '700': Colour.from_hex('7B1FA2'),
                '800': Colour.from_hex('6A1B9A'),
                '900': Colour.from_hex('4A148C'),
                'A100': Colour.from_hex('EA80FC'),
                'A200': Colour.from_hex('E040FB'),
                'A400': Colour.from_hex('D500F9'),
                'A700': Colour.from_hex('AA00FF')
            }
        ),
        'Red': MaterialColour(
            'Red', {
                '50': Colour.from_hex('FFEBEE'),
                '100': Colour.from_hex('FFCDD2'),
                '200': Colour.from_hex('EF9A9A'),
                '300': Colour.from_hex('E57373'),
                '400': Colour.from_hex('EF5350'),
                '500': Colour.from_hex('EE413D'),
                '600': Colour.from_hex('E53935'),
                '700': Colour.from_hex('D32F2F'),
                '800': Colour.from_hex('C62828'),
                '900': Colour.from_hex('B71C1C'),
                'A100': Colour.from_hex('FF8A80'),
                'A200': Colour.from_hex('FF5252'),
                'A400': Colour.from_hex('FF1744'),
                'A700': Colour.from_hex('D50000')
            }
        ),
        'Teal': MaterialColour(
            'Teal', {
                '50': Colour.from_hex('E0F2F1'),
                '100': Colour.from_hex('B2DFDB'),
                '200': Colour.from_hex('80CBC4'),
                '300': Colour.from_hex('4DB6AC'),
                '400': Colour.from_hex('26A69A'),
                '500': Colour.from_hex('009688'),
                '600': Colour.from_hex('00897B'),
                '700': Colour.from_hex('00796B'),
                '800': Colour.from_hex('00695C'),
                '900': Colour.from_hex('004D40'),
                'A100': Colour.from_hex('A7FFEB'),
                'A200': Colour.from_hex('64FFDA'),
                'A400': Colour.from_hex('1DE9B6'),
                'A700': Colour.from_hex('00BFA5')
            }
        ),
        'Yellow': MaterialColour(
            'Yellow', {
                '50': Colour.from_hex('FFFDE7'),
                '100': Colour.from_hex('FFF9C4'),
                '200': Colour.from_hex('FFF59D'),
                '300': Colour.from_hex('FFF176'),
                '400': Colour.from_hex('FFEE58'),
                '500': Colour.from_hex('FFEB3B'),
                '600': Colour.from_hex('FDD835'),
                '700': Colour.from_hex('FBC02D'),
                '800': Colour.from_hex('F9A825'),
                '900': Colour.from_hex('F57F17'),
                'A100': Colour.from_hex('FFFF8D'),
                'A200': Colour.from_hex('FFFF00'),
                'A400': Colour.from_hex('FFEA00'),
                'A700': Colour.from_hex('FFD600')
            }
        )
    }

    def find(name: str) -> MaterialColour:
        return normalized.find(MaterialColours.ALL, name)

    def amber() -> MaterialColour:
        return MaterialColours.find('amber')

    def blue() -> MaterialColour:
        return MaterialColours.find('blue')

    def blue_gray() -> MaterialColour:
        return MaterialColours.find('blue_gray')

    def brown() -> MaterialColour:
        return MaterialColours.find('brown')

    def cyan() -> MaterialColour:
        return MaterialColours.find('cyan')

    def deep_orange() -> MaterialColour:
        return MaterialColours.find('deep_orange')

    def deep_purple() -> MaterialColour:
        return MaterialColours.find('deep_purple')

    def green() -> MaterialColour:
        return MaterialColours.find('green')

    def gray() -> MaterialColour:
        return MaterialColours.find('gray')

    def indigo() -> MaterialColour:
        return MaterialColours.find('indigo')

    def light_blue() -> MaterialColour:
        return MaterialColours.find('light_blue')

    def light_green() -> MaterialColour:
        return MaterialColours.find('light_green')

    def lime() -> MaterialColour:
        return MaterialColours.find('lime')

    def orange() -> MaterialColour:
        return MaterialColours.find('orange')

    def pink() -> MaterialColour:
        return MaterialColours.find('pink')

    def purple() -> MaterialColour:
        return MaterialColours.find('purple')

    def red() -> MaterialColour:
        return MaterialColours.find('red')

    def teal() -> MaterialColour:
        return MaterialColours.find('teal')

    def yellow() -> MaterialColour:
        return MaterialColours.find('yellow')

