# pi_brightness
Module for controlling a Raspberry Pi's external display brightness  
Writes value to "/sys/class/backlight/DEVICE/brightness", which is used by the GPU to render the display backlight brightness

## Compatibility
Works on raspbian, functionality should also exist on most Linux systems  
Will only work if 1 device is attached as a screen

## Installation
```bash
pip install pi_brightness
```

## Usage
```python
from pi_brightness import *

# Use a value from 0-100 for screen brightness percentage
update_brightness("80")
```

## Error codes
PATH_NOT_FOUND = 1  
INT_OUT_OF_RANGE = 2  
UPDATE_FAILED = 3  
TOO_MANY_DEVICES = 4  
FILE_DOESNT_EXIST = 5  

## Contributing
Feel free to pull and use as you see fit.  
If you find any of these tools and scripts useful, feel free to dontate <lightning address TBA>

## License
[MIT](https://choosealicense.com/licenses/mit/)
