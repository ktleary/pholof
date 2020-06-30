import os
import exiftool
from utils import listFiles
import json

def findExifFiles(dirs: list, tags: list, exts: list):
    exifFiles = {}
    for d in dirs:
        files = listFiles(d, exts)
        for f in files:
            exifFiles[f] = ""
    return exifFiles
