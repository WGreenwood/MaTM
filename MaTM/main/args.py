from argparse import ArgumentParser
import sys
import typing


class MatmMsgArguments(object):
    command: str

    def __init__(self, args):
        self.command = args.command


def split_args(argv: typing.List[str] = None)\
        -> typing.Tuple[str, typing.List[str]]:
    if argv is None:
        argv = sys.argv
    return argv[0], argv[1:]


def parse_msg_args(argv: typing.List[str] = None):
    from MaTM.main.msg import MsgCommand
    prog, args = split_args(argv)

    parser = ArgumentParser(
        prog=prog,
        description='Sends a message to the MaTM daemon'
    )

    parser.add_argument(
        'command',
        action='store',
        choices=[c for c in MsgCommand.HELP_DICT.value.keys()],
        help='Specifies which command to send'
    )

    return MatmMsgArguments(parser.parse_args(args))
