import unittest
import sys
import os
import time

# To be run on raspberry PI/Linux

current_directory = os.path.dirname(os.path.realpath(__file__))
# Set the working directory to the script's directory
os.chdir(current_directory)
parent_directory = os.path.dirname(current_directory)
sys.path.append(parent_directory)
from pi_brightness.pi_brightness import *


class TestBacklightPath(unittest.TestCase):
    def test_default_path(self):
        print("Running test:", self._testMethodName)
        # Test with a valid path
        test_return = find_backlight_path()
        self.assertIsNotNone(test_return, msg=f"path = {test_return}")
        print(self._testMethodName, " - PASSED")
        print("-----")

    def test_valid_path(self):
        print("Running test:", self._testMethodName)
        # Test with a valid path
        test_return = find_backlight_path(default_backlight_dir)
        self.assertIsNotNone(test_return, msg=f"path = {test_return}")
        print(self._testMethodName, " - PASSED")
        print("-----")

    def test_invalid_path(self):
        print("Running test:", self._testMethodName)
        test_return = find_backlight_path("/invalid/")
        self.assertEqual(test_return, ErrorCode.PATH_NOT_FOUND)
        print(self._testMethodName, " - PASSED")
        print("-----")

    # def test_multiple_subdirs(self):

    # def test_no_subdir(self):

    def test_brightness_high(self):
        print("Running test:", self._testMethodName)
        test_return = update_brightness("100")
        self.assertEqual(test_return, 0)
        print(self._testMethodName, " - PASSED")
        print("-----")
        time.sleep(3)  # wait for screen tests on pi

    def test_brightness_low(self):
        print("Running test:", self._testMethodName)
        test_return = update_brightness("0")
        self.assertEqual(test_return, 0)
        print(self._testMethodName, " - PASSED")
        print("-----")
        time.sleep(3)  # wait for screen tests on pi

    def test_brightness_medium(self):
        print("Running test:", self._testMethodName)
        test_return = update_brightness("30")
        self.assertEqual(test_return, 0)
        print(self._testMethodName, " - PASSED")
        print("-----")
        time.sleep(3)  # wait for screen tests on pi

    # Test that number in range 0-100 is a translated to whole number in range 0-255
    def test_number_is_int_in_range(self):
        print("Running test:", self._testMethodName)
        lower_bound = 0
        upper_bound = 255
        loop_limit = 100

        # Iterate through values from lower_bound to upper_bound (inclusive)
        for value in range(lower_bound, loop_limit + 1):
            brightness = translate_percentage_brightness(value)
            print(f"Test BRIGHTNESS = {brightness}")
            # Assert that the value is a whole number
            self.assertAlmostEqual(brightness, round(brightness), delta=0, msg=f"Value {brightness} is not a whole number.")

            # Assert that the value is within the specified range
            self.assertGreaterEqual(brightness, lower_bound, msg=f"Value {brightness} is below the lower bound {lower_bound}.")
            self.assertLessEqual(brightness, upper_bound, msg=f"Value {brightness} is above the upper bound {upper_bound}.")

        print(self._testMethodName, " - PASSED")
        print("-----")

    def test_brightness_path(self):
        print("Running test:", self._testMethodName)
        test_return = update_brightness("80", default_backlight_dir)
        self.assertEqual(test_return, 0)
        print(self._testMethodName, " - PASSED")
        print("-----")

    def test_brightness_above_range(self):
        print("Running test:", self._testMethodName)
        return_code = update_brightness("101")
        self.assertEqual(return_code, ErrorCode.INT_OUT_OF_RANGE)
        print(self._testMethodName, " - PASSED")
        print("-----")


if __name__ == "__main__":
    unittest.main()
