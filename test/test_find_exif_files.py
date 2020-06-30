from unittest import TestCase
from pholof import findExifFiles


class TestFindExifFiles(TestCase):
    def setUp(self):
        print("setup", str(1))

    def test_findExifFilesReturnType(self):
        # test pholoc findExifFile return type is dictionary
        dirs, tags, exts = [], [], []
        result = findExifFiles(dirs, tags, exts)
        self.assertEqual(True, type(result) is dict)
