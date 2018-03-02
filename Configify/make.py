"""Actually makes the configuration file."""

import json


def __generate_config_dict(template):
    """Generate a json config at the system path based on the template dict."""
    new_config = {}
    for k, v in template.items():
        new_config[k] = input(
            "'{k}' (default '{v}'   ): ".format(k=k, v=v)
        ) or v
        if new_config[k] == v:
            print("Added '{k}': {v} to {t}".format(
                k=k, v=v, t=str('').replace('_template', '')))
    return new_config


def make(filename='config.json', path='', data={}):
    """Make a file at the system path specified, or where run from."""
    __generate_config_dict(template=data)
    path_and_name = '{p}{f}'.format(p=path, f=filename)
    config = open(path_and_name, 'w')
    data = json.dumps(data)
    config.write(str(data))
    return {path_and_name: data}
