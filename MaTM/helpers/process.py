import os
import subprocess
import typing


def get_output(args: typing.List[str]):
    return subprocess.check_output(args)\
        .decode('utf-8').rstrip()


def get_list_output(args: typing.List[str]) -> typing.List[str]:
    return list(filter(
        None,
        get_output(args).split('\n')
    ))


def run(args: typing.List[str], stdin: str = '')\
        -> subprocess.CompletedProcess:
    kwargs = {
        'stdout': subprocess.PIPE,
        'stderr': subprocess.PIPE,
        'universal_newlines': True,
    }
    if len(stdin) > 0:
        kwargs['input'] = stdin
    return subprocess.run(args, **kwargs)


def call(args: typing.List[str], hide_output=True) -> int:
    kwargs = {}
    if hide_output:
        dnull = open(os.devnull, 'wt')
        kwargs['stdout'] = dnull
        kwargs['stderr'] = dnull
    return subprocess.call(
        args,
        **kwargs
    )
