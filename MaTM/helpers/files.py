from os import path
import shutil
import typing


def read_lines(filename: str) -> typing.Iterator[str]:
    with open(filename, 'rt') as f:
        lines = [line.rstrip() for line in f]
    return filter(None, lines)


def write_lines(filename: str, lines: typing.Iterable[str]):
    with open(filename, 'wt') as f:
        for line in lines:
            print(line, file=f)


def get_program_path(section, program: str) -> str:
    program_path = section[program] if program in section\
        else shutil.which(program)
    if program_path is not None and\
            len(program_path) > 0 or\
            path.isfile(program_path):
        return program_path
    return None
