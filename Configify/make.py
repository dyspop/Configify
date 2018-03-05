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


def __generate_file(data, outpath):
    f = open(outpath, 'w')
    f.write(str(data))


def make(
        data,
        filename='config',
        path='',
        secret=True,
        get=False,
        char='*'):
    """Make a file at the system path specified, or where run from."""
    # Variables formatting
    # we only support json, but should abstract for later.
    format = 'json'
    outpath = '{p}{fn}.{fmt}'.format(p=path, fn=filename, fmt=format)

    # Custom conditions and error handling
    # handle data
    if not isinstance(data, dict):
        raise TypeError("'data' argument must be a python dictionary.")

    __generate_file(data, outpath)

    # Contextualized returns before default return
    # handle get
    if get is False:
        return None

    return {outpath: data}
