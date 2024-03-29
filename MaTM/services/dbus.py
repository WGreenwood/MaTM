import dbus
import dbus.service
import dbus.mainloop.glib

from dbus import DBusException
from dbus.service import Object as DBusObject  # noqa:F401

import functools
from sys import stderr

dbus.mainloop.glib.DBusGMainLoop(set_as_default=True)
REV_DOMAIN = 'com.github.WGreenwood'


class MatmServiceException(DBusException):
    _dbus_error_name = f"{REV_DOMAIN}.MamtServiceException"


class DbusService(object):
    UNKNOWN_SVC_NAME = 'org.freedesktop.DBus.Error.ServiceUnknown'
    SVC_NAME = f"{REV_DOMAIN}.MaTMService"
    IFACE_NAME = f"{REV_DOMAIN}.MaTMInterface"
    IFACE_PATH = '/Service'

    session_bus: dbus.SessionBus
    bus_name: dbus.service.BusName
    iface: dbus.service.Object

    def __init__(self):
        self.session_bus = dbus.SessionBus()

    def as_server(self, iface_class):
        self.name = dbus.service.BusName(
            self.SVC_NAME,
            self.session_bus
        )
        self.iface = iface_class(self.session_bus, self.IFACE_PATH)
        return self

    def as_client(self):
        try:
            bus_obj = self.session_bus.get_object(
                self.SVC_NAME,
                self.IFACE_PATH
            )
        except dbus.DBusException as e:
            if e.get_dbus_name() == self.UNKNOWN_SVC_NAME:
                print('No MaTM dbus service was located', file=stderr)
            else:
                print(e, file=stderr)
            exit(1)
        self.iface = dbus.Interface(bus_obj, self.IFACE_NAME)
        return self


def quick_client():
    return DbusService().as_client().iface


def iface_method(view):
    @dbus.service.method(DbusService.IFACE_NAME)
    @functools.wraps(view)
    def _wrapped_iface_method(*args, **kwargs):
        return view(*args, **kwargs)
    return _wrapped_iface_method
