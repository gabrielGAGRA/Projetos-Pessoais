import requests
from bs4 import BeautifulSoup

main_url = 'https://www.pine.com/'

response = requests.get(main_url)
soup = BeautifulSoup(response.content, 'html.parser')

buttons = soup.find_all('a', class_='child-link flex items-center gap-1 text-lg py-1 pointer-events-auto')

urls = [button['href'] for button in buttons]

for url in urls:
    print(url)