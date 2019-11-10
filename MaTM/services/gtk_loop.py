import contextlib

import gi
gi.require_version('Gtk', '3.0')

from gi.repository import Gtk  # noqa:E402


class GtkLoop(object):
    def __init__(self):
        pass

    def start(self, suppress_kb_interrupt=True):
        with contextlib.suppress(KeyboardInterrupt) if suppress_kb_interrupt\
                else contextlib.nullcontext():
            Gtk.main()

    def end(self):
        Gtk.main_quit()
