from pholof import findExifFiles
from pconfig import directories, tags, exts

def main():
	filesExifData=findExifFiles(directories, tags, exts)


if __name__ == "__main__":
    import sys
    import pconfig
    try:
        sys.exit(main())
    except FileNotFoundError as e:
        sys.exit(e)
