from MaTM.main.args import parse_msg_args
from MaTM.main.daemon import MatmInterface
from enum import Enum


class MsgCommand(Enum):
    LIST_CMDS = 'list-cmds'
    GET_THEME = 'get-theme'
    QUIT = 'quit'
    HELP_DICT = {
        LIST_CMDS: 'List all available commands',
        GET_THEME: '',
        QUIT: 'Quit the matm daemon'
    }


def get_iface() -> MatmInterface:
    from MaTM.services.dbus import DbusService
    return DbusService().as_client().iface


CMD_FUNC_LIST = {
    MsgCommand.LIST_CMDS: lambda: [
        print('  {}:  {}'.format(c.value, MsgCommand.HELP_DICT.value[c.value]))
        for c in MsgCommand
        if c != MsgCommand.HELP_DICT
    ],
    MsgCommand.GET_THEME: lambda: [
        print('  {}: {}'.format(k.rjust(16), v))
        for k, v in get_iface().GetTheme().items()
    ],
    MsgCommand.QUIT: lambda: get_iface().Quit()
}


def main():
    args = parse_msg_args()
    cmd = MsgCommand(args.command)
    CMD_FUNC_LIST[cmd]()
