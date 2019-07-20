# 함수 function crawl하는 함수를 만들어 보세요
# 이름crawl -> url을 받아서 pageString return
# parse(pageString) -> list []

import requests
from bs4 import BeautifulSoup

def crawl(url):
    data = requests.get(url)
    print(data, url)
    return data.content

# li -> {} productInfo not productInfos
def getProductInfo(li):
    img = li.find("img")
    name = img["alt"]

    priceReload = li.find("span", {"class":"_price_reload"})
    price = priceReload.text

    productInfo = {"name":name, "price":price} # dictionary 딕셔너리
    return productInfo

def parse(pageString):
    bsObj = BeautifulSoup(pageString, "html.parser")
    ul = bsObj.find("ul", {"class":"goods_list"})
    lis = ul.findAll("li", {"class":"_itemSection"})
    productInfos = []
    for li in lis:
        try:
            productInfo = getProductInfo(li)
            productInfos.append(productInfo)
        except:
            # print("----")
            print(end="")

    return productInfos

result = []
for pageNo in range(1, 2 + 1):

    url = "https://search.shopping.naver.com/search/all.nhn?origQuery=%EC%97%90%EC%96%B4%EC%BB%A8&pagingIndex={}&pagingSize=80&viewType=list&sort=rel&frm=NVSHPAG&query={}".format("냉장고",pageNo)
    # html, http, python, 자료구조
    pageString = crawl(url)
    productInfos = parse(pageString)

    for productInfo in productInfos:
        result.append(productInfo)

for info in result:
    print(info["name"]+"#"+info["price"])



