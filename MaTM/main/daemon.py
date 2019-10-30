from MaTM.services.daemon import DaemonService
from MaTM.services.dbus import (
    iface_method,
    REV_DOMAIN,
    DBusException,
    DBusObject
)


class MaTMDaemonException(DBusException):
    _dbus_error_name = f"{REV_DOMAIN}.MaTMDaemonException"
    message: str

    def __init__(self, message: str):
        self.message = message


class MatmInterface(DBusObject):
    daemon: DaemonService

    @iface_method
    def SetTheme(self,
                 brightness: str,
                 primary_colour: str,
                 secondary_colour: str):
        tm = self.daemon.theme_manager
        try:
            tm.find_and_apply(
                brightness,
                primary_colour,
                secondary_colour
            )
            return tm.current_theme.to_dict()
        except ValueError as e:
            raise MaTMDaemonException(e.args[0])

    @iface_method
    def GetTheme(self):
        return self.daemon.theme_manager.current_theme.to_dict()

    @iface_method
    def Quit(self):
        print('Quit received')
        self.daemon.main_quit()


def main():
    # Note: os.getppid == 1, running as service
    daemon = DaemonService(MatmInterface)
    daemon.main(True)
