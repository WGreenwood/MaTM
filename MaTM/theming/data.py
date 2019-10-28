from configparser import ConfigParser
from MaTM.theming.colours import\
    Brightness, Colour, Colours,\
    MaterialColour, MaterialColours


class ThemeData(object):
    SECTION_KEY = 'theme'

    BRIGHTNESS_KEY = 'brightness'
    PRIMARY_COLOUR_KEY = 'primary-colour'
    SECONDARY_COLOUR_KEY = 'secondary-colour'

    primary_colour: MaterialColour
    secondary_colour: MaterialColour

    brightness: Brightness

    @property
    def foreground(self) -> Colour:
        return Colours.light()\
            if self.brightness == Brightness.Dark\
            else Colours.dark()

    @property
    def background(self) -> Colour:
        return Colours.dark()\
            if self.brightness == Brightness.Dark\
            else Colours.light()

    def __init__(self,
                 brightness: Brightness,
                 primary_colour: MaterialColour,
                 secondary_colour: MaterialColour):
        self.brightness = brightness or Brightness.Dark
        self.primary_colour = primary_colour or MaterialColours.purple()
        self.secondary_colour = secondary_colour or MaterialColours.green()

    def to_cfg(self, cfg: ConfigParser):
        cfg[ThemeData.SECTION_KEY] = {
            ThemeData.BRIGHTNESS_KEY: self.brightness.name,
            ThemeData.PRIMARY_COLOUR_KEY: self.primary_colour.name,
            ThemeData.SECONDARY_COLOUR_KEY: self.secondary_colour.name
        }

    @staticmethod
    def from_cfg(cfg: ConfigParser):
        theme = None
        if cfg.has_section(ThemeData.SECTION_KEY):
            theme = cfg[ThemeData.SECTION_KEY]

        def find_value(key, cls):
            if theme is None or key not in theme.keys():
                return None
            value = theme[key]
            return cls.find(value)

        brightness = find_value(
            ThemeData.BRIGHTNESS_KEY,
            Brightness
        )
        primary = find_value(
            ThemeData.PRIMARY_KEY,
            MaterialColours
        )
        secondary = find_value(
            ThemeData.SECONDARY_KEY,
            MaterialColours
        )
        return ThemeData(brightness, primary, secondary)

    def __repr__(self):
        return "ThemeData<brightness: {}, primary_colour: {}, secondary_colour: {}>".format(  # noqa:E501
            self.brightness.name,
            self.primary_colour.name,
            self.secondary_colour.name
        )
