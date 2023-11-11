# import x
#
# from x import add, A
# # if module names are big then we will use aliases.
# import x as x_ref
#
# from mypackage import b, functions as f
# from mypackage.b import module2
# from mypackage.functions import average
# from mypackage.sub_package import sub_functions as sf
#
#
# b.module2()
#
# c = add(1, 2)
# print(c)
#
# print(x_ref.a)
#
# a = A()
# print(f.add(1, 2))
#
# print(average([1, 2, 3, 4, 5]))
#
# sf.sub_functions()

# whenever we use import statement then the statements from __init__ file will get executed and if we use the import
# within that package then it will not execute again. import mypackage whenever we import package and sub package
# then both the __init__ files of package and sub package will get executed. import mypackage.sub_package

# if we want to access functions in the modules of mypackage then we have to add them in the __init__ file of that
# package Also to access methods of the sub package we have to import sub_functions module in the init file.
import mypackage as mp

import mypackage.sub_package as sp
mp.sub_functions.sub_functions()

from mypackage import functions as af
from mypackage import b







