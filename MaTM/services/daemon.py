from MaTM.services.gtk_loop import GtkLoop
from MaTM.services.dbus import DbusService
from MaTM.theming import create_default_manager, ThemeManager


class DaemonService(object):
    dbus: DbusService
    theme_manager: ThemeManager
    main_loop: GtkLoop

    def __init__(self, iface_class):
        self.dbus = DbusService().as_server(iface_class)
        self.dbus.iface.daemon = self
        self.theme_manager = create_default_manager()
        self.main_loop = GtkLoop()

    def main(self, suppress_kb_interrupt=True):
        print('Starting daemon')
        self.theme_manager.on_startup()
        self.main_loop.start(suppress_kb_interrupt)
        print('\nDaemon shutting down')

    def main_quit(self):
        self.theme_manager.save_config()
        self.main_loop.end()
