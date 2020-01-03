import requests
from libs import file_name, file_url
from tkinter import messagebox


def file_download():
    ###
    # Download file from url and save as 'name from fine_name.py' for later purposes.
    ###
    answer = messagebox.askquestion("Download file?", "Do you want to download file?")
    if answer == 'yes':
        messagebox.showinfo('File downloaded...', 'File has been downloaded and saved to Application path.')
        url = file_url.url
        filename = file_name.name_file
        download_file = requests.get(url, stream=True)

        with open(filename, 'wb') as file:
            for chunk in download_file.iter_content(chunk_size=1024):
                if not chunk:
                    break
                file.write(chunk)
    else:
        messagebox.showinfo('Download or open...', 'You need to download or open file first!')
