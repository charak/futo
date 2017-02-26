#!/usr/bin/env python 

import os,sys,time,threading,re
import SimpleHTTPServer,SocketServer,BaseHTTPServer
from packages import *


def __init__(self):
		#os.system('clear')
		pass
		
def jumper_use(use):
		os.system('clear')
		x = intro.jumper_intro()
		x.main_banner()
def jumper_server_run(self):
	
	try:		
					toolbar_width = 20
					jumper_use("")
					print "[+] Starting HTTP Server [+]"
					host = raw_input("[+] Define The Hostname Please >> ")
					port = int(raw_input("[+] Define Any Free Port To Run Server On >> "))
					handler = SimpleHTTPServer.SimpleHTTPRequestHandler
					get_dir = os.getcwd()
					os.chdir(get_dir+"/web/")
					global httpd
					httpd = SocketServer.TCPServer((host ,port ), handler)
					#http_start=httpd.serve_forever()
					thread_1 = threading.Thread(target = httpd.serve_forever)
					thread_1.daemon = True
					thread_1.start()
					os.system("sudo service apache2 start > /dev/null 2>&1 & \n")
					time.sleep(2)
					sys.stdout.write("Server Is Being Started =>[%s]" % (" " * toolbar_width))
					sys.stdout.flush()
					sys.stdout.write("\b" * (toolbar_width+1))
					for i in xrange(toolbar_width):
						time.sleep(0.1)
						sys.stdout.write("=")
						sys.stdout.flush()

					print "\n[+] Server Has Been Started [+]"
					time.sleep(2)
					#return jumper_server_run("")		
	except KeyboardInterrupt as e:
				try:
					print ""
					choice = raw_input("Wanna Exit? [y/N] ")
					if choice.lower() != "" and choice.lower()[0] == "y":
						exit()
						return True
					else:
						return jumper_server_run("")
				except KeyboardInterrupt as e:
						os.system('clear')
						return jumper_server_run("")
	except OSError as e:
		print "[-] port '%s' is busy , try different port [-]"%port
		time.sleep(2)
		return jumper_server_run("")									
def db_check(self):
	pass		
def main(self):
		
	while 1:		
			try:	
					global option
					print ""
					option=raw_input('[Jump3r =>>>>>>>] ')	
					if option == "list_modules":
								self=modules.modulehelp()
								self.modulelist()
								#creds_main("")
					elif option == "about":
								self=about.thisme()
								self.itsme()
					elif option == "clear":
								os.system('clear')			
					elif option =="help":
								self=help.jumphelp()
								self.helpus()
					elif option == "service_start":
								return jumper_server_run("")
					elif option == "listener":
								jumper_get_action("")			
					else:
								comm = os.system(option)
								#print re.sub("0","",comm)
								return main("")
			except KeyboardInterrupt as e:
				try:
					print ""
					choice = raw_input("Wanna Exit? [y/N] ")
					if choice.lower() != "" and choice.lower()[0] == "y":
						try:
							toolbar_width = 20
							httpd.shutdown()
							os.system("sudo service apache2 stop > /dev/null 2>&1 & \n")
							sys.stdout.write("Services Are Being Stopped =>[%s]" % (" " * toolbar_width))
							sys.stdout.flush()
							sys.stdout.write("\b" * (toolbar_width+1))
							for i in xrange(toolbar_width):
								time.sleep(0.1)
								sys.stdout.write("=")
								sys.stdout.flush()	
							print "\n[+] Service Has Been Stoped [+]"
							time.sleep(2)
							exit()
						except NameError as w:
							print"[INFO] No HTTP Server Was Running [INFO]"	
							exit()
							return True
					else:
						return main("")
				except KeyboardInterrupt as e:
						os.system('clear')
						return main("")
			except ValueError as e:
				print ""
				return main("")	
								
	else :					
			
			return main("")
			option=""
def jumper_get_action(self):
	pass 														
if __name__ == '__main__':
			jumper_server_run("")
			jumper_use("")
			main("")
			
				
