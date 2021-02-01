import requests
from bs4 import BeautifulSoup

URL = "http://www.alba.co.kr/"


def extract_brands(html):
    company = html.find("span", {"class": "company"}).get_text()
    company_url = html.find("a", {"class": "goodsBox-info"})["href"]
    return {'company': company, 'url': company_url}

# 메인 페이지에서 슈퍼 채용 브랜드 리스트를 얻는 함수


def get_brands():
    result = requests.get(URL)
    soup = BeautifulSoup(result.text, "html.parser")
    brands = soup.find("div", {"id": "MainSuperBrand"}).find_all(
        "li", {"class": "impact"})
    brand_list = []
    for brand in brands:
        brand = extract_brands(brand)
        brand_list.append(brand)
    return brand_list


brands = get_brands()
