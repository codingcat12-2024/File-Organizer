import unittest
import os
import shutil
from pathlib import Path
from src.core import organize_folder

class TestFileOrganizer(unittest.TestCase):
    def setUp(self):
        # Create a temporary directory for testing
        self.test_dir = Path("./test_organizer_dir")
        self.test_dir.mkdir(exist_ok=True)
        
        # Create dummy files
        (self.test_dir / "image.jpg").touch()
        (self.test_dir / "document.pdf").touch()
        (self.test_dir / "unknown.xyz").touch()

    def tearDown(self):
        # Clean up the directory after test
        if self.test_dir.exists():
            shutil.rmtree(self.test_dir)

    def test_organization(self):
        # Run organizer logic
        results = organize_folder(self.test_dir)

        # Assert files were moved to correct subfolders
        self.assertTrue((self.test_dir / "Images" / "image.jpg").exists())
        self.assertTrue((self.test_dir / "Documents" / "document.pdf").exists())
        self.assertTrue((self.test_dir / "Others" / "unknown.xyz").exists())

        # Assert summary counts are accurate
        self.assertEqual(results["Images"], 1)
        self.assertEqual(results["Documents"], 1)
        self.assertEqual(results["Others"], 1)

if __name__ == "__main__":
    unittest.main()
