import typing


def read_lines(filename: str) -> typing.List[str]:
    with open(filename, 'rt') as f:
        lines = [line.rstrip() for line in f]
    return filter(None, lines)


def write_lines(filename: str, lines: typing.List[str]):
    with open(filename, 'wt') as f:
        for line in lines:
            print(line, file=f)
