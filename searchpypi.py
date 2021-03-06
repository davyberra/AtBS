#! python3
# searchpypi.py - Opens several search results simultaneously.

import requests, sys, webbrowser, bs4

print('Searching for ' + str(sys.argv[1])) # display text while downloading the search result page
res = requests.get('https://google.com/search?q=''https://pypi.org/search/?='
                   + ''.join(sys.argv[1:]))
res.raise_for_status()
print(sys.argv[1:])
# Retrieve top search result links.

soup = bs4.BeautifulSoup(res.text, 'html.parser')

# Open a browser tab for each result.
linkElems = soup.select('.package-snippet')
print(linkElems)
numOpen = min(5, len(linkElems))
for i in range(numOpen):
    urlToOpen = 'https://pypi.org' + linkElems[i].get('href')
    print('Opening', urlToOpen)
    webbrowser.open(urlToOpen)

