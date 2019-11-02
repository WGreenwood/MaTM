from MaTM.helpers import environ
from MaTM.helpers.rofi.menu import RofiMenu
from MaTM.theming.colours import Brightness, MaterialColours
from MaTM.services.dbus import quick_client

from enum import Enum


class MainMenuChoice(Enum):
    All = 'Change All'
    Brightness = 'Change Brightness'
    PrimaryAccent = 'Change Primary Accent Colour'
    SecondaryAccent = 'Change Secondary Accent Colour'


def get_main_menu() -> RofiMenu:
    menu = RofiMenu(environ.APP_NAME, 'What would you like to change?')
    for choice in MainMenuChoice:
        menu.add_option(choice.value, choice)
    return menu


def get_brightness_menu() -> RofiMenu:
    menu = RofiMenu(environ.APP_NAME, 'Select a new brightness')
    for b in Brightness:
        menu.add_option(b.name, b)
    return menu


def get_colour_menu() -> RofiMenu:
    menu = RofiMenu(environ.APP_NAME)
    for colour in MaterialColours.ALL.values():
        menu.add_option(colour.name, colour)
    return menu


def main():
    client = quick_client()
    current_theme = client.GetTheme()

    main_menu = get_main_menu()
    while True:
        main_menu.show('')
        if main_menu.selected_option is None:
            return
        choice: MainMenuChoice = main_menu.selected_option.tag
        is_all = choice == MainMenuChoice.All

        brightness_choice = ''
        primary_choice = ''
        secondary_choice = ''

        brightness_menu = get_brightness_menu()
        colour_menu = get_colour_menu()

        def show_menu(menu: RofiMenu, special_item: str, msg: str = '') -> str:
            if len(msg) > 0:
                menu.message = msg
            menu.show(special_item)
            if menu.selected_option is None:
                return None
            return menu.selected_option.text

        if is_all or choice == MainMenuChoice.Brightness:
            brightness_choice = show_menu(
                brightness_menu,
                current_theme['brightness']
            )
            if brightness_choice is None:
                return

        if is_all or choice == MainMenuChoice.PrimaryAccent:
            primary_choice = show_menu(
                colour_menu,
                current_theme['primary-colour'],
                'Select a new primary accent colour'
            )
            if primary_choice is None:
                return

        if is_all or choice == MainMenuChoice.SecondaryAccent:
            secondary_choice = show_menu(
                colour_menu,
                current_theme['secondary-colour'],
                'Select a new secondary accent colour'
            )
            if secondary_choice is None:
                return

        choices = [brightness_choice, primary_choice, secondary_choice]
        if any(map(lambda s: len(s) > 0, choices)):
            client.SetTheme(
                brightness_choice,
                primary_choice,
                secondary_choice
            )
        if choice == MainMenuChoice.All:
            return
