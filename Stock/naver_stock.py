import requests
from bs4 import BeautifulSoup

def get_obj(code):
    url = "https://finance.naver.com/item/main.nhn?code=005930" #+ code
    result = requests.get(url)
    obj = Beautifulsoup(result.content, "html.parser")
    return obj

def get_price(code):
    obj = get_obj (code)
    no_today = obj.find("p", {"class":"no_today"})
    blind_now = no_today.find("span",{"class":"blind"})
    return blind_now.text

while True:
#삼성전자 005930
    print("삼성전자 현재가")
    print(get_price("005930"))
    print()


