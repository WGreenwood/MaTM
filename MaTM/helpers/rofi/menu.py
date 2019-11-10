import typing

from MaTM.helpers import process

from MaTM.helpers.rofi.item import RofiMenuItem
from MaTM.helpers.rofi.html_stripper import strip_html


class RofiMenu(object):
    DEFAULT_SPECIAL_ATTRIBS = {
        'weight': 'heavy',
        'underline': 'single'
    }

    title: str
    message: str
    location: int
    yoffset: int
    xoffset: int
    sort: bool
    levenshtein_sort: bool
    options: typing.List[RofiMenuItem]
    selected_option: typing.Union[None, RofiMenuItem]
    special_attribs: typing.Dict[str, str]

    def __init__(self,
                 title: str,
                 message: str = '',
                 location: int = 2,
                 yoffset: int = 100,
                 xoffset: int = 0,
                 special_attribs: typing.Dict[str, str] = None):
        self.title = title
        self.message = message
        self.location = location
        self.yoffset = yoffset
        self.xoffset = xoffset
        self.sort = True
        self.levenshtein_sort = False
        self.options = []
        self.special_attribs = special_attribs or\
            RofiMenu.DEFAULT_SPECIAL_ATTRIBS
        self.reset_state()

    def add_option(self, text: str,
                   tag: typing.Any = None,
                   selected: typing.Callable = None) -> RofiMenuItem:
        item = RofiMenuItem(text, tag)
        item.add_on_selected(selected)
        self.options.append(item)
        return item

    def reset_state(self):
        self.selected_option = None

    def show(self, special_item: str):
        self.reset_state()
        output = self._run_rofi(special_item)
        if len(output) == 0:
            return
        output = strip_html(output)
        for item in self.options:
            if item.text != output:
                continue
            self.selected_option = item
            item.call_on_selected()
            break

    def _run_rofi(self, special_item: str):
        special_item = special_item or ''

        sort = '-sort'
        levenshtein_sort = '-levenshtein-sort'
        if not self.sort:
            sort = '-no' + sort
        if not self.levenshtein_sort:
            levenshtein_sort = '-no' + levenshtein_sort

        args = [
            'rofi',
            '-location', str(self.location),
            '-yoffset', str(self.yoffset),
            '-xoffset', str(self.xoffset),

            '-dmenu', '-markup-rows', '-i',
            sort, levenshtein_sort,
            '-p', self.title
        ]
        if len(self.message) > 0:
            args.append('-mesg')
            args.append(self.message)

        option_text = '\n'.join(map(
            lambda c: c.format_item(
                self.special_attribs if c.text == special_item
                else {}
            ),
            self.options
        ))
        return process.run(args, option_text).stdout.rstrip()
