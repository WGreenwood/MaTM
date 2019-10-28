from MaTM.theming.colours import Brightness, Colour
from MaTM.helpers import normalized


class MaterialColour(object):
    name: str
    shade1: Colour
    shade2: Colour
    shade3: Colour
    shade4: Colour
    shade5: Colour
    shade6: Colour
    shade7: Colour
    shade8: Colour

    def __init__(self, name: str, shade1: str,
                 shade2: str, shade3: str,
                 shade4: str, shade5: str,
                 shade6: str, shade7: str,
                 shade8: str):
        self.name = name
        self.shade1 = Colour.from_hex(shade1)
        self.shade2 = Colour.from_hex(shade2)
        self.shade3 = Colour.from_hex(shade3)
        self.shade4 = Colour.from_hex(shade4)
        self.shade5 = Colour.from_hex(shade5)
        self.shade6 = Colour.from_hex(shade6)
        self.shade7 = Colour.from_hex(shade7)
        self.shade8 = Colour.from_hex(shade8)

    def get_shade(self, brightness: Brightness):
        if brightness == Brightness.Light:
            return self.shade8
        return self.shade1

    def to_dict(self):
        brightness: Brightness = self.shade4.get_brightness()
        accent_text: Colour = Brightness.get_negative_colour(brightness)
        return {
            'shade1': self.shade1.to_hex(),
            'shade2': self.shade2.to_hex(),
            'shade3': self.shade3.to_hex(),
            'shade4': self.shade4.to_hex(),
            'shade5': self.shade5.to_hex(),
            'shade6': self.shade6.to_hex(),
            'shade7': self.shade7.to_hex(),
            'shade8': self.shade8.to_hex(),
            'accent-text': accent_text.to_hex()
        }

    def __repr__(self):
        return f'MaterialColour<{self.name}>'


class MaterialColours(object):
    ALL = {
        'Amber': MaterialColour(
            'Amber',
            'FF6F00', 'FF8F00',
            'FFA000', 'FFA000',
            'FFC107', 'FFC107',
            'FFD54F', 'FFE082'
        ),
        'Blue': MaterialColour(
            'Blue',
            '0D47A1', '1565C0',
            '1976D2', '1E88E5',
            '2196F3', '42A5F5',
            '64B5F6', '90CAF9'
        ),
        'Blue Gray': MaterialColour(
            'Blue Gray',
            '263238', '37474F',
            '455A64', '546E7A',
            '607D8B', '78909C',
            '90A4AE', 'B0BEC5'
        ),
        'Brown': MaterialColour(
            'Brown',
            '3E2723', '4E342E',
            '5D4037', '6D4C41',
            '795548', '8D6E63',
            'A1887F', 'BCAAA4'
        ),
        'Cyan': MaterialColour(
            'Cyan',
            '006064', '00838F',
            '0097A7', '00ACC1',
            '00BCD4', '26C6DA',
            '4DD0E1', '80DEEA'
        ),
        'Deep Orange': MaterialColour(
            'Deep Orange',
            'BF360C', 'D84315',
            'E64A19', 'F4511E',
            'FF5722', 'FF7043',
            'FF8A65', 'FFAB91'
        ),
        'Deep Purple': MaterialColour(
            'Deep Purple',
            '311B92', '4527A0',
            '512DA8', '5E35B1',
            '673AB7', '7E57C2',
            '9575CD', 'B39DDB'
        ),
        'Green': MaterialColour(
            'Green',
            '1B5E20', '2E7D32',
            '388E3C', '43A047',
            '4CAF50', '66BB6A',
            '81C784', 'A5D6A7'
        ),
        'Gray': MaterialColour(
            'Gray',
            '212121', '424242',
            '616161', '757575',
            '9E9E9E', '8D8D8D',
            'D4D4D4', 'EEEEEE'
        ),
        'Indigo': MaterialColour(
            'Indigo',
            '1A237E', '283593',
            '303F9F', '3949AB',
            '3F51B5', '5C6BC0',
            '7986CB', '9FA8DA'
        ),
        'Light Blue': MaterialColour(
            'Light Blue',
            '01579B', '0277BD',
            '0288D1', '039BE5',
            '03A9F4', '29B6F6',
            '4FC3F7', '81D4FA'
        ),
        'Light Green': MaterialColour(
            'Light Green',
            '33691E', '558B2F',
            '689F38', '7CB342',
            '8BC34A', '9CCC65',
            'AED581', 'C5E1A5'
        ),
        'Lime': MaterialColour(
            'Lime',
            '827717', '9E9D24',
            'AFB42B', 'C0CA33',
            'CDDC39', 'D4E157',
            'DCE775', 'E6EE9C'
        ),
        'Orange': MaterialColour(
            'Orange',
            'E65100', 'EF6C00',
            'F57C00', 'FB8C00',
            'FF9800', 'FFA726',
            'FFB74D', 'FFB74D'
        ),
        'Pink': MaterialColour(
            'Pink',
            '880E4F', 'AD1457',
            'C2185B', 'D81B60',
            'E91E63', 'EC407A',
            'F06292', 'F48FB1'
        ),
        'Purple': MaterialColour(
            'Purple',
            '4A148C', '6A1B9A',
            '7B1FA2', '8E24AA',
            '9C27B0', 'AB47BC',
            'BA68C8', 'CE93D8'
        ),
        'Red': MaterialColour(
            'Red',
            'B71C1C', 'C62828',
            'D32F2F', 'E53935',
            'EE413D', 'EF5350',
            'E57373', 'EF9A9A'
        ),
        'Teal': MaterialColour(
            'Teal',
            '004D40', '00695C',
            '00796B', '00897B',
            '009688', '26A69A',
            '4DB6AC', '80CBC4'
        ),
        'Yellow': MaterialColour(
            'Yellow',
            'F57F17', 'F9A825',
            'FBC02D', 'FDD835',
            'FFEB3B', 'FFEE58',
            'FFF176', 'FFF59D'
        ),
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
