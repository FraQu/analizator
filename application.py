import tkinter as tk
from tkinter import *
from libs.count_letters import count_letters
from msg_box import _msg_box


class Application:
    def __init__(self):
        self.win = tk.Tk()
        self.create_widgets()
        self.text = tk.Text(self.win)
        self._widgets_styling()
        self.win.mainloop()

    def _widgets_styling(self):
        ##
        # Style of widgets
        ##
        self.win.geometry("800x800")
        self.win.title("Text Analyzer")
        self.win.iconbitmap(default="icons/text_analyzer.ico")
        self.scrollbar_text = tk.Scrollbar(self.win)
        self.scrollbar_text.place(in_=self.text, relx=1., rely=0, relheight=1.)
        self.scrollbar_text.config(command=self.text.yview)
        self.text.config(yscrollcommand=self.scrollbar_text.set)
        self.text.place(x=0, y=0, relwidth=1, relheight=1, width=- 18)

    def create_widgets(self):
        ##
        # Create widgets like menu, text box, etc.
        ##
        menu_bar = Menu()
        self.win.config(menu=menu_bar)

        file_menu = Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="Download hardcoded file")
        file_menu.add_command(label="Open file...")
        file_menu.add_command(label="Generate usage report [A-Z]...")
        file_menu.add_command(label="Save file...")
        file_menu.add_command(label="Save statistics...")
        file_menu.add_command(label="Exit")

        count_menu = Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Count", menu=count_menu)
        count_menu.add_command(label="Count letters...", command=count_letters)
        count_menu.add_command(label="Count punctuation marks...")
        count_menu.add_command(label="Count sentences...")
        count_menu.add_command(label="Count words...")

        help_menu = Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Help", menu=help_menu)
        help_menu.add_command(label="About...", command=_msg_box)


app = Application()


