import typing


class RofiMenuItem(object):
    text: str
    tag: typing.Any
    _on_selected: typing.Callable

    def __init__(self, text: str, tag: typing.Any):
        self.text = text
        self.tag = tag
        self.span_attrs = {}
        self._on_selected = None

    def add_on_selected(self, selected: typing.Callable):
        self._on_selected = selected

    def call_on_selected(self):
        if self._on_selected is not None:
            self._on_selected(self)

    def format_item(self, span_attribs: typing.Dict[str, str]) -> str:
        if len(span_attribs) == 0:
            return self.text
        return '<span {}>{}</span>'.format(
            ' '.join([
                '{}="{}"'.format(k, v)
                for k, v in span_attribs.items()
            ]),
            self.text
        )
