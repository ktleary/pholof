import os
import exiftool
from utils import listFiles
import json
''' retrieve file exifData '''


def findExifFiles(dirs: list, tags: list, exts: list):
    exifFileData = {}
    for d in dirs:
        files = listFiles(d, exts)
        with exiftool.ExifTool() as et:
            for f in files:
                exifData = {}
                for tag in tags:
                    tagdata = et.get_tag(tag, f)
                    if tagdata:
                        exifData[tag] = tagdata
                if exifData:
                    exifFileData[f] = exifData
    return exifFileData
