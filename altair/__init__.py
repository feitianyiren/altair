# flake8: noqa
__version__ = '2.0.0'

from .vegalite import *

def load_ipython_extension(ipython):
    from ._magics import vega, vegalite
    ipython.register_magic_function(vega, 'cell')
    ipython.register_magic_function(vegalite, 'cell')
