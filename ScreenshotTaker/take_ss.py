from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
import argparse

parser = argparse.ArgumentParser(
    prog='python take_ss.py', description='Take screenshot of any webpage in desired size')
parser.add_argument('url', help='URL of the website')
parser.add_argument('filename', help='Image filename')
parser.add_argument('--width', type=int,
                    help='Width of screenshot (default 1920)')
parser.add_argument('--height', type=int,
                    help='Height of screenshot (default 1080)')
parser.add_argument('--wait', type=int,
                    help='Page loading time (default 15)')
args = parser.parse_args()

url, filename = args.url, args.filename
width = 1920 if args.width == None else args.width
height = 1080 if args.height == None else args.height
wait = 15 if args.wait == None else args.wait

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--start-maximized')
driver = webdriver.Chrome(options=chrome_options)
driver.set_window_size(width, height)
driver.get(url)
sleep(wait)
driver.get_screenshot_as_file(filename)
driver.close()
