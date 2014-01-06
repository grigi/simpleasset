"""
Python version compatibility layer
"""

from __future__ import division

import sys

__all__ = ['PYVER']

PYVER = sys.version_info[0] + (sys.version_info[1] / 10.0)

if PYVER < 3.3:
    FileNotFoundError = IOError # pylint: disable=W0622
    __all__.extend(["FileNotFoundError"])

if PYVER < 3.0:
    from io import open # pylint: disable=W0622,W0611
    __all__.extend(["open"])
