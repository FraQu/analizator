import tkinter as tk
from tkinter import *
from tkinter import messagebox as msg
from collections import Counter
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


        counter = Counter(data)
        consonants = counter['b'] + counter ['B'] + counter ['c'] + counter ['C'] + counter ['d'] + counter ['D'] \
        + counter['f'] + counter ['F'] + counter ['g'] + counter ['G'] + counter ['h'] + counter ['H'] \
        + counter['j'] + counter ['J'] + counter ['k'] + counter ['K'] + counter ['l'] + counter ['L'] \
        + counter['m'] + counter ['M'] + counter ['n'] + counter ['N'] + counter ['p'] + counter ['P'] \
        + counter['q'] + counter ['Q'] + counter ['r'] + counter ['R'] + counter ['s'] + counter ['S'] \
        + counter['t'] + counter ['T'] + counter ['v'] + counter ['V'] + counter ['w'] + counter ['W'] \
        + counter['x'] + counter ['X'] + counter ['z'] + counter ['Z']

        a = counter['a'] + counter['A']
        b = counter['b'] + counter['B']
        c = counter['c'] + counter['C']
        d = counter['d'] + counter['D']
        e = counter['e'] + counter['E']
        f = counter['f'] + counter['F']
        g = counter['g'] + counter['G']
        h = counter['h'] + counter['H']
        i = counter['i'] + counter['I']
        j = counter['j'] + counter['J']
        k = counter['k'] + counter['K']
        l = counter['l'] + counter['L']
        m = counter['m'] + counter['M']
        n = counter['n'] + counter['N']
        o = counter['o'] + counter['O']
        p = counter['p'] + counter['P']
        q = counter['q'] + counter['Q']
        r = counter['r'] + counter['R']
        s = counter['s'] + counter['S']
        t = counter['t'] + counter['T']
        u = counter['u'] + counter['U']
        v = counter['v'] + counter['V']
        w = counter['w'] + counter['W']
        x = counter['x'] + counter['X']
        y = counter['y'] + counter['Y']
        z = counter['z'] + counter['Z']
        text.insert(INSERT, "A: ")
        text.insert(END, a)
        text.insert(END, "\nB: ")
        text.insert(END, b)
        text.insert(END, "\nC: ")
        text.insert(END, c)
        text.insert(END, "\nD: ")
        text.insert(END, d)
        text.insert(END, "\nE: ")
        text.insert(END, e)
        text.insert(END, "\nF: ")
        text.insert(END, f)
        text.insert(END, "\nG: ")
        text.insert(END, g)
        text.insert(END, "\nH: ")
        text.insert(END, h)
        text.insert(END, "\nI: ")
        text.insert(END, i)
        text.insert(END, "\nJ: ")
        text.insert(END, j)
        text.insert(END, "\nK: ")
        text.insert(END, k)
        text.insert(END, "\nL: ")
        text.insert(END, l)
        text.insert(END, "\nM: ")
        text.insert(END, m)
        text.insert(END, "\nN: ")
        text.insert(END, n)
        text.insert(END, "\nO: ")
        text.insert(END, o)
        text.insert(END, "\nP: ")
        text.insert(END, p)
        text.insert(END, "\nQ: ")
        text.insert(END, q)
        text.insert(END, "\nR: ")
        text.insert(END, r)
        text.insert(END, "\nS: ")
        text.insert(END, s)
        text.insert(END, "\nT: ")
        text.insert(END, t)
        text.insert(END, "\nU: ")
        text.insert(END, u)
        text.insert(END, "\nV: ")
        text.insert(END, v)
        text.insert(END, "\nW: ")
        text.insert(END, w)
        text.insert(END, "\nX: ")
        text.insert(END, x)
        text.insert(END, "\nY: ")
        text.insert(END, y)
        text.insert(END, "\nZ: ")
        text.insert(END, z)
        text.insert(END, "\nConsonants: ")
        text.insert(END, consonants)
        text.insert(END, "\nVowels: ")
        text.insert(END, vowels)
        text.pack()

    except IOError:
        msg.showinfo("There is no file!", "Download file...")

