"""
Author : Prudhvi Akella
Understanding Packages
"""

# when mypackage is imported in any of the python program then DatapackageUtils.py file will be the first that will be get
# executed Its like a constructor to a package

# Here "." in front of functions or b represents current directory

from .functions import add, average
from .b import module2
from .sub_package import sub_functions

print("This is the message from mypackage __init__")
