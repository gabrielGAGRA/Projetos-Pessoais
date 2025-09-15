import requests
from bs4 import BeautifulSoup

# URL of the main page
main_url = 'https://www.pine.com/'

# Fetch the main page
response = requests.get(main_url)
soup = BeautifulSoup(response.content, 'html.parser')

# Find all buttons (assuming they are <a> tags with a specific class or attribute)
buttons = soup.find_all('a', class_='child-link flex items-center gap-1 text-lg py-1 pointer-events-auto')

# Extract URLs from the buttons
urls = [button['href'] for button in buttons]

# Print the extracted URLs
for url in urls:
    print(url)