
"""
    Plugin importer

    This file goes through each package and imports it.
    The package must include a __init__.py.
"""

import os

__all__ = []
basedir = os.path.dirname(__file__)

for plugin in [os.path.split(x[0])[-1] for x in os.walk(basedir)][1:]:
    if os.path.exists(basedir + '/' + plugin + '/__init__.py'):
        print 'Adding plugin:', plugin
        __all__.append(plugin)
    else:
        print 'No __init__.py for:', plugin

__all__.sort()
