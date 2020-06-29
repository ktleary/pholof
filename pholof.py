import os
import exiftool

exts = [".jpg", ".gif", ".png", ".jpeg"]
tags = []




# def processFiles(filelist):
#     for filepath in filelist:
#         if filepath.endswith("pdf"):
#             print(filepath)
#             text = pdf2text(filepath)
#     return text

# def listFiles(directory, patterns):
# 	return []


def findExifFiles(dirs, tags, exts):
	exifFiles = {}
	for d in dirs:
		listFiles(d, patts)
