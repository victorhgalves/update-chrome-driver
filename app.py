import requests
import zipfile
import os
from io import BytesIO


def getVersion():
    version = requests.get('https://chromedriver.storage.googleapis.com/LATEST_RELEASE').text
    return version

def updateChromeDriver():
    latest_version = getVersion()
    name_file = 'chromedriver_win32.zip'
    get_download = requests.get('https://chromedriver.storage.googleapis.com/{}/{}'.format(latest_version,name_file),stream=True)
    save_file = zipfile.ZipFile(BytesIO(get_download.content))
    save_file.extractall()
    
if __name__ == '__main__':
    updateChromeDriver()