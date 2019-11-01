from MaTM.helpers.rofi import Rofi
from MaTM.helpers.rofi import strip_html
from MaTM.theming.colours import Brightness, MaterialColours
from MaTM.services.dbus import quick_client

from enum import Enum


class RofiState(Enum):
    Brightness = (
        1, 'Choose brightness level',
        'brightness', 'brightness')
    PrimaryColour = (
        2, 'Choose a primary colour',
        'primary', 'primary_colour')
    SecondaryColour = (
        3, 'Choose a secondary colour',
        'secondary', 'secondary_colour')

    def matches_state(self, other) -> bool:
        return other == self.value[1]

    @staticmethod
    def from_arg(arg):
        for r in RofiState:
            if r.value[2] == arg:
                return r
        return None


BRIGHTNESS_OPTIONS = [b.name for b in Brightness]
COLOUR_OPTIONS = [c for c in MaterialColours.ALL.keys()]


def main():
    import sys
    argcount = len(sys.argv)
    if argcount <= 1:
        exit(1)
    state = RofiState.from_arg(sys.argv[1])

    selected = sys.argv[2] if argcount > 2 else ''

    client = quick_client()

    rofi = Rofi(message=state.value[1])
    rofi_selected_key = ''

    def add_options(options):
        for option in options:
            rofi.add_option(option, option, None)

    kwargs = {
        'brightness': '',
        'primary_colour': '',
        'secondary_colour': ''
    }

    for rstate in RofiState:
        if rstate != state:
            continue

        _, friendly, identifier, themekey = rstate.value
        options = BRIGHTNESS_OPTIONS\
            if rstate == RofiState.Brightness\
            else COLOUR_OPTIONS
        add_options(options)
        if len(selected) > 0:
            rofi_selected_key = identifier

            kwargs[themekey] = strip_html(selected)

            # TODO: This doesn't work properly, work through the logic again
            print('selected: {}'.format(selected), file=sys.stderr)
            print('rstate: {}'.format(rstate), file=sys.stderr)
            print('values: {}'.format(rstate.value), file=sys.stderr)
            print('kwargs: {}'.format(kwargs), file=sys.stderr)
            quick_client().SetTheme(
                kwargs['brightness'],
                kwargs['primary_colour'],
                kwargs['secondary_colour']
            )
        break

    current = client.GetTheme()
    rofi.print_options(
        current[rofi_selected_key]
        if rofi_selected_key in current
        else ''
    )
