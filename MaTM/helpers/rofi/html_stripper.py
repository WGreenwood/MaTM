from html.parser import HTMLParser
from typing import List


class HtmlStripper(HTMLParser):
    data: List[str]

    def __init__(self):
        super().__init__()
        self.reset()
        self.data = []

    def handle_data(self, data):
        self.data.append(data)

    def get_output(self):
        return ''.join(self.data)


def strip_html(input: str) -> str:
    p = HtmlStripper()
    p.feed(input)
    return p.get_output()
