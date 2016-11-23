import os
from urllib.request import urlopen

def download(url):
    """Download a file and save it in the current folder.
    Return the name of the downloaded file."""

    # Get the filename.
    file = os.path.basename(url)

    if not file:
        file = 'downloaded'

    # Download the file unless it already exists.
    if not os.path.exists(file):
        with open(file, 'w') as f:
            print(urlopen(url).read())
            f.write(urlopen(url).read())
    return file
