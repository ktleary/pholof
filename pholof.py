import exiftool

exts = [".jpg", ".gif", ".png", ".jpeg"]
tags = []

# def listFiles(directory, patterns="*.*"):
#     filepaths = []
#     for ROOT, DIR, FILES in os.walk(directory):
#         for file in FILES:
#             if file.endswith((tuple(patterns))):
#                 filepaths.append(os.path.join(ROOT, file))
#     return sorted(filepaths)


# def processFiles(filelist):
#     for filepath in filelist:
#         if filepath.endswith("pdf"):
#             print(filepath)
#             text = pdf2text(filepath)
#     return text

def listFiles(directory, patterns):
	return []


def findExifFiles(dirs, tags, exts):
	exifFiles = {}
	for d in dirs:
		listFiles(d, patts)
