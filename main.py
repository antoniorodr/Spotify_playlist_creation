import requests
from bs4 import BeautifulSoup

# user_input = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD:: ")

header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"}

# URL = f"https://www.billboard.com/charts/hot-100/{user_input}/"
URL = "https://www.billboard.com/charts/hot-100/2024-08-03/"


response = requests.get(URL, headers = header)
website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")

print(soup.prettify())
