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


def make(
        data={},
        filename='config.json',
        path='',
        secret=True,
        get=False,
        char='*',
        format='json'):
    """Make a file at the system path specified, or where run from."""
    # format the save destination
    path_and_name = '{p}{f}'.format(p=path, f=filename)
    return {path_and_name: data}
