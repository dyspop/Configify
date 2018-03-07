"""Test the make module."""

import Configify
import os
import pytest
import json

path = 'tests/'
filename = 'config'
format = 'json'
outpath = '{p}{fn}.{fmt}'.format(p=path, fn=filename, fmt=format)
data = {'spam': 'bacon', 'ham': 'eggs'}
data2 = {'spam': 'baked beans', 'ham': 'sausage'}

def setup_function(function):
    """Set up a new state."""
    pass


def teardown_function(function):
    """Tear down any state that was previously setup with a setup_function call."""
    try:
        os.remove(outpath)
    except OSError:
        pass
    try:
        os.remove('tests/spam.json')
    except OSError:
        pass


def test_args_none():
    """Should return TypeError."""
    with pytest.raises(TypeError):
        Configify.make()


def test_arg_data_none_error():
    """Should return an error if the input data is bad."""
    bad_input_datas = [
        None, False, True,
        1, 0, 0.1, complex('j'),
        [], [0, 1], (), (0, 1),
        range(0), range(1),
        '', 'spam',
        b'', b'spam',
        bytearray(), bytearray(b'\xf0\xf1'),
        {}, {0, 1}
    ]
    with pytest.raises(TypeError):
        for bad_input_data in bad_input_datas:
            Configify.make(data=None)


def test_get_gets_dict(monkeypatch):
    """Should get a dict when we supply the get argument."""
    monkeypatch.setattr('builtins.input', lambda x: "I'll do you for that.")
    assert isinstance(Configify.make(data=data, path=path, get=True), dict)


def test_arg_filename_blank_returns_config(monkeypatch):
    """Should get something called 'config' if there's no argument."""
    monkeypatch.setattr('builtins.input', lambda x: "Spam, spam, spam, spam.")
    assert 'config' in list(Configify.make(data=data, path=path, get=True).keys())[0]


def test_arg_filename_supplied_returns_arg_in_returned_dict(monkeypatch):
    """Should get dict with first key returning the input filename."""
    monkeypatch.setattr('builtins.input', lambda x: "cabbage crates coming over the briny?")
    assert 'spam' in list(Configify.make(
        data=data, get=True, filename='spam', path=path).keys())[0].split('.')[0]


def test_args_filename_and_path_concat_in_returned_dict(monkeypatch):
    """Should combine the args for the file write destination."""
    monkeypatch.setattr('builtins.input', lambda x: "What-ho, Squiffy.")
    assert outpath.split('.')[0] == list(
        Configify.make(
            data=data, get=True, filename=filename, path=path
        ).keys())[0].split('.')[0]


def test_file_creation(monkeypatch):
    """A file should have been created."""
    monkeypatch.setattr('builtins.input', lambda x: "Jolly good. Fire away.")
    Configify.make(data=data, path=path)
    assert os.path.exists(outpath)


def test_file_is_valid_format_json(monkeypatch):
    """We should get a valid json file created."""
    monkeypatch.setattr('builtins.input', lambda x: "sausage squad up the blue end?")
    Configify.make(data=data, path=path)
    assert json.load(open(outpath))


def test_if_file_exists_returns_error(monkeypatch):
    """If there is already a file we should not rewrite it."""
    monkeypatch.setattr('builtins.input', lambda x: "Bunch of monkeys on the ceiling")
    Configify.make(data=data, path=path)
    with pytest.raises(Exception):
        Configify.make(data=data2, path=path)


def test_arg_force_true_results_in_file(monkeypatch):
    """If force is true we should make a file even if there was a file."""
    monkeypatch.setattr('builtins.input', lambda x: "let's get the bacon delivered!")
    Configify.make(data=data, path=path)
    Configify.make(data=data2, path=path, force=True)
    assert os.path.exists(outpath)


def test_arg_force_true_creates_file_with_second_input_data(monkeypatch):
    """The file we made should have the data from the second call."""
    monkeypatch.setattr('builtins.input', lambda x: "Grab your egg-and-fours")
    Configify.make(data=data, path=path)
    Configify.make(data=data2, path=path, force=True)
    assert json.load(open(outpath)) == data2


# def test_make_multiple_entries(monkeypatch):
#     """Do the file keys and values match the input."""
#     monkeypatch.setattr('builtins.input', lambda x: "bar")
#     data = {'foo': 'bar', 'bobs': 'bar'}
#     config = Configify.make(path=path, data=data, get=True, secret=False)
#     config_from_sys = json.load(open(config_file))
#     config_from_test = eval(config[config_file])
#     assert config_from_test == config_from_sys



# Tests for features planned for future releases
# unmark this and write a more complete test
@pytest.mark.xfail
def test_arg_format():
    """The promptcontext argument is not supported yet."""
    assert Configify.make(data=data, path=path, promptcontext=True)


# unmark this and write a more complete test
@pytest.mark.xfail
def test_arg_promptcontext():
    """The promptcontext argument is not supported yet."""
    assert Configify.make(data=data, path=path, promptcontext=True)


# Test pytest itself
def test_teardown_tears_down():
    """If teardown works we should not have a file at this path."""
    assert not os.path.exists(outpath)
