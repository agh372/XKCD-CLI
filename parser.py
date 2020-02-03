from __future__ import print_function
import urllib2
import os
from bs4 import BeautifulSoup, Comment
import img2txt
import sys,urllib, cStringIO
import ansi
import utils
from PIL import Image

def get_terminal_width():
	columns = os.popen('stty size', 'r').read().split()[1]
	#print (int(columns))
	return int(columns)

def img_parse(img_url, avatar=False):
	file = cStringIO.StringIO(urllib.urlopen(img_url).read())
	remote_img = Image.open(file)
	if avatar is True:
		img = img2txt.load_and_resize_image(file, True, 20, 1.0)
	else:
		img = img2txt.load_and_resize_image(file, True,(get_terminal_width()/3)*2, 1.0)
	pixel = img.load()
	width, height = img.size
	sys.stdout.write("\x1b[49m")
	sys.stdout.write("\x1b[K")
	sys.stdout.write(ansi.generate_ANSI_from_pixels(pixel, width, height, None)[0])
	sys.stdout.write("\x1b[0m\n")
