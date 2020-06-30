import os
import exiftool
import utils

exts = [".jpg", ".gif", ".png", ".jpeg"]
tags = []


def findExifFiles(dirs:list, tags:list, exts:list):
    exifFiles = {}
    for d in dirs:
        utils.listFiles(d, exts)
    return exifFiles
