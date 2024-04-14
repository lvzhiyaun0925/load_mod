import tkinter as tk  # Libraries that must be used.
from tkinter import ttk  # It is recommended to use the TTK in Tkinter to achieve the effect of matching with the -
# - main program.
import logging  # Libraries that must be used.



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
