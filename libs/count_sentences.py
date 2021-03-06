import tkinter as tk
from tkinter import *
from libs import file_name
from tkinter import messagebox as msg


def count_sentences():
    ##
    # Count sentences in file
    ##
    try:
        file = open(file_name.name_file)
        win = tk.Toplevel()
        win.geometry("400x200")
        win.title("Number of sentences")
        data = file.read()

        sentences = re.split(r'[.?]\s*', data)
        count_sentence = len(sentences) - 1
        text = Label(win, text="Number of sentences in text: ")
        text.pack()
        number_of_sentences = Label(win, text=count_sentence)
        number_of_sentences.pack()
    except IOError:
        msg.showinfo("There is no file!", "Download file...")

