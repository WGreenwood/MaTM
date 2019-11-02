from MaTM.helpers import environ
from MaTM.helpers.rofi.menu import RofiMenu
from MaTM.theming.colours import Brightness, MaterialColours
from MaTM.services.dbus import quick_client

from enum import Enum


def get_main_menu() -> RofiMenu:
    menu = RofiMenu(environ.APP_NAME, 'What would you like to change?')
    for choice in MainMenuChoice:
        menu.add_option(choice.value[0], choice)
    return menu


def get_brightness_menu() -> RofiMenu:
    menu = RofiMenu(environ.APP_NAME)
    for b in Brightness:
        menu.add_option(b.name, b)
    return menu


def get_colour_menu() -> RofiMenu:
    menu = RofiMenu(environ.APP_NAME)
    for colour in MaterialColours.ALL.values():
        menu.add_option(colour.name, colour)
    return menu


class MainMenuChoice(Enum):
    All = ('Everything',)
    Brightness = (
        'Brightness',
        'Select a new brightness',
        'brightness',
        get_brightness_menu,
    )
    PrimaryAccent = (
        'Primary accent colour',
        'Select a new primary colour',
        'primary-colour',
        get_colour_menu,
    )
    SecondaryAccent = (
        'Secondary accent colour',
        'Select a new secondary ary colour',
        'secondary-colour',
        get_colour_menu,
    )
    @staticmethod
    def get_choices():
        yield MainMenuChoice.Brightness
        yield MainMenuChoice.PrimaryAccent
        yield MainMenuChoice.SecondaryAccent


def main():
    client = quick_client()
    current_theme = client.GetTheme()

    main_menu = get_main_menu()
    while True:
        main_menu.show('')
        if main_menu.selected_option is None:
            return
        user_choice: MainMenuChoice = main_menu.selected_option.tag
        is_all = user_choice == MainMenuChoice.All

        theme_choices = {}

        brightness_menu = get_brightness_menu()
        colour_menu = get_colour_menu()

        for choice in MainMenuChoice.get_choices():
            _, msg, key, func = choice.value
            if is_all or user_choice == choice:
                menu = brightness_menu\
                    if func == get_brightness_menu\
                    else colour_menu
                menu.message = msg
                special_item = current_theme[key]
                menu.show(special_item)
                if menu.selected_option is None:
                    return
                theme_choices[key] = menu.selected_option.text
            else:
                theme_choices[key] = ''

        if any(map(lambda s: len(s) > 0, theme_choices.values())):
            current_theme = client.SetTheme(
                theme_choices['brightness'],
                theme_choices['primary-colour'],
                theme_choices['secondary-colour'],
            )

        if choice == MainMenuChoice.All:
            return
