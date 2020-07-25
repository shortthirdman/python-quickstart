# https://www.geeksforgeeks.org/downloading-files-web-using-python/
import os
import requests
import re

def isEmpty(directoryPath):
    if os.path.exists(directoryPath):
        if len(os.listdir(directoryPath)) == 0: 
            print("No files found in the directory.")
            return True
        else: 
            print("Some files found in the directory.")
            return False
    else: 
        return None

def isDownloadable(url):
    """
    Does the url contain a downloadable resource
    """
    h = requests.head(url, allow_redirects=True)
    header = h.headers
    content_type = header.get('content-type')
    if 'text' in content_type.lower():
        return False
    if 'html' in content_type.lower():
        return False
    return True

def downloadFile(file_url):
    r = requests.get(file_url, stream = True)
    with open("python.pdf","wb") as image:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:
                image.write(chunk)

def getFileName(file_url):
    if file_url.find('/'):
        file_name = file_url.rsplit('/', 1)[1]
    return file_name

def getFileNameFromCD(cd):
    """
    Get filename from content-disposition
    """
    if not cd:
        return None
    fname = re.findall('filename=(.+)', cd)
    if len(fname) == 0:
        return None
    return fname[0]

def getResourceLink():
    directoryPath = "D:/Pycharm projects/GeeksforGeeks/Nikhil"
    print("Valid path:", isEmpty(directoryPath))
    file1 = open('wallpapers.txt', 'r')
    
    while True: 
        count += 1
        # Get next line from file 
        line = file1.readline()
        # if line is empty 
        # end of file is reached 
        if not line:
            break
        file_url = line.strip()
        print("Line{}: {}".format(count, file_url))

    file1.close()


if __name__ == "__main__": 
    getResourceLink()