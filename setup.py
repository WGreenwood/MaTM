from os import path
from setuptools import find_packages, setup


NAME = 'MaTM'
DESC = 'Applies a consistent theme to multiple applications'
URL = f'https://github.com/WGreenwood/{NAME}'
AUTHOR = 'Wesley Greenwood'
AUTHOR_EMAIL = 'WesleyFGreenwood@gmail.com'
REQUIRES_PYTHON = '>=3.6.0'
with open('VERSION', 'rt') as f:
    VERSION = f.read()

PLATFORMS = ['posix']
CONSOLE_SCRIPTS = {
    'matm-msg': 'MaTM.main:msg',
    'matm-prompt': 'MaTM.main:rofi_mode',
    'matm-daemon': 'MaTM.main:daemon'
}

# Nothing should be put in this list, they should be listed in PKGBUILD.template
INSTALL_REQUIRES = []
# Dev/Testing can be used, it is run in a virtual environment
DEV_REQUIRES = [
    'flake8',
    'rope',
    'autopep8',
    'pydeps'
]
TESTING_REQUIRES = [
    'pytest',
    'coverage',
]


def read_long_desc():
    here = path.abspath(path.dirname(__file__))
    try:
        with open(path.join(here, 'README.md'), encoding='utf-8') as f:
            return '\n' + f.read()
    except FileNotFoundError:
        return DESC


kwargs = {
    'name': NAME,
    'version': VERSION,
    'description': DESC,
    'long_description': read_long_desc(),
    'long_description_content_type': 'text/markdown',
    'author': AUTHOR,
    'author_email': AUTHOR_EMAIL,
    'url': URL,
    'packages': find_packages(exclude=['docs', 'tests']),
    'install_requires': INSTALL_REQUIRES,
    'platforms': PLATFORMS,
}

EXTRAS_REQUIRE = {}
if DEV_REQUIRES is not None:
    EXTRAS_REQUIRE['dev'] = DEV_REQUIRES
if TESTING_REQUIRES is not None:
    EXTRAS_REQUIRE['testing'] = TESTING_REQUIRES
kwargs['extras_require'] = EXTRAS_REQUIRE

if CONSOLE_SCRIPTS is not None:
    kwargs['entry_points'] = {
        'console_scripts': [f"{k}={v}" for k, v in CONSOLE_SCRIPTS.items()]
    }

setup(**kwargs)
