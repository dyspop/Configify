"""Actually makes the configuration file."""

import json
import getpass
import sys


def __obscure(string):
    """Obscure the data for display."""
    deplorables = ["[", "]", "'", ",", " "]
    obscured = str(['*' for char in string])
    for deplorable in deplorables:
        obscured = obscured.replace(deplorable, '')
    return obscured


def __generate_config_dict(template, secret, filename):
    """Generate a json config at the system path based on the template dict."""
    new_config = {}
    for k, v in template.items():
        if secret is True:
            func = getpass.getpass
        else:
            func = input
        new_config[k] = func("'{k}': ".format(k=k)) or v
        if secret is True:
            v = __obscure(new_config[k])
        else:
            v = new_config[k]
        print("Set {k} to {v} in {f}".format(k=k, v=v, f=filename))
        return new_config


def make(data={}, filename='config.json', path='', secret=True, get=False):
    """Make a file at the system path specified, or where run from."""
    data = __generate_config_dict(template=data, secret=secret, filename=filename)
    path_and_name = '{p}{f}'.format(p=path, f=filename)
    config = open(path_and_name, 'w')
    data = json.dumps(data)
    config.write(str(data))
    if get is True:
        return {path_and_name: data}
    else:
        pass
