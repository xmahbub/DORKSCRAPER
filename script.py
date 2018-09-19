from bs4 import BeautifulSoup
import urllib.request
import urllib.parse

print ("""
\033[32m
================================================================================
                     \033[34m   The GOOGLE DORK SCRAPER 
\033[32m
 ____   ___  ____  _  _ ____   ____ ____     _    ____  _____ ____  
|  _ \ / _ \|  _ \| |/ / ___| / ___|  _ \   / \  |  _ \| ____|  _ \ 
| | | | | | | |_) | ' /\___ \| |   | |_) | / _ \ | |_) |  _| | |_) |
| |_| | |_| |  _ <| . \ ___) | |___|  _ < / ___ \|  __/| |___|  _ < 
|____/ \___/|_| \_|_|\_|____/ \____|_| \_/_/   \_|_|   |_____|_| \_\
                                                                                                                                    
	  		\033[35m Coded by Gπ33nK!D \033[0m 
================================================================================
\033[0m """)


url=input(str('Search me, I am Google:'))
values={'q':url}
data=urllib.parse.urlencode(values)
extra=str('&ei=xomrWqLjLcPQ0gS05o_gCA&start=')
ix=0
z=int(input('How many pages do you want to scrape:'))
while ix <= z-1:
      url = 'https://www.google.com/search?' + data + extra + str(ix) + '0&sa=N'
      ix = ix + 1

      headers = {}
      headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686)"
      req = urllib.request.Request(url, headers=headers)

      resp = urllib.request.urlopen(req)

      resp_data = resp.read()
      soup = BeautifulSoup(resp_data, "lxml")
      clean = soup.prettify()
      gdata = soup.find_all('h3', {'class': 'r'})
      for link in gdata:
            word = link.find('a')
            m = word.get("href")
            print('www.google.com'+m )