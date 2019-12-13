import tkinter as tk
from tkinter import *
from libs import file_name
from tkinter import messagebox as msg


def count_letters():
    ##
    # Show Window about letters in text.
    ##

    try:
        file = open(file_name.name_file)
        win = tk.Toplevel()
        win.geometry("400x200")
        win.title("Number of letters")

        data = file.read()
        rm_spaces = data.replace(" ", "")
        rm_dots = rm_spaces.replace(".", "")
        rm_q = rm_dots.replace("?", "")
        rm_em = rm_q.replace("!", "")
        rm_sc = rm_em.replace(";", "")
        rm_comm = rm_sc.replace(",", "")
        rm_c = rm_comm.replace(":", "")
        rm_a = rm_c.replace("'", "")
        rm_d = rm_a.replace("-", "")
        rm_an = len(rm_d.replace("$", ""))

        text = Label(win, text="Number of letters in text: ")
        text.pack()
        number_of_letters = Label(win, text=rm_an)
        number_of_letters.pack()

    except IOError:
        msg.showinfo("There is no file!", "Download file...")

