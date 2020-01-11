import tkinter as tk
from tkinter import *
from tkinter import messagebox as msg

from libs import file_name


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

        number_of_vowels = Label(win, text="Number of vowels in text: " + str(vowels))
        number_of_vowels.pack()
        number_of_consonants = Label(win, text="Number of consonants in text: " + str(consonants))
        number_of_consonants.pack()

    except IOError:
        msg.showinfo("There is no file!", "Download file...")

