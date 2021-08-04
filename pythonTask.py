import requests
from bs4 import BeautifulSoup

url = 'https://en.wikipedia.org/wiki/Quantum_mechanics'
res = requests.get(url)
html_page = res.content
soup = BeautifulSoup(html_page, 'html.parser')
html_text = soup.find_all(text=True)

f = open("html_text.txt", "w", encoding="utf-8")         # Creating html_text.txt File

for line in html_text:
	f.write(line)

f.close() 