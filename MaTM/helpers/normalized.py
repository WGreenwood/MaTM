
def name(name: str) -> str:
    name = name.lower()
    for c in [' ', '-']:
        name = name.replace(c, '_')
    return name


def find(keyvalues: dict, key: str):
    key = name(key)
    for k, v in keyvalues.items():
        normalk = name(k)
        if normalk == key:
            return v
    return None
