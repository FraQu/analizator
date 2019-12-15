import tkinter as tk
from tkinter import *
from libs import file_name
from tkinter import messagebox as msg


def count_punctuation_marks():
    ##
    # Count punctuation marks in file
    ##
    try:
        file = open(file_name.name_file)
        win = tk.Toplevel()
        win.geometry("400x200")
        win.title("Number of punctuation marks")
        data = file.read()
        count = 0
        for i in range(0, len(data)):
            if data[i] in (".", "?"):
                count = count + 1

        punctuation_marks = count
        text = Label(win, text="Number of punctuation marks in text: ")
        text.pack()
        number_of_punctuation_marks = Label(win, text=punctuation_marks)
        number_of_punctuation_marks.pack()
    except IOError:
        msg.showinfo("There is no file!", "Download file...")
