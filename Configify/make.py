"""Actually makes the configuration file."""

import json


def make(filename='config.json', path='', data={}):
    """Make a file at the system path specified, or where run from."""
    path_and_name = '{p}{f}'.format(p=path, f=filename)
    config = open(path_and_name, 'w')
    config.write(str(data))
    return path_and_name