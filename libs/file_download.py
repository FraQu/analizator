import requests
from libs import file_name

from tkinter import *
from tkinter import messagebox


def file_download_window():
    ###
    # Download file from url and save as '5.txt' for later purposes.
    ###
    answer = messagebox.askquestion("Download file?", "Do you want to download file from Internet?")

    if answer == 'yes':
        win = Tk()
        win.title("Download file...")

        box = StringVar()
        entry = Entry(win, textvariable=box, width=50)
        entry.pack()

        def file_download():
            url = entry.get()
            download_file = requests.get(url, allow_redirects=True)

            filename = file_name.name_file
            with open(filename, 'wb') as file:
                file.write(download_file.content)
            messagebox.showinfo('File downloaded...', 'File has been downloaded and saved to Application path as ' +
                                                      filename + '.')
            win.destroy()
        button = Button(win, text="Download file", command=file_download)
        button.pack()
    else:
        messagebox.showinfo('Download or open...', 'You need to download or open file first!')

