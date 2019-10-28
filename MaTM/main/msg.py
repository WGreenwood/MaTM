import dbus
from MaTM.main.args import parse_msg_args


def get_iface():
    from MaTM.services.dbus import DbusService
    return DbusService().as_client().iface


class MatmMsgCommands(object):
    def __init__(self):
        pass

    def _print_theme_response(self, theme):
        for k, v in theme.items():
            print('{}: {}'.format(k.rjust(16), v))

    def set_theme(self, args):
        if args.brightness is None\
                and args.primary_colour is None\
                and args.secondary_colour is None:
            print('A brightness, primary, or secondary colour is required')
            return
        try:
            theme = get_iface().SetTheme(
                args.brightness or '',
                args.primary_colour or '',
                args.secondary_colour or ''
            )
            self._print_theme_response(theme)
        except dbus.DBusException as e:
            print('Error: {}'.format(e.args[0]))

    def get_theme(self, args):
        theme = get_iface().GetTheme()
        self._print_theme_response(theme)

    def get_colours(self, args):
        print('get colours')
        print('args: {}'.format(args))

    def get_brightnesses(self, args):
        print('get brightnesses')
        print('args: {}'.format(args))

    def quit_daemon(self, args):
        get_iface().Quit()


def main(argv=None):
    cmds = MatmMsgCommands()
    parse_msg_args(cmds, argv)
