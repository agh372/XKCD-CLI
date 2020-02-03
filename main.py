from __future__ import print_function
from parser import *
from utils import *
import getpass
import title_xkcd
import stdgif 
from moviepy.editor import *






if __name__ == "__main__":
    title_xkcd.print_xkcd()
    number_of_pages = int(raw_input("Enter number the of comics you want:"))
    posts = get_posts_from_page(number_of_pages =number_of_pages)
    for post in posts:
    	for i in range(0, get_terminal_width()):
    		print("*", end="")
    	print(post['title'])
    	img_parse(post['media_url'],True)
			

	
	
    	