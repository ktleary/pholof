import os
import glob
import json
from unittest import TestCase
from pholof import findExifFiles
from utils import listFiles


class TestFindExifFiles(TestCase):
    def setUp(self):
        self.currentDirectory = os.getcwd()
        self.testFileDirectory = os.path.join(self.currentDirectory,
                                              "test/files/")
        self.geoTags = ["Composite:GPSPosition"]
        self.imageExts = ['.jpg', '.gif', '.png', '.jpeg']
        self.files = [
            'Geneva.JPG', 'RANDOM.GIF', 'geneva-comp.jpg', 'lorem.html',
            'lorem.md', 'lorem.odt', 'lorem.pdf', 'lorem.txt',
            'new-hampshire-comp.jpg', 'new-york-comp.jpg', 'random.gif',
            'random.jpeg', 'randompng-comp.png', 'vietnam-comp.jpg',
            'vietnam.png'
        ]

    def test_findExifFilesReturnType(self):
        # test pholoc findExifFile return type is dictionary
        dirs, tags, exts = [], [], []
        result = findExifFiles(dirs, tags, exts)
        self.assertEqual(True, type(result) is dict)

    def test_findExifFilesReturnKeys(self):
        testFiles = listFiles(self.testFileDirectory, ['.jpg'])
        dirs = [self.testFileDirectory]
        tags = self.geoTags
        exts = self.imageExts
        exifFileData = findExifFiles(dirs, tags, exts)
        exifFiles = list(exifFileData)
        self.assertEqual(exifFiles[0], testFiles[0])

    def test_findExifGpsResult(self):
        exifFileData = findExifFiles([self.testFileDirectory], self.geoTags,
                                     ['.jpg'])
        testPath = "/home/user/projects/pholof/test/files/geneva-comp.jpg"
        testTag = "Composite:GPSPosition"
        exifData = exifFileData[testPath]
        exifTagData = exifData[testTag]
        self.assertEqual(exifTagData, "46.2210805555556 6.15205833333333")
