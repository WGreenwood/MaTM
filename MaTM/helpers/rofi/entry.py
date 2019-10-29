from typing import Callable


class RofiEntry(object):
    text: str
    value: object
    on_selected: Callable

    def __init__(self, text: str, value: object, on_selected: Callable):
        self.text = text
        self.value = value
        self.on_selected = on_selected

    def handle_event(self):
        if self.on_selected is not None:
            self.on_selected()

    def print(self, is_selected: bool):
        SELECTED_FORMAT = '<span weight="heavy">{}</span>'
        print(
            SELECTED_FORMAT.format(self.text)
            if is_selected else self.text
        )
