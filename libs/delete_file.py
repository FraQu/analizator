from tkinter import messagebox
from libs.file_name import name_file
import os
import sys


def delete_file():
    statistics = "statistics.txt"
    text = name_file
    if os.path.exists(statistics) and os.path.exists(text):
        os.remove(statistics), os.remove(text)
        messagebox.showinfo('Info1', 'The files has been deleted.')
        exit(0)
    if os.path.exists(statistics):
        os.remove(statistics)
        messagebox.showinfo('Info2', 'The statistics.txt file has been deleted.')
        exit(0)
    elif os.path.exists(text):
        os.remove(text)
        messagebox.showinfo('Info3', 'The 5.txt file has been deleted.')
        sys.exit(0)
    else:
        exit(0)

