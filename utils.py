import os
"""Return the pathname of the specified directory."""


def listFiles(directory: str, patterns: list):
    filepaths = []
    for ROOT, DIR, FILES in os.walk(directory):
        for file in FILES:
            if file.lower().endswith((tuple(patterns))):
                filepaths.append(os.path.join(ROOT, file))
    return sorted(filepaths)
