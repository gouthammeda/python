"""
Author : Prudhvi Akella
"""
# here we are importing chemistry class from .chemistryModule and creating the object for it inside the __init__ file of chemistry package and accessing it using science.chemistry
from Science.Chemistry import chemistry
#from Science import what_is_biology
from Science.Biology import biologyModule as pm

print(chemistry.what_is_a_atom())

# Observation1:
# how did "Inside Biology Module" got printed on to the console?
# Where did the chemistry object got created?

# Let's understand Python Memory Management to answer these question
