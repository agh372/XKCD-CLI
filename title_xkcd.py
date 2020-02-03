from __future__ import print_function
from parser import *

s = """   
        Welcome to XKCD-CLI version

         
         """

def print_xkcd():
	for i in range(0, get_terminal_width()):
			print("*", end="")				
	print (s)	
	for i in range(0, get_terminal_width()):
			print("*", end="")							