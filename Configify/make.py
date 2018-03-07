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
import os.path


valid_contexts = {'tty': input}


def __generate_file(data, outpath, format):
    """Generate the file."""
    f = open(outpath, 'w')
    f.write(str(json.dumps(data)))


def __validate_context(context):
    if context.lower() in valid_contexts.keys():
        return True
    else:
        return False


def __prompt(context, template):
    """Prompt the user for input from a context (TTY, app, SMS, API etc)."""
    new_config = {}
    # loop through key-value pairs
    for k, v in template.items():
        # check if we're in the secret state
        if secret is True:
            # check that there's a default
            if v != ('' or None or False):
                # if there is then prompt with the default but obscured
                prompt = prompt_text.format(k=k, v=__obscure(v, char))
            else:
                # but if there isn't one then don't try to display it
                prompt = "'{k}: ".format(k=k)
            # set the value of the user input, if not to the default
            new_config[k] = getpass.getpass(prompt)
        # if we're not handling secrets
        else:
            # don't obscure the default values if not secret
            prompt = prompt_text.format(k=k, v=v)
            new_config[k] = input(prompt)
        # print the prompt
        print(prompt)
        # set the value of the user input, if not to the default
        # new_config[k] = func() or v
        # if secret set the new value's display version to be obscured
        if secret is True:
            v_display = __obscure(new_config[k], char)
        # if not don't obscure it
        else:
            v_display = new_config[k]
        # print the results, but delete the extra line from the user if they entered the default
        if v == new_config[k]:
            print('\033[F')
        print(set_confirmation_text.format(k=k, v=v_display, f=filename))
    return new_config

def make(
        data,
        filename='config',
        path='',
        get=False,
        force=False):
    """Make a file at the system path specified, or where run from."""
    # Variables formatting
    # we only support json but should abstract for later.
    format = 'json'
    # we only support TTY (terminal/shell/stdout/console),
    # but should abstract for later.
    promptcontext = 'TTY'
    # we only support not secret but should abstract for later
    secret = False
    outpath = '{p}{fn}.{fmt}'.format(p=path, fn=filename, fmt=format)

    # Custom conditions and error handling
    # handle data
    if not isinstance(data, dict):
        raise TypeError("'data' argument must be a python dictionary.")

    # handle context
    if __validate_context(promptcontext) is True:
        __prompt(promptcontext, data)
    else:
        raise ValueError(
            "'promptcontext' argument must be one of {v}".format(
                v=''.join(map(str, valid_contexts))))

    # handle file exists
    if os.path.isfile(outpath) and force is False:
        raise Exception(
            "{f} exists. Use Configify.make(force=True) to override.".format(
                f=outpath))

    __generate_file(data, outpath, format)

    # Contextualized returns before default return
    # handle get
    if get is False:
        return None

    return {outpath: data}
