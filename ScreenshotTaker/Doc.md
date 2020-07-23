# ScreenshotTaker

A python script to take screenshot of any website in any desired size

> You have to have selenium installed and setup first. Take a look at [here](https://selenium-python.readthedocs.io/installation.html) for detailed information.

To get help run:
`python take_ss.py -h` or `python take_ss.py --help`

Example:
```sh
python take_ss.py https://co-ronabd.info shot.png --width 1024 --height 768 --wait 20
```

Documentation:

```
usage: python take_ss.py [-h] [--width WIDTH] [--height HEIGHT] [--wait WAIT]
                         url filename

Take screenshot of any webpage in desired size

positional arguments:
  url              URL of the website
  filename         Image filename

optional arguments:
  -h, --help       show this help message and exit
  --width WIDTH    Width of screenshot (default 1920)
  --height HEIGHT  Height of screenshot (default 1080)
  --wait WAIT      Page loading time (default 15)


```
