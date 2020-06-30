import unittest
import utils
import json
import os

files = [
    'Geneva.JPG', 'RANDOM.GIF', 'geneva-comp.jpg', 'lorem.html', 'lorem.md',
    'lorem.odt', 'lorem.pdf', 'lorem.txt', 'new-hampshire-comp.jpg',
    'new-york-comp.jpg', 'random.gif', 'random.jpeg', 'randompng-comp.png',
    'vietnam-comp.jpg', 'vietnam.png'
]

imageFiles = [
    'Geneva.JPG', 'RANDOM.GIF', 'geneva-comp.jpg', 'new-hampshire-comp.jpg',
    'new-york-comp.jpg', 'random.gif', 'random.jpeg', 'randompng-comp.png',
    'vietnam-comp.jpg', 'vietnam.png'
]

pdfFiles = ['lorem.pdf']

class TestFileOperations(unittest.TestCase):
    def test_listImageFiles(self):
        currentDirectory = os.getcwd()  # eg /home/user/projects/pholof
        testFileDirectory = os.path.join(currentDirectory, "test/files/")
        imageExts = [".jpg", ".gif", ".png", ".jpeg"]
        fullImagePaths = [
            os.path.join(testFileDirectory, file) for file in imageFiles
        ]
        result = utils.listFiles(testFileDirectory, imageExts)
        self.assertEqual(result, fullImagePaths)

    def test_listPdfFile(self):
        currentDirectory = os.getcwd()  # eg /home/user/projects/pholof
        testFileDirectory = os.path.join(currentDirectory, "test/files/")
        pdfExts = [".pdf",]
        fullPdfPaths = [
            os.path.join(testFileDirectory, file) for file in pdfFiles
        ]
        result = utils.listFiles(testFileDirectory, pdfExts)
        self.assertEqual(result, fullPdfPaths)



if __name__ == '__main__':
    unittest.main()
