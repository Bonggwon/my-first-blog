import requests
from bs4 import BeautifulSoup

url = 'https://tutorial.djangogirls.org/en/django_models/'
res = requests.get(url)
soup = BeautifulSoup(res.text, 'lxml')

headings = soup.select('h2')
for heading in headings:
    print(heading.get_text(strip=True))
