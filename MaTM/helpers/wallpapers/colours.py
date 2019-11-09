import random
# Copied from https://github.com/alexwlchan/specktre


def random_colours(start, end):
    d_red = (start.red - end.red)
    d_green = (start.green - end.green)
    d_blue = (start.blue - end.blue)
    while True:
        chosen_d = random.uniform(0, 1)
        yield (
            start.red - int(d_red * chosen_d),
            start.green - int(d_green * chosen_d),
            start.blue - int(d_blue * chosen_d)
        )
