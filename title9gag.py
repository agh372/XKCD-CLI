from __future__ import print_function
from parser import *

s = """   
        Welcome to

              *
            *   * 
           *      *      
         *         *
       *            *
        *          * *
          *      *   *
            *   *    *
              *      * 
                     * gag
                     *
                     *
        *          *
           *      *
             *   *
               *

         
         """

def print_9gag():
	for i in range(0, get_terminal_width()):
			print("*", end="")				
	print (s)	
	for i in range(0, get_terminal_width()):
			print("*", end="")							