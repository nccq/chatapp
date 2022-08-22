from jinja2 import Undefined


def _slice(iterable, pattern):

    if iterable is None or isinstance(iterable, Undefined):
        return iterable


    items = str(iterable)

    start = None
    end = None
    stride = None


    if pattern:
        tokens = pattern.split(':')
        print(tokens)
        if len(tokens) > 1:
            start = int(tokens[0])
        if len(tokens) > 2:
            end = int(tokens[1])
        if len(tokens) > 3:
            stride = int(tokens[2])

    return items[start:end:stride]