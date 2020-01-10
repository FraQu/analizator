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



