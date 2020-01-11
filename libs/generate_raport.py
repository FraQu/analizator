import re
from tkinter import messagebox as msg

from libs import file_name


def generate():
    try:
        filename = "statistics.txt"

        # Count words
        file = open(file_name.name_file)
        data = file.read()
        rm_spaces = data.replace(".", " ")
        words = len(rm_spaces.split(" "))

        # Count letters
        letters = ['A', 'a', 'E', 'e', 'I', 'i', 'O', 'o', 'U', 'u', 'Y', 'y', 'B', 'b', 'C', 'c', 'D', 'd', 'F', 'f',
                   'G', 'g', 'H', 'h', 'J', 'j', 'K', 'k', 'L', 'l', 'M', 'm', 'N', 'n', 'p', 'P', 'R', 'r', 'S', 's',
                   'T', 't', 'W', 'w', 'X', 'x', 'Z', 'z']
        count_letters = 0
        for char in data:
            if char in letters:
                count_letters = count_letters + 1

        # Count punctuation marks
        count = 0
        for i in range(0, len(data)):
            if data[i] in (".", "?"):
                count = count + 1
        punctuation_marks = count

        # Count sentences
        sentences = re.split(r'[.?]\s*', data)
        sentences = len(sentences) - 1

        # Count Vowels and Consonants
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
                file.write("Letters in text: " + str(count_letters) + "\n")
                + file.write("Punctuation marks in text: " + str(punctuation_marks) + "\n") \
                + file.write("Sentences in text: " + str(sentences) + "\n") \
                + file.write("Words in text: " + str(words) + "\n")
                + file.write("Consonants in text: " + str(consonants) + "\n" ) \
                + file.write("Vowels in text: " + str(vowels))

    except IOError:
        msg.showinfo("There is no file!", "Download file...")

