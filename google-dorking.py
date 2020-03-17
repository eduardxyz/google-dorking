#!/usr/bin/env python

"""
Copyright (C) 08 Feb 20: Eduard Marian

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.

    https://EduardMarian.xyz
    eduard_marian@protonmail.com
    Use at your own risk
"""

import requests, argparse, os, sys, platform, webbrowser

# ERROR PROOF FUNCTION TO SEE IF HASH PARAMETER IS website SHA1 or SHA256
def checkwebsite(cwebsite):
	try:
		if "http://" in cwebsite:
			return cwebsite
		elif "https://" in cwebsite:
			return cwebsite
		else:
			cwebsite = ("http://" + cwebsite)
			return cwebsite
	except Exception as Error:
			print(Error)

# ERROR PROOF FUNCTION TO SEE IF INPUT FILE EXISTS	
def checkfile(cfile):
	try:
		if os.path.isfile(cfile):
			return cfile
		else:
			print ("File %s is missing in your script directory." % (cfile))
			exit()
	except Exception as Error:
			print(Error)

# DORKING FUNCTION
def google_dorking(google, url, menu):

	if menu == '1':
		webbrowser.open_new_tab(google + 'site:' + url + '+intitle:index.of')
	elif menu == '2':
		webbrowser.open_new_tab(google + 'site:' + url + '+ext:xml+|+ext:conf+|+ext:cnf+|+ext:reg+|+ext:inf+|+ext:rdp+|+ext:cfg+|+ext:txt+|+ext:ora+|+ext:ini')
	elif menu == '3':
		webbrowser.open_new_tab(google + 'site:' + url + '+ext:sql+|+ext:dbf+|+ext:mdb')
	elif menu == '4':
		webbrowser.open_new_tab(google + 'site:' + url + '+ext:log')
	elif menu == '5':
		webbrowser.open_new_tab(google + 'site:' + url + '+ext:bkf+|+ext:bkp+|+ext:bak+|+ext:old+|+ext:backup')
	elif menu == '6':
		webbrowser.open_new_tab(google + 'site:' + url + '+inurl:login | admin | user | cpanel | account | moderator | /cp')
	elif menu == '7':
		webbrowser.open_new_tab(google + 'site:' + url + '+intext:"sql+syntax+near"+|+intext:"syntax+error+has+occurred"+|+intext:"incorrect+syntax+near"+|+intext:"unexpected+end+of+SQL+command"+|+intext:"Warning:+mysql_connect()"+|+intext:"Warning:+mysql_query()"+|+intext:"Warning:+pg_connect()"')
	elif menu == '8':
		webbrowser.open_new_tab(google + 'site:' + url + '+ext:doc+|+ext:docx+|+ext:odt+|+ext:pdf+|+ext:rtf+|+ext:sxw+|+ext:psw+|+ext:ppt+|+ext:pptx+|+ext:pps+|+ext:csv')
	elif menu == '9':
		webbrowser.open_new_tab(google + 'site:' + url + '+ext:php+intitle:phpinfo+"published+by+the+PHP+Group"')
	else:
		print ("[ UNKNOWN ERROR ]")

def Main():
	parser = argparse.ArgumentParser(description="Google Dorking is a computer hacking technique that uses Google Search and other Google Applications to find security holes in the configuration and computer code that websites use.", formatter_class=argparse.RawTextHelpFormatter)
	parser.add_argument("-d", "--dorks", required=True, 
		help="01: Directory Listing \n02: Configuration Files \n03: Database Files \n04: Log Files \n05: Backup and Old Files \n06: Login Pages \n07: SQL Errors \n08: Publicly Exposed Document \n09: PHP Information ")
	parser.add_argument("-i", "--input", type=checkfile, required=False, help="Input File Location (EX: /Path/To/input.txt)")
	parser.add_argument("-w", "--website", type=checkwebsite, required=False, help="Single website (EX: http://example.com)")
	args = parser.parse_args()

	google_url = "https://www.google.com/search?q="

	# SINGLE WEBSITE FUNCTION
	if args.website and args.dorks:
		google_dorking(google_url, args.website, args.dorks)

	# MULTIPLE WEBSITE FUNCTION
	elif args.input and args.dorks:
		with open(args.input) as o:
			for line in o.readlines():
				google_dorking(google_url, line, args.dorks)

if __name__ == "__main__":
	Main()

