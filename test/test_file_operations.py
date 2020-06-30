import unittest
from unittest import TestCase
import utils
import json
import os

imageFiles = [
    'Geneva.JPG', 'RANDOM.GIF', 'geneva-comp.jpg', 'new-hampshire-comp.jpg',
    'new-york-comp.jpg', 'random.gif', 'random.jpeg', 'randompng-comp.png',
    'vietnam-comp.jpg', 'vietnam.png'
]

pdfFiles = ['lorem.pdf']


class TestFileOperations(TestCase):
    def setUp(self):
        self.currentDirectory = os.getcwd()
        self.testFileDirectory = os.path.join(self.currentDirectory,
                                              "test/files/")
        self.files = [
            'Geneva.JPG', 'RANDOM.GIF', 'geneva-comp.jpg', 'lorem.html',
            'lorem.md', 'lorem.odt', 'lorem.pdf', 'lorem.txt',
            'new-hampshire-comp.jpg', 'new-york-comp.jpg', 'random.gif',
            'random.jpeg', 'randompng-comp.png', 'vietnam-comp.jpg',
            'vietnam.png'
        ]

    def test_listImageFiles(self):
        # find only image files
        imageExts = [".jpg", ".gif", ".png", ".jpeg"]
        fullImagePaths = [
            os.path.join(self.testFileDirectory, file) for file in imageFiles
        ]
        result = utils.listFiles(self.testFileDirectory, imageExts)
        self.assertEqual(result, fullImagePaths)

    def test_listPdfFile(self):
        # find only pdf files
        pdfExts = [
            ".pdf",
        ]
        fullPdfPaths = [
            os.path.join(self.testFileDirectory, file) for file in pdfFiles
        ]
        result = utils.listFiles(self.testFileDirectory, pdfExts)
        self.assertEqual(result, sorted(fullPdfPaths))

    def test_listFilesNoExtArg(self):
        # test passing no extension argument
        self.assertRaises(TypeError, utils.listFiles, self.testFileDirectory)

    def test_listFilesNoArguments(self):
        # test passing no arguments
        self.assertRaises(TypeError, utils.listFiles)

    def test_listPdfJpg(self):
        # test finding pdf and jpg
        jpgPdfFiles = imageFiles = [
            'Geneva.JPG', 'geneva-comp.jpg', 'new-hampshire-comp.jpg',
            'new-york-comp.jpg', 'vietnam-comp.jpg', "lorem.pdf"
        ]
        fullJpgPdfPaths = [
            os.path.join(self.testFileDirectory, file) for file in jpgPdfFiles
        ]
        exts = [".pdf", ".jpg"]
        result = utils.listFiles(self.testFileDirectory, exts)
        self.assertEqual(result, sorted(fullJpgPdfPaths))


if __name__ == '__main__':
    unittest.main()
