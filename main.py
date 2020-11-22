import requests
from bs4 import BeautifulSoup

def fetchExtension(header):
    #Find the child tag
    data = header.find_next_sibling()
    #Search for all hyperlinks
    extension = data.find_all("a")
    #clean extension
    cleanExtension = [header.text]
    for x in extension:
        cleanExtension.append(x.text.strip())
    return cleanExtension

if __name__ == "__main__":
    URL = 'https://www.online-convert.com/file-type'
    page = requests.get(URL)
    soup = BeautifulSoup(page.content,"html.parser")
    header = soup.find_all("h2")[1:]
    arr = []
    for x in range(len(header)):
        arr.append(fetchExtension(header[x]))
    print(arr)
        