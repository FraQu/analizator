import tkinter as tk
from tkinter import *
from tkinter import messagebox as msg
from libs import file_name


def plot_usage_statistics():
    try:

        file = open(file_name.name_file, encoding="utf8")
        data = file.read()

        win = tk.Toplevel()
        text = tk.Text(win)
        scrollbar_text = tk.Scrollbar(win)
        scrollbar_text.place(in_=text, relx=1., rely=0, relheight=1.)
        scrollbar_text.config(command=text.yview)
        text.config(yscrollcommand=scrollbar_text.set)
        text.place(x=0, y=0, relwidth=1, relheight=1, width=-18)
        win.geometry("400x460")
        win.title("Usage of letters")

        vowels = 0
        vowels_list = ['A', 'a', 'E', 'e', 'I', 'i', 'O', 'o', 'U', 'u', 'Y', 'y']
        for char in data:
            if char in vowels_list:
                vowels = vowels + 1

        consonants = 0
        consonants_list = ['B', 'b', 'C', 'c', 'D', 'd', 'F', 'f', 'G', 'g', 'H', 'h', 'J', 'j', 'K', 'k', 'L', 'l',
                           'M', 'm', 'N', 'n', 'p', 'P', 'R', 'r', 'S', 's', 'T', 't', 'W', 'w', 'X', 'x', 'Z', 'z']
        for char in data:
            if char in consonants_list:
                consonants = consonants + 1

        text.insert(INSERT, "Consonants: ")
        text.insert(END, consonants)
        text.insert(END, "\nVowels: ")
        text.insert(END, vowels)
        text.pack()

    except IOError:
        msg.showinfo("There is no file!", "Download file...")

