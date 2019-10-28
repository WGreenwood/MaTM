import dbus  # noqa:E403
from dbus.service import Object as DbusObject  # noqa:E403

from MaTM.services.daemon import DaemonService  # noqa:E403
from MaTM.services.dbus import iface_method, REV_DOMAIN  # noqa:E403,E501


class MaTMDaemonException(dbus.DBusException):
    _dbus_error_name = f"{REV_DOMAIN}.MaTMDaemonException"


class MatmInterface(DbusObject):
    daemon: DaemonService

    @iface_method
    def GetTheme(self):
        t = self.daemon.theme_manager.current_theme
        print('Get Theme Received: {}'.format(t))
        return t.to_dict()

    @iface_method
    def Quit(self):
        print('Quit received')
        self.daemon.main_quit()


def main():
    daemon = DaemonService(MatmInterface)
    daemon.main(True)
