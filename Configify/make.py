"""Actually makes the configuration file.

Configify  Copyright (C) 2018  Dan Black
    This program comes with ABSOLUTELY NO WARRANTY; 
    This is free software, and you are welcome to redistribute it
    under certain conditions; For details see license.txt

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""



import json
import getpass
import sys


def __obscure(string, char='*'):
    """Obscure the data for display."""
    return char * len(string)


def __generate_config_dict(template, secret, filename, char):
    """Generate a json config at the system path based on the template dict."""
    # Don't do stuff unless we got a dict
    if isinstance(template, dict):
        new_config = {}
        # loop through key-value pairs
        for k, v in template.items():
            # check if we're in the secret state
            if secret is True:
                # set the function to call user input
                func = getpass.getpass
                # check that there's a default
                if v != ('' or None or False):
                    # if there is then prompt with the default but obscured
                    prompt = "Enter value for \"{k}\"\n(return for default \"{v}\")': ".format(
                        k=k, v=__obscure(v, char))
                else:
                    # but if there isn't one then obviously don't try to display it
                    prompt = "'{k}: ".format(k=k)
            # if we're not handling secrets
            else:
                # just use normal input
                func = input
                # and don't obscure the default values
                prompt = "Enter value for \"{k}\"\n(return for default \"{v}\")': ".format(
                    k=k, v=v)
            # print the prompt
            print(prompt)
            # set the value of the user input, if not to the default
            new_config[k] = func() or v
            # check secretness again, if so set the new value's display version to be obscured
            if secret is True:
                v_display = __obscure(new_config[k], char)
            # if not don't obscure it
            else:
                v_display = new_config[k]
            # print the results, but delete the extra line from the user if they entered the default
            if v == new_config[k]:
                print('\033[F')
            print("Set \"{k}\" to \"{v}\" in {f}".format(k=k, v=v_display, f=filename))
            return new_config
    else:
        return None


def make(
        data={},
        filename='config.json',
        path='',
        secret=True,
        get=False,
        char='*'
    ):
    """Make a file at the system path specified, or where run from."""
    # set the data to the return of our generator with all the user options passed through
    data = __generate_config_dict(template=data, secret=secret, filename=filename, char=char)
    # format the save destination
    path_and_name = '{p}{f}'.format(p=path, f=filename)
    # write the actual config file
    config = open(path_and_name, 'w')
    # format the data as json
    data = json.dumps(data)
    # write the json data to the file
    config.write(str(data))
    if get is True:
        # return the data only if the user wants it
        if sys.stdout.isatty() and secret is True:
            # but not to terminal when secret of course
            pass
        else:
            return {path_and_name: data}
    else:
        # don't return by default after we've gone through all that trouble to obscure things.
        pass
