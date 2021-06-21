import requests
from bs4 import BeautifulSoup

url = "https://finance.naver.com/item/main.nhn?code=005930"
result = requests.get(url)
obj = BeautifulSoup(result.cotent, "html.parser")

print(obj)







