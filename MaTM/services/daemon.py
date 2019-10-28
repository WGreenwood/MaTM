import gi
gi.require_version('Gtk', '3.0')

from gi.repository import Gtk  # noqa:E402

from MaTM.services.dbus import DbusService  # noqa:E402
from MaTM.theming import create_default_manager, ThemeManager  # noqa:E402


class DaemonService(object):
    dbus: DbusService
    theme_manager: ThemeManager

    def __init__(self, iface_class):
        self.dbus = DbusService().as_server(iface_class)
        self.dbus.iface.daemon = self
        self.theme_manager = create_default_manager()

    def main(self, suppress_kb_interrupt=True):
        print('Starting daemon')
        import contextlib
        with contextlib.suppress(KeyboardInterrupt) if suppress_kb_interrupt\
                else contextlib.nullcontext():
            Gtk.main()
        print('\nDaemon shutting down')

    def main_quit(self):
        Gtk.main_quit()
