from MaTM.main.args import parse_msg_args
from MaTM.main.daemon import MatmInterface
from enum import Enum


class MsgCommand(Enum):
    LISTCMDS = 'listcmds'
    QUIT = 'quit'
    HELP_DICT = {
        LISTCMDS: 'List all available commands',
        QUIT: 'Quit the matm daemon'
    }


def get_iface() -> MatmInterface:
    from MaTM.services.dbus import DbusService
    return DbusService().as_client().iface


CMD_FUNC_LIST = {
    MsgCommand.LISTCMDS: lambda: [
        print('  {}:  {}'.format(c.value, MsgCommand.HELP_DICT.value[c.value]))
        for c in MsgCommand
        if c != MsgCommand.HELP_DICT
    ],
    MsgCommand.QUIT: lambda: get_iface().Quit()
}


def main():
    args = parse_msg_args()
    cmd = MsgCommand(args.command)
    CMD_FUNC_LIST[cmd]()
