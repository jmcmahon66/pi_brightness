import unittest
import sys
import os

current_directory = os.path.dirname(os.path.realpath(__file__))
# Set the working directory to the script's directory
os.chdir(current_directory)
parent_directory = os.path.dirname(current_directory)
sys.path.append(parent_directory)
from module.pi_brightness import *

windows_path = "C:\\Workspace\\pi_brightness\\test"  # Need to make dir


class TestBacklightPath(unittest.TestCase):
    def test_default_path(self):
        # Test with a valid path
        path = find_backlight_path()
        self.assertIsNotNone(path)

    def test_valid_path(self):
        # Test with a valid path
        path = find_backlight_path(default_backlight_dir)
        self.assertIsNotNone(path)

    def test_invalid_path(self):
        path = find_backlight_path("/invalid/")
        self.assertIsNotNone(path)

    def test_windows_path(self):
        path = find_backlight_path(windows_path)
        self.assertIsNotNone(path)

    # def test_multiple_subdirs(self):

    # def test_no_subdir(self):


if __name__ == "__main__":
    unittest.main()