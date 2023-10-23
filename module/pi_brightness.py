import os
import sys

# Uses Linux Kernel GPU driver registers, should be supported by most Linux platforms
# https://docs.kernel.org/gpu/backlight.html
# Doesn't work on OLED screen because of no backlight

backlight_dir = "/sys/class/backlight/"
brightness_file = "brightness"


def find_backlight_path():
    # Check if /sys/class/backlight/ exists
    if not os.path.exists(backlight_dir) or not os.path.isdir(backlight_dir):
        return None

    # Get list of subdirectories in /sys/class/backlight/
    backlight_subdirs = [d for d in os.listdir(backlight_dir) if os.path.isdir(os.path.join(backlight_dir, d))]

    # Check if there is exactly one child directory
    # Will only change backlight if only 1 attached screen is detected
    if len(backlight_subdirs) == 1:
        # Construct the full path of the child directory
        brightness_file_path = os.path.join(backlight_dir, backlight_subdirs[0], brightness_file)
        return brightness_file_path
    else:
        return None


dir = find_backlight_path()
print(dir)