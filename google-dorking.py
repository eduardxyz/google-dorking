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

# ERROR PROOF FUNCTION TO SEE IF INPUT FILE EXISTS	
def checkdorks(cdorks):
	try:
		if os.path.isfile(cdorks):
			return cdorks
		else:
			print ("File %s is missing in your script directory." % (cdorks))
			exit()
	except Exception as Error:
			print(Error)

# DORKING FUNCTION
def google_dorking(google, url, dorks):
	if url:
		webbrowser.open_new_tab(google + 'site:' + url + '+' + dorks)
	else:
		webbrowser.open_new_tab(google + dorks)


# DORKING FUNCTION
def google_dorking_else(google, dorks):
	
	webbrowser.open_new_tab(google + dorks)

def Main():
	parser = argparse.ArgumentParser(description="Google Dorking is a computer hacking technique that uses Google Search and other Google Applications to find security holes in the configuration and computer code that websites use.", formatter_class=argparse.RawTextHelpFormatter)
	parser.add_argument("-d", "--dorks", type=checkdorks, required=False, help="Input Dorks File Location (EX: /Path/To/droks.txt)")
	parser.add_argument("-w", "--website", type=checkwebsite, required=False, help="Single website (EX: http://example.com)")
	args = parser.parse_args()

	google_url = "https://www.google.com/search?q="

	# WEBSITE FUNCTION
	if args.website and args.dorks:
		with open(args.dorks) as o:
			for line in o.readlines():
				google_dorking(google_url, args.website, line)

	# NO WEBSITE
	else:
		with open(args.dorks) as o:
			for line in o.readlines():
				google_dorking(google_url, None, line)


if __name__ == "__main__":
	Main()

