import requests
from bs4 import BeautifulSoup

def fetch_headers(soup):
	header = soup.find_all("h2")
	for x in header:
		print(x.text)
	
if __name__ == "__main__":
	URL = 'https://www.online-convert.com/file-type'
	page = requests.get(URL)
	soup = BeautifulSoup(page.content,"html.parser")
	fetch_headers(soup)
