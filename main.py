from pholof import findExifFiles
from pconfig import directories, tags, exts
import json

def main():
	print("running with: ", directories, tags, exts)
	filesExifData=findExifFiles(directories, tags, exts)
	print(json.dumps(filesExifData))


if __name__ == "__main__":
    import sys

    try:
        sys.exit(main())
    except FileNotFoundError as e:
        sys.exit(e)
