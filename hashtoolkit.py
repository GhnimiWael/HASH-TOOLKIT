import requests
import sys

from bs4 import BeautifulSoup

print("""

██╗░░██╗░█████╗░░██████╗██╗░░██╗░░░░░░████████╗░█████╗░░█████╗░██╗░░░░░██╗░░██╗██╗████████╗
██║░░██║██╔══██╗██╔════╝██║░░██║░░░░░░╚══██╔══╝██╔══██╗██╔══██╗██║░░░░░██║░██╔╝██║╚══██╔══╝
███████║███████║╚█████╗░███████║█████╗░░░██║░░░██║░░██║██║░░██║██║░░░░░█████═╝░██║░░░██║░░░
██╔══██║██╔══██║░╚═══██╗██╔══██║╚════╝░░░██║░░░██║░░██║██║░░██║██║░░░░░██╔═██╗░██║░░░██║░░░
██║░░██║██║░░██║██████╔╝██║░░██║░░░░░░░░░██║░░░╚█████╔╝╚█████╔╝███████╗██║░╚██╗██║░░░██║░░░
╚═╝░░╚═╝╚═╝░░╚═╝╚═════╝░╚═╝░░╚═╝░░░░░░░░░╚═╝░░░░╚════╝░░╚════╝░╚══════╝╚═╝░░╚═╝╚═╝░░░╚═╝░░░
                                        BY: W43L
                                BASED ON: Hashtoolkit.com
                                       Version: 0.1
""")

hash = sys.argv
if sys.argv[1] == "-h":
    print("Usage: python3 hashtoolkit.py <yourhash>")
    print(""" Hash Toolkit Support:  
    md5 hash, sha1 hash, sha256 hash, sha384 hash, sha512 hash and many more.""")
else:
    url = "https://hashtoolkit.com:443/decrypt-hash/?hash="+sys.argv[1]
    header = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8", "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate", "Referer": "https://hashtoolkit.com/", "Upgrade-Insecure-Requests": "1", "Te": "trailers"}
    response = requests.get(url, headers=header)

    soup = BeautifulSoup(response.text, 'html.parser')
    
    for link in soup.find_all('a'):
        #print(link.get('href'))
        if "/generate-hash/?text=" in link.get('href'):
            dehashed = link.get('href')
            print("\n"+str(sys.argv[1])+":"+str(dehashed[21:]))
            break
