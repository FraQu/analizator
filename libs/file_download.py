import requests
from libs import file_name, file_url


def file_download():
    ###
    # Download file from url and save as 'name from fine_name.py' for later purposes.
    ###
    url = file_url.url
    filename = file_name.name_file
    download_file = requests.get(url, stream=True)

    with open(filename, 'wb') as file:
        for chunk in download_file.iter_content(chunk_size=1024):
            if not chunk:
                break
            file.write(chunk)

