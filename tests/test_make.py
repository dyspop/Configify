import Configify
import os
import pytest
import json

path = 'tests/'
filename = 'config.json'

def test_make_makes_json_at_path():
    """Did the json file get made at the path we said."""
    Configify.make(path=path)
    config_file = '{p}{f}'.format(p=path, f=filename)
    assert open(config_file, 'r')
    os.remove(config_file)


def test_switching_inputs_returns_error():
    """If we switch params does it fail with the right error."""
    Configify.make(path=path)
    config_file = '{f}{p}'.format(p=path, f=filename)
    with pytest.raises(FileNotFoundError):
        open(config_file, 'r')


def test_make_makes_json_file_by_eof():
    """Did the json file we wrote end in .json."""
    assert list(
        Configify.make(path=path, get=True).keys()
    )[0].endswith('.json')
    os.remove('{p}{f}'.format(p=path, f=filename))


def test_make_makes_json_actually():
    """Did the file we wrote actually become json."""
    Configify.make(path=path, data={"foo": "bar"})
    config_file = '{p}{f}'.format(p=path, f=filename)
    assert json.load(open(config_file))
    os.remove(config_file)