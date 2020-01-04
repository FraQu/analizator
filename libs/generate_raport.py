from collections import Counter
from tkinter import messagebox as msg

from libs import file_name


def generate():
    try:
        # Count words
        file = open(file_name.name_file)
        data = file.read()
        rm_spaces = data.replace(".", " ")
        words = len(rm_spaces.split(" "))

        # Count letters

        file = open(file_name.name_file)
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

        # Count punctuation marks
        file = open(file_name.name_file)
        data = file.read()
        count = 0
        for i in range(0, len(data)):
            if data[i] in (".", "?"):
                count = count + 1
        punctuation_marks = count

        # Count sentences
        file = open(file_name.name_file)

        data = file.read()
        sentences = len(data.split("."))
        sentences = sentences - 1

        filename = "statistics.txt"

        if filename:
            with open(filename, "w") as file:
                file.write("Count letters: " + str(rm_an) + "\n")
                + file.write("Count punctuation marks: " + str(punctuation_marks) + "\n") \
                + file.write("Count sentences: " + str(sentences) + "\n") \
                + file.write("Count words: " + str(words))

        file = open(file_name.name_file, encoding="utf8")
        data = file.read()

        counter = Counter(data)
        consonants = counter['b'] + counter['B'] + counter['c'] + counter['C'] + counter['d'] + counter['D'] \
                     + counter['f'] + counter['F'] + counter['g'] + counter['G'] + counter['h'] + counter['H'] \
                     + counter['j'] + counter['J'] + counter['k'] + counter['K'] + counter['l'] + counter['L'] \
                     + counter['m'] + counter['M'] + counter['n'] + counter['N'] + counter['p'] + counter['P'] \
                     + counter['q'] + counter['Q'] + counter['r'] + counter['R'] + counter['s'] + counter['S'] \
                     + counter['t'] + counter['T'] + counter['v'] + counter['V'] + counter['w'] + counter['W'] \
                     + counter['x'] + counter['X'] + counter['z'] + counter['Z']
        vowels = counter['a'] + counter['A'] + counter['e'] + counter['E'] + counter['i'] + counter['I'] \
                 + counter['o'] + counter['O'] + counter['u'] + counter['U'] + counter['y'] + counter['Y']
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

        if filename:
            with open(filename, "w") as file:
                file.write("Count letters: " + str(rm_an) + "\n")
                + file.write("Count punctuation marks: " + str(punctuation_marks) + "\n") \
                + file.write("Count sentences: " + str(sentences) + "\n") \
                + file.write("Count words: " + str(words) + "\n")
                + file.write("Count consonants: " + str(consonants) + "\n" ) \
                + file.write("Count vowels: " + str(vowels))

    except IOError:
        msg.showinfo("There is no file!", "Download file...")



