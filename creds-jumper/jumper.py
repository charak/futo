#!/usr/bin/env python 

import os,sys
import time
from packages import *


def __init__(self):
		#os.system('clear')
		pass
		
def jumper_use(use):
		os.system('clear')
		x = intro.jumper_intro()
		x.main_banner()
global main		
def main(self):
		
	while 1:
					
			try:	
					#os.system('clear')
					
					global option
					

					option=raw_input('[Jump3r =>>>>>>>] ')
						
					
					if option == "list_modules":
								self=modules.modulehelp()
								self.modulelist()
								#creds_main("")

					elif option == "about":
								self=about.thisme()
								self.itsme()
					elif option == "quit":
								os.system('clear')
								sys.exit(0)
					elif option == "clear":
								os.system('clear')
								
								print ""
					elif option=="help":
								self=help.jumphelp()
								self.helpus()
					else:
								print "wrong"
								return main("")

					
	
			except KeyboardInterrupt as e:
				try:
					print ""
					choice = raw_input("Wanna Exit? [y/N] ")
					if choice.lower() != "" and choice.lower()[0] == "y":
						exit()
						return True
					else:
						os.system('clear')
						x = intro.jumper_intro()
						x.main_banner()
						return main("")
				except KeyboardInterrupt as e:
						os.system('clear')
						return main("")
	else :					
			
			return main("")
			option=""					
						
if __name__ == '__main__':
			jumper_use("")
			main("")
			
				
