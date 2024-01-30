import requests
from bs4 import BeautifulSoup


# TODO 1 - Use BeautifulSoup to Scrape the Product Price
url = "https://www.amazon.com.br/Cafeteira-Espresso-Oster-Compacta-Perfect/dp/B0CB4SXZ82/ref=rvi_d_sccl_3/147-7681842-9031103?pd_rd_w=BjnG2&content-id=amzn1.sym.5a5fdb9d-0c9f-4ef8-98d5-3da45c0cade0&pf_rd_p=5a5fdb9d-0c9f-4ef8-98d5-3da45c0cade0&pf_rd_r=FHBXXXXMAKFGTTZEMFSW&pd_rd_wg=2EwQV&pd_rd_r=2ed5e33c-69d0-4a37-a48b-58f83909b024&pd_rd_i=B0CB4SXZ82&psc=1"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
           "Accept-Language": "pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7"}

response = requests.get(url=url, headers=headers)

soup = BeautifulSoup(response.content, "lxml")

item_price = soup.find(class_="a-offscreen").text
item_price = float("".join([item_price[2:-3].replace(".", ""), ".", item_price[-2:]]))
print(item_price)
