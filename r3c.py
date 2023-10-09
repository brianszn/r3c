try:
	import urllib3 
except:
	print('\n [ ? ] Please, pip install urllib3')
try:
	import sys
except:
	print('\n [ ? ] Please, pip install sys')
try:
	import argparse
except:
	print('\n [ ? ] Please, pip install argparse')
try:
	import whois
except:
	print('\n [ ? ] Please, pip install python-whois')
try:
	from colorama import Fore,Back,Style
except:
	print('\n [ ? ] Please, pip install colorama')
try:
	from bs4 import BeautifulSoup
except:
	print('\n [ ? ] Please, pip install BeautifulSoup4')
try: 
	import requests as r
except:
	print('\n [ ? ] Please, pip install requests')

print(r""" - Basic tool for study
───▐▀▄───────▄▀▌───▄▄▄▄▄▄▄───24/03/22──
───▌▒▒▀▄▄▄▄▄▀▒▒▐▄▀▀▒██▒██▒▀▀▄──────────
──▐▒▒▒▒▀▒▀▒▀▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▀▄────────
──▌▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▄▒▒▒▒▒▒▒▒▒▒▒▒▀▄────── 
▀█▒▒▒█▌▒▒█▒▒▐█▒▒▒▀▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▌─────  
▀▌▒▒▒▒▒▒▀▒▀▒▒▒▒▒▒▀▀▒▒▒▒▒▒▒▒▒▒▒▒▒▒▐───▄▄		  
▐▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▒█▀─	 
▐▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▀───
▐▒▒▒▒▒▒▒▒▒Information Gathering▒▒▌────   
─▌▒▒▒▒▒▒▒▒▒▒▒▒Tool▒▒▒▒▒▒▒▒▒▒▒▒▒▒▐─────   
─▐▒▒▒▒▒▒▒▒▒▒By braian 	       ▒▌─────
──▐▄▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▄▌──────
────▀▄▄▀▀▀▀▀▄▄▀▀▀▀▀▀▀▄▄▀▀▀▀▀▄▄▀────────

 ► Github: github.com/brianszn
 ► Use: python3 r3c.py -h

 Use with inteligence and obtain great results :)
""")

parser = argparse.ArgumentParser()
parser.add_argument('--scrap', action='store', help='[With http/https] - Basic URL scraping')
parser.add_argument('--iplookup', action='store', help='[Without http/https] - Reverse iplookup [HackerTarget API ]')
parser.add_argument('--vhosts', action='store', help='[Without http/https] - Get subdomains vhosts [HackerTarget API ]')
parser.add_argument('--whois', action='store', help='[Without TOR] - Whois website')
args = parser.parse_args()

paths = []
path_without_http = []
path_with_http = []
full = []

def scraping():

	url = sys.argv[2]

	urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

	def gethref(web):
		try:
			global soup;
			soup = BeautifulSoup(r.get(web).text, 'html.parser')
			for links in soup.find_all('a'):
				path = links.get('href')
				paths.append(path)
		except:
			print(Fore.RED+'[+] Failed to establish a new connection, try again OR check target.\n')
			quit()
	gethref(url)

	print(Fore.GREEN+'\n[*]' + Fore.WHITE +' - Web Scraping [URLS] - '+Fore.GREEN+'[*]\n')

	 
	for i in range(len(paths)):
		if paths[i] == None:
			paths[i] = '#'
		elif paths[i].startswith('http'):
			path_with_http.append(paths[i])		
		elif not paths[i].startswith('http'):
			link = f'{url}{paths[i]}'
			path_without_http.append(link)					
			

	for baby in list(set(path_without_http)):
		full.append(baby)
	for baby in list(set(path_with_http)):
		full.append(baby)
	for baby in range(len(path_without_http)):
		gethref(path_without_http[baby])


	for i in range(len(list(paths))):
		if paths[i] == None:
			paths[i] = '#'
	for nothttp in (paths):	
		if not nothttp.startswith('http'):
			link = f'{url}{nothttp}'
			full.append(link)

	ext = ['pdf', 'png', 'jpg', 'mp3', 'mp4', 'doc', 'lsx', 'ocx', 'exe', 'rar', 'zip']
	for webs in list(set(full)):
		try:
			boraver = (webs[-3::].lower() in ext)
			if not boraver:
				if r.get(webs, verify=False, timeout=5):
					print(Fore.GREEN + '[+] - ' + Fore.WHITE, webs)
		except:
			pass

def hostsearch():
	vhosts = r.get(f'https://api.hackertarget.com/hostsearch/?q={sys.argv[2]}').text
	vhosts = vhosts.replace(',', ' ')
	vhosts = vhosts.split()
	i=0
	while i < len(vhosts):
		print(Fore.GREEN + '[+] - ' + Fore.WHITE, vhosts[i])		
		i = i+2

def reverseip():
	lokuup = r.get(f'https://api.hackertarget.com/reverseiplookup/?q={sys.argv[2]}').text
	lokuup = lokuup.split()
	for i in range(len(lokuup)):
		print(Fore.GREEN + '[+] - ' + Fore.WHITE, lokuup[i])


if args.scrap:
	scraping()

elif args.whois:
	print(Fore.GREEN+'\n[*]' + Fore.WHITE +' - WHOIS - '+Fore.GREEN+'[*]\n')
	consult = whois.whois(sys.argv[2])
	print(consult)

elif args.vhosts:
	print(Fore.GREEN+'\n[*]' + Fore.WHITE +' - VHOSTS - '+Fore.GREEN+'[*]\n')
	hostsearch()
elif args.iplookup:
	print(Fore.GREEN+'\n[*]' + Fore.WHITE +' - REVERSE IP DOMAIN CHECK - '+Fore.GREEN+'[*]\n')
	reverseip()
