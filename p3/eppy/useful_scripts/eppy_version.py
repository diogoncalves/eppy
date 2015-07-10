# Copyright (c) 2012 Santosh Philip

# along with Eppy.  If not, see <http://www.gnu.org/licenses/>.
"""I print the current version of eppy. Being polite, I also say hello !"""






import argparse
import sys


pathnameto_eplusscripting = "../../"
sys.path.append(pathnameto_eplusscripting)

import eppy

if __name__ == '__main__':
    # do the argparse stuff
    parser = argparse.ArgumentParser(usage=None, description=__doc__)
    nspace = parser.parse_args()
    version = eppy.__version__
    print("Hello! I am  eppy version %s" % (version, ))