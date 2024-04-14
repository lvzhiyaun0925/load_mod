import tkinter as tk  # Libraries that must be used.
from tkinter import ttk  # It is recommended to use the TTK in Tkinter to achieve the effect of matching with the -
# - main program.
import logging  # Libraries that must be used.

'''
Modding SDK(v6.7.2) (MUST-SEE):

When using this script, you must adhere to the following rules:

1. If you write down your module operation log, please use Chinese.

2. You must change the __introduction__ and __Supported_versions__ and populate the correct values.
    In the Profiles/illustrate directory.

3. If you can use the TTK module, use TTK, don't use TK.

4. When filling in the call file path, it must be (must) preceded by "mods/temp/mods/{packaged zip name}/", 
    which is required, otherwise there will be an error when loading,
    For example: path = 'mods/temp/mods/SDK/images/python.png'.If you were writing normally, you would write it as:
    path = 'images/python.png'

5. To call a local module/library, do not use the import library_name directly, please use:
    from mods.temp.mods.<zip name> import repository_name.

6. You may need to make your mod name a little more complicated to avoid duplicate names with other mods, mainly because
    users can't rename mod names (which can cause errors). I really don't want to make this rule...

7. You don't need any build tools to package it, just compress it into a zip directly in the root directory of the
    project.

8. If you want to close the source, go to Profiles/command and change the value of the __command_main__ to the pyd file
    in the root directory of your project (no suffix required)
'''

########################################################################################################################

'''
Explanation of args parameters:

window_1: The main window instance for adding and managing GUI components(This will also be the one you use the most).
    Here, the tkinter component you created can be given to this window, like this:
        ttk.Button(self.window_1, text='example').pack()
    It's like writing code normally,just create the component on the window_1.

button_1: An instance of a button, which modules can use to add event handlers.
    This button is for developer testing, that is, it is simply used to test the content of the change 
    button (it can also be hidden), and it serves as a developer method to change the component.

logging_config: A dictionary containing logging configurations. Modules should use these settings for logging.
    You can see the details of how to use it in the main function,You can also use print
     to view the content (go to "加载mod" and run it!!!).

error_detailed, error_name, error_simplification: Variables for error recording.Modules should update these variables
when an error occurs.
    error_detailed: Details of each module error,is a list.
    error_name: The name of all the faulty modules.
    error_simplification: Simple information about each mod error.

    Error Detailed and Error Simplification, you can print it yourself below to see the difference.

loaded_mods: A list for recording the names of successfully loaded modules.
    Very simple, there's not much to say...
'''


class Main(object):

    def __init__(self, *args):
        (window_1,  # You will use this window_1 parameter a lot.
         button_1_,
         logging_config,
         error_detailed,
         error_name,
         error_simplification,
         loaded_mods) = args  # For more information on these parameters, see the comments above the class.

        super().__init__()  # Please fill in the actual situation.
        self.window_1 = window_1  # Feel free to change the variable name.
        self.button_1_ = button_1_  # Feel free to change the variable name.
        self.logging_config = logging_config  # Feel free to change the variable name.
        self.error_detailed = error_detailed  # Feel free to change the variable name.
        self.error_name = error_name  # Feel free to change the variable name.
        self.error_simplification = error_simplification  # Feel free to change the variable name.
        self.loaded_mods = loaded_mods  # Feel free to change the variable name.

        try:
            logging.basicConfig(filename=self.logging_config['filename'],
                                level=self.logging_config['level'],
                                format=self.logging_config['format'],
                                encoding='utf-8')
            '''
            The above is the basic configuration of the logger,
            This is achieved by loading logging_config dictionary parameters.
            Call the element in the logging_config dictionary,
            you can print this dictionary to see the specific parameters.
            '''

        except TypeError:
            '''
            This will serve as a test for not creating logs,
            but if that is what you are trying to test your logs, then configure the correct parameters...
            '''
            pass

    def __MAIN__(self) -> 'You will write the code here':
        # ———————————————————————————Start Coding—————————————————————————————
        ...  # You will write the code here, please delete this line.


if __name__ == '__main__':
    ROOT = tk.Tk()  # Prevent name collision with root.

    BUTTON_1 = ttk.Button(ROOT, text='developer testing', command=lambda: (ttk.Label(tk.Toplevel(ROOT), text='dev!!!!')
                                                                           .pack()))
    # This is to enable the button_1_ function, you can go to the top  of the main function to see how to use button_1_.

    Main(ROOT, BUTTON_1, None, None, None, None, None)  # You can pass the other 5 parameters as needed.

    BUTTON_1.pack()

    ROOT.title('dev')
    ROOT.mainloop()