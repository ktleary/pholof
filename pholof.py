import os
import exiftool

exts = [".jpg", ".gif", ".png", ".jpeg"]
tags = []


def findExifFiles(dirs, tags, exts):
    exifFiles = {}
    for d in dirs:
        listFiles(d, patts)
