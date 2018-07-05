#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Script Created By:
	Cr4sHCoD3
Copyrights:
	Cr4sHCoD3 2018
Special Mentions:
	PureHackers PH
	Blood Security Hackers
"""



import os
import sys
import platform
import webbrowser
import requests



def clear():
	if platform.system() == 'Linux':
		os.system('clear')
	elif platform.system() == 'Windows':
		os.system('cls')
	elif platform.system() == 'Darwin':
		os.system('clear')
	else:
		os.system('clear')



def banner():
	if platform.system() == 'Windows':
		print  ("""
 o-o               o         o  o          o                    o-o   o--o
o                  |         |  |          | /  o               |  \  |   |
|  -o o-o o-o o--o | o-o     O--O  oo  o-o OO     o-o  o--o     |   O O--o
o   | | | | | |  | | |-'     |  | | | |    | \  | |  | |  |     |  /  |   |
 o-o  o-o o-o o--O o o-o     o  o o-o- o-o o  o | o  o o--O     o-o   o--o
                 |                                        |
              o--o                                     o--o

Created By: Cr4sHCoD3 [ PureHackers | Blood Security Hackers ]
Github: https://github.com/cr4shcod3
		""")
	elif platform.system() == 'Linux' or platform.system() == 'Darwin':
		print  ("""
 o-o               o         o  o          o                    o-o   o--o
o                  |         |  |          | /  o               |  \  |   |
|  -o o-o o-o o--o | o-o     O--O  oo  o-o OO     o-o  o--o     |   O O--o
o   | | | | | |  | | |-'     |  | | | |    | \  | |  | |  |     |  /  |   |
 o-o  o-o o-o o--O o o-o     o  o o-o- o-o o  o | o  o o--O     o-o   o--o
                 |                                        |
              o--o                                     o--o

Created By: Cr4sHCoD3 [ PureHackers | Blood Security Hackers ]
Github: https://github.com/cr4shcod3
		""")
	else:
		print  ("""
 o-o               o         o  o          o                    o-o   o--o
o                  |         |  |          | /  o               |  \  |   |
|  -o o-o o-o o--o | o-o     O--O  oo  o-o OO     o-o  o--o     |   O O--o
o   | | | | | |  | | |-'     |  | | | |    | \  | |  | |  |     |  /  |   |
 o-o  o-o o-o o--O o o-o     o  o o-o- o-o o  o | o  o o--O     o-o   o--o
                 |                                        |
              o--o                                     o--o

Created By: Cr4sHCoD3 [ PureHackers | Blood Security Hackers ]
Github: https://github.com/cr4shcod3
		""")



def main():
	clear()
	banner()
	print ("""
[ Google Hacking Menu ]
\t01) Directory Listing
\t02) Configuration Files
\t03) Database Files
\t04) Log Files
\t05) Backup and Old Files
\t06) Login Pages
\t07) SQL Errors
\t08) Publicly Exposed Documents
\t09) phpinfo()
\t10) Google Hacking Database
\t99) Exit
\tOR) CTRL + C
	""")
	try:
		choice = int(input('Google_Hacking: '))
	except ValueError:
		print ('[+] - Please enter a valid integer.')
		main()
	except EOFError:
		print ('\n[+] - Exiting.')
		sys.exit()
	except KeyboardInterrupt:
		print ('\n[+] - Exiting.')
		sys.exit()
	if choice == 1:
		webbrowser.open_new_tab(google_hacking + 'site:' + url + '+intitle:index.of')
		main()
	elif choice == 2:
		webbrowser.open_new_tab(google_hacking + 'site:' + url + '+ext:xml+|+ext:conf+|+ext:cnf+|+ext:reg+|+ext:inf+|+ext:rdp+|+ext:cfg+|+ext:txt+|+ext:ora+|+ext:ini')
		main()
	elif choice == 3:
		webbrowser.open_new_tab(google_hacking + 'site:' + url + '+ext:sql+|+ext:dbf+|+ext:mdb')
		main()
	elif choice == 4:
		webbrowser.open_new_tab(google_hacking + 'site:' + url + '+ext:log')
		main()
	elif choice == 5:
		webbrowser.open_new_tab(google_hacking + 'site:' + url + '+ext:bkf+|+ext:bkp+|+ext:bak+|+ext:old+|+ext:backup')
		main()
	elif choice == 6:
		webbrowser.open_new_tab(google_hacking + 'site:' + url + '+inurl:login | admin | user | cpanel | account | moderator | /cp')
		main()
	elif choice == 7:
		webbrowser.open_new_tab(google_hacking + 'site:' + url + '+intext:"sql+syntax+near"+|+intext:"syntax+error+has+occurred"+|+intext:"incorrect+syntax+near"+|+intext:"unexpected+end+of+SQL+command"+|+intext:"Warning:+mysql_connect()"+|+intext:"Warning:+mysql_query()"+|+intext:"Warning:+pg_connect()"')
		main()
	elif choice == 8:
		webbrowser.open_new_tab(google_hacking + 'site:' + url + '+ext:doc+|+ext:docx+|+ext:odt+|+ext:pdf+|+ext:rtf+|+ext:sxw+|+ext:psw+|+ext:ppt+|+ext:pptx+|+ext:pps+|+ext:csv')
		main()
	elif choice == 9:
		webbrowser.open_new_tab(google_hacking + 'site:' + url + '+ext:php+intitle:phpinfo+"published+by+the+PHP+Group"')
		main()
	elif choice == 10:
		webbrowser.open_new_tab('https://www.exploit-db.com/google-hacking-database/')
	elif choice == 99:
		print ('\n[+] - Exiting.')
		sys.exit()
	else:
		print ('[!] - Unknown error has occured.')
		main()



if __name__ == '__main__':
	clear(); banner()
	print ('\n[#] - Checking Modules...')
	try:
		import requests
		print ('[+] - requests == OK!')
	except ImportError:
		raise ImportError('\n[!] - requests == NOT OK!')
	print ('\n[#] - Checking URL...')
	try:
		url = sys.argv[1]
		print ('[+] - URL == OK!')
		print ('URL: ' + url)
	except IndexError:
		print ('[!] - URL == NOT OK!')
		url = str(input('URL: '))
	if 'http://' not in url:
		hostname = url
		print ('[+] - URL == Adding http://')
		url = ('http://' + url)
		print ('URL: ' + url)
	elif 'http://' in url:
		hostname = url.replace('http://', '')
		url = url
	print ('[+] - Search Engine == SET!')
	google_hacking = 'https://www.google.com/search?q='
	main()
