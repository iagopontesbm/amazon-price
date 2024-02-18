import requests
from bs4 import BeautifulSoup
import email_send as email


# TODO 1 - Use BeautifulSoup to Scrape the Product Price
URL = "https://www.amazon.com.br/Headphone-Ouvido-HV-H2002d-Microfone-Falante/dp/B07Y2G7VX5?th=1"
HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
           "Accept-Language": "pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7"}

response = requests.get(url=URL, headers=HEADERS)

soup = BeautifulSoup(response.content, "lxml")

item_price = soup.find(class_="a-offscreen").text
item_price = float("".join([item_price[2:-3].replace(".", ""), ".", item_price[-2:]]))

print(item_price)

target_price = 226.0

email_body = f""" O item Headphone Fone de Ouvido Havit HV-H2002d esta com preço desejado.\n 
Preço agora: {item_price}\n
link: {URL}"""

if item_price <= target_price:
    email.send_email(email_body)
