from argparse import ArgumentParser
import sys
import typing


class MatmMsgArguments(object):
    command: str

    def __init__(self, args):
        self.command = args.command


def _cut_args(argv: typing.List[str])\
        -> typing.Tuple[str, typing.List[str]]:
    return argv[0], argv[1:]


def parse_msg_args(argv=None):
    from MaTM.main.msg import MsgCommand
    prog, args = _cut_args(argv or sys.argv)

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
