import sys
import os

program_name = os.path.basename(sys.argv[0])
__command_libraries__ = ['PyQt5', 'pygame']
__command_main__ = 'main'
__command_class__ = 'Main'
__command_function__ = '__MAIN__'
__command_function_args__ = ''
__command_append__ = ''

if program_name == '__main__.py':
    __command_class_args__ = 'root, None, None, None, None, None, None'
else:
    __command_class_args__ = '_root, button_1, logging_config, error_1, error_name, error_1_j, mod_name'

