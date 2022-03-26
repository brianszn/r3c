# r3c
Basic information gathering tool, only for study.

  --scrap SCRAP        [With http/https] - Basic URL scraping <br>
  --iplookup IPLOOKUP  [Without http/https] - Reverse iplookup [HackerTarget API ] <br>
  --vhosts VHOSTS      [Without http/https] - Get subdomains vhosts [HackerTarget API ]<br>
  --whois WHOIS        [Without TOR] - Whois website
  
  Example scrap: python3 r3c.py --scrap http://testphp.vulnweb.com/<br>
  
  Example iplookup: python3 r3c.py --iplookup testphp.vulnweb.com<br>
  
  Example vhots: python3 r3c.py --vhosts vulnweb.com<br>
  
  Example whois: python3 r3c.py --whois http://testphp.vulnweb.com/
