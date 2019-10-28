from argparse import ArgumentParser
from os import path
import sys
import typing


def split_args(argv: typing.List[str] = None)\
        -> typing.Tuple[str, typing.List[str]]:
    if argv is None:
        argv = sys.argv
    return path.basename(argv[0]), argv[1:]


def parse_msg_args(commands, argv: typing.List[str] = None):
    def add_parser(subparser, name, help):
        return subparser.add_parser(
            name,
            help=help,
            description=help
        )

    prog, args = split_args(argv)
    parser = ArgumentParser(
        prog=prog,
        description='Sends dbus messages to the matm-daemon'
    )
    subparsers = parser.add_subparsers()

    quit_parser = add_parser(subparsers, 'quit', 'Quits the matm-daemon')
    quit_parser.set_defaults(func=commands.quit_daemon)

    def add_get_cmd():
        get_parser = add_parser(
            subparsers, 'get',
            'Gets various properties from the daemon'
        )
        get_subparsers = get_parser.add_subparsers()

        def add_get_parser(func, name, help):
            add_parser(
                get_subparsers, name, help
            ).set_defaults(func=func)

        add_get_parser(
            commands.get_theme, 'theme',
            'Gets the current theme'
        )
        add_get_parser(
            commands.get_colours, 'colours',
            'Gets the list of material colours from the daemon'
        )
        add_get_parser(
            commands.get_brightnesses, 'brightness',
            'Gets the list of brightness values from the daemon'
        )
    add_get_cmd()

    def add_set_cmd():
        set_parser = add_parser(
            subparsers, 'set',
            'Sets properties in matm-daemon'
        )
        set_subparsers = set_parser.add_subparsers()

        theme_set_parser = add_parser(
            set_subparsers, 'theme',
            'Sets the current theme in matm-daemon'
        )

        theme_set_parser.set_defaults(func=commands.set_theme)
        theme_set_parser.add_argument(
            '-p', '--primary-colour',
            action='store',
            help='The primary colour of the theme'
        )
        theme_set_parser.add_argument(
            '-s', '--secondary-colour',
            action='store',
            help='The secondary colour of the theme'
        )
        theme_set_parser.add_argument(
            '-b', '--brightness',
            action='store',
            help='The brightness of the theme'
        )
    add_set_cmd()

    parsed_args = parser.parse_args(args)
    if hasattr(parsed_args, 'func'):
        func = parsed_args.func
        del parsed_args.func
        if func(parsed_args):
            return
    parser.print_help()
