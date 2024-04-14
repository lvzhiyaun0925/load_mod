""" command
If you want to close the source, change the __command_main__ value to your pyd file name (without the suffix)。
pyd should be placed in the root directory of the project!!
Note: Only pyd/py can be loaded, do not compile to dll.
"""
import sys
import os
program_name = os.path.basename(sys.argv[0])
########################################################################################################################

# The editing functions are described below:
# -foundation-

# Tell the loader which third-party libraries need to be installed, and he will use pip to install him.
__command_libraries__ = ['pyqt5', 'pygame']
# The name at the time of import(THIRD PARTY LIBRARIES).
__command_libraries_name__ = ['PyQt5', 'pygame']

__command_main__ = 'Beta'  # Set the main program to main.
__command_class__ = 'Main'  # Tell the mod loader which class it should execute(main program).
__command_function__ = '__MAIN__'  # Tell the mod loader which class's function it should execute(main program).
__command_function_args__ = ''
__command_append__ = ''  # Appends, ForExample: .function_name(arg)

# -advanced (!) NEWBIES DO NOT EDIT !!!!!!!!!!-

if program_name == '__main__.py':
    '''If it is__main__.py it means that it is a test and does not pass some unnecessary parameters.'''
    __command_class_args__ = 'root, None, None, None, None, None, None'

else:
    # Please do not change it unless necessary,
    # This is the argument passed by the class and function, and it should never be changed unless necessary.
    __command_class_args__ = 'i, button_1, logging_config, error_1, error_name, error_1_j, mod_name_not_error'

...