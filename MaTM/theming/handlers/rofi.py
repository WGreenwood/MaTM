import itertools
from os import path

from MaTM.helpers import files
from MaTM.theming import AppThemeManager, ThemeManager


class RofiThemeHandler(AppThemeManager):
    __appname__ = 'rofi'
    template_path: str
    output_path: str

    def __init__(self):
        super().__init__()

    def on_config_loaded(self, manager: ThemeManager):
        CFG_KEY = RofiThemeHandler.__appname__
        cfg = manager.config
        section = cfg[CFG_KEY] if CFG_KEY in cfg else {}

        TEMPLATE_KEY = 'template'
        OUTPUT_KEY = 'output'
        if TEMPLATE_KEY not in section or OUTPUT_KEY not in section:
            # TODO: Add log statement here to inform user
            self.is_active = False
            return

        self.template_path = section[TEMPLATE_KEY]
        self.output_path = section[OUTPUT_KEY]
        self.is_active = path.isfile(self.template_path)

    def on_startup(self, manager: ThemeManager):
        pass

    def on_apply_theme(self, manager: ThemeManager):
        template = files.read_lines(self.template_path)
        theme = manager.current_theme

        colourbase = theme.brightness.to_accent_idx()
        primary = theme.primary_colour
        secondary = theme.secondary_colour

        scrollbar = primary[colourbase+200]
        borders = primary[colourbase]

        prompt = primary[colourbase+200]
        prompt_text = prompt.get_text_colour()

        selected_bg = secondary[colourbase]
        selected_fg = selected_bg.get_text_colour()

        inidata = {
            'background': theme.background,
            'foreground': theme.foreground,

            'scrollbar': scrollbar,
            'borders': borders,

            'prompt': prompt,
            'prompt-text': prompt_text,

            'normal-element-background': theme.background,
            'normal-element-foreground': theme.foreground,
            'selected-element-background': selected_bg,
            'selected-element-foreground': selected_fg,
        }

        lines = ['* {']
        for k, v in inidata.items():
            lines.append("  {}: {};".format(k, v.to_hex()))
        lines.append('}')

        with open(self.output_path, 'wt') as f:
            for line in itertools.chain(lines, template):
                f.write(line)
                f.write('\n')
