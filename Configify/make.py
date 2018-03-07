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


valid_contexts = ['tty']

def __generate_file(data, outpath, format):
    """Generate the file."""
    f = open(outpath, 'w')
    f.write(str(json.dumps(data)))


def __validate_context(context):
    if context.lower() in valid_contexts:
        return True
    else:
        return False

def __prompt(context, data):
    """Prompt the user for input from a context (TTY, app, SMS, API etc)."""
    pass


def make(
        data,
        filename='config',
        path='',
        get=False,
        force=False):
    """Make a file at the system path specified, or where run from."""
    # Variables formatting
    # we only support json, but should abstract for later.
    format = 'json'
    # we only support TTY (terminal/shell/stdout/console), but should abstract for later.
    promptcontext='TTY'
    outpath = '{p}{fn}.{fmt}'.format(p=path, fn=filename, fmt=format)

    # Custom conditions and error handling
    # handle data
    if not isinstance(data, dict):
        raise TypeError("'data' argument must be a python dictionary.")

    # handle context
    if __validate_context(promptcontext) is True:
        __prompt(context=promptcontext, data=data)
    else:
        raise ValueError(
            "'promptcontext' argument must be one of {v}".format(
                v=''.join(map(str, valid_contexts))))

    # handle file exists
    if os.path.isfile(outpath) and force is False:
        raise Exception("File {f} exists. Use Configify.make(force=True) to override.".format(f=outpath))

    __generate_file(data, outpath, format)

    # Contextualized returns before default return
    # handle get
    if get is False:
        return None

    return {outpath: data}
