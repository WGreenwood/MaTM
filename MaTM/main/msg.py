from MaTM.main.args import parse_msg_args
from MaTM.main.daemon import MatmInterface
from enum import Enum


class MsgCommand(Enum):
    LIST_CMDS = 'list-cmds'
    GET_THEME = 'get-theme'
    SET_THEME = 'set-theme'
    QUIT = 'quit'
    HELP_DICT = {
        LIST_CMDS: 'List all available commands',
        GET_THEME: 'Gets the current theme',
        SET_THEME: 'Sets the current theme',
        QUIT: 'Quit the matm daemon'
    }


def get_iface() -> MatmInterface:
    from MaTM.services.dbus import DbusService
    return DbusService().as_client().iface


def cmd_list_commands():
    def not_help_dict(c):
        return c is not MsgCommand.HELP_DICT

    for c in filter(not_help_dict, MsgCommand):
        helptext = MsgCommand.HELP_DICT.value[c.value]
        print('{}:  {}'.format(c.value.rjust(10), helptext))


def cmd_get_theme():
    [
        print('  {}: {}'.format(k.rjust(16), v))
        for k, v in get_iface().GetTheme().items()
    ]


CMD_FUNC_LIST = {
    MsgCommand.LIST_CMDS: cmd_list_commands,
    MsgCommand.GET_THEME: cmd_get_theme,
    MsgCommand.QUIT: lambda: get_iface().Quit()
}


def main():
    args = parse_msg_args()
    cmd = MsgCommand(args.command)
    CMD_FUNC_LIST[cmd]()
