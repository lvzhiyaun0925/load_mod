import tkinter as tk
from tkinter import ttk
import logging


class Main(object):

    def __init__(self, *args):
        (self.window_1,
         self.button_1_,
         self.logging_config,
         self.error_detailed,
         self.error_name,
         self.error_simplification,
         self.loaded_mods) = args
        super().__init__()
        try:
            logging.basicConfig(filename=self.logging_config['filename'],
                                level=self.logging_config['level'],
                                format=self.logging_config['format'],
                                encoding='utf-8')
        except TypeError:
            pass

    def __MAIN__(self) -> None:
        ttk.Label

if __name__ == '__main__':
    ROOT = tk.Tk()
    BUTTON_1 = ttk.Button(ROOT, text='developer testing', command=lambda: (ttk.Label(tk.Toplevel(ROOT), text='dev!!!!').pack()))
    Main(ROOT, BUTTON_1, None, None, None, None, None)
    BUTTON_1.pack()
    ROOT.title('dev')
    ROOT.mainloop()
