from MaTM.environ import APP_NAME
from MaTM.helpers.rofi.entry import RofiEntry
from MaTM.helpers.rofi.html_stripper import strip_html

from sys import stdout
from typing import List


class RofiPrintHelpers(object):
    def __init__(self):
        raise Exception('Static helper class')

    @staticmethod
    def print_header(key, value, prefix='\0'):
        stdout.write('{}{}\x1f{}\n'.format(prefix, key, value))

    @staticmethod
    def print_header_title(title):
        RofiPrintHelpers.print_header('prompt', title, prefix='\x00')

    @staticmethod
    def print_header_urgent(urgent_idxs):
        RofiPrintHelpers.print_header('urgent', urgent_idxs)

    @staticmethod
    def print_header_active(active_idxs):
        RofiPrintHelpers.print_header('active', active_idxs)

    @staticmethod
    def print_header_message(message):
        RofiPrintHelpers.print_header('message', message)


class Rofi(object):
    prompt_title: str
    message: str
    options: List[RofiEntry]

    def __init__(self, prompt_title=APP_NAME, message=None):
        self.prompt_title = prompt_title
        self.message = message
        self.clear_options()

    def add_option(self, text, value, on_selected):
        self.options.append(RofiEntry(text, value, on_selected))

    def find_entry(self, text):
        text = strip_html(text)
        for i in range(len(self.options)):
            option = self.options[i]
            if option.text == text:
                return i, option
        return -1, None

    def handle_event(self, selectedentry):
        idx, entry = self.find_entry(selectedentry)
        if idx > -1:
            entry.handle_event()

    def clear_options(self):
        self.options = []

    def print_options(self, selectedtext):
        selected_idx, selected_option = self.find_entry(selectedtext)

        ph = RofiPrintHelpers
        ph.print_header_title(self.prompt_title)
        ph.print_header('markup-rows', 'true')
        if selected_idx > -1:
            ph.print_header_urgent(selected_idx)

        if self.message is not None:
            ph.print_header_message(self.message)

        for i in range(len(self.options)):
            option = self.options[i]
            option.print(i == selected_idx)

        stdout.flush()
