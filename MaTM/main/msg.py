from MaTM.main.args import parse_msg_args
from MaTM.services.dbus import quick_client
from MaTM.services.gtk_loop import GtkLoop


class MatmMsgCommands(object):
    def _print_theme_response(self, theme):
        for k, v in theme.items():
            print('{}: {}'.format(k.rjust(16), v))

    def set_theme(self, args):
        if args.brightness is None\
                and args.primary_colour is None\
                and args.secondary_colour is None:
            print('A brightness, primary, or secondary colour is required\n')
            return False

        loop = GtkLoop()

        def handle_reply(theme):
            self._print_theme_response(theme)
            loop.end()

        def handle_error(e):
            print('Error: {}'.format(e.args[0]))
            loop.end()

        quick_client().SetTheme(
            args.brightness or '',
            args.primary_colour or '',
            args.secondary_colour or '',
            reply_handler=handle_reply,
            error_handler=handle_error
        )
        loop.start()
        return True

    def get_theme(self, args):
        loop = GtkLoop()

        def handle_reply(theme):
            self._print_theme_response(theme)
            loop.end()

        def handle_error(e):
            loop.end()

        quick_client().GetTheme(
            reply_handler=handle_reply,
            error_handler=handle_error
        )
        loop.start()
        return True

    def get_colours(self, args):
        print('get colours')
        print('args: {}'.format(args))
        return True

    def get_brightnesses(self, args):
        print('get brightnesses')
        print('args: {}'.format(args))
        return True

    def quit_daemon(self, args):
        quick_client().Quit()
        return True


def main(argv=None):
    cmds = MatmMsgCommands()
    parse_msg_args(cmds, argv)
