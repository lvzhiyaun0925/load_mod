import tkinter as tk
from Profiles import command

root = tk.Tk()

mod = __import__(command.__command_main__)

run = (f'mod.{command.__command_class__}({command.__command_class_args__}).{command.__command_function__}'
       f'({command.__command_function_args__}){command.__command_append__}')
exec(run)

root.title('dev')

try:
    root.mainloop()
except KeyboardInterrupt:
    pass
