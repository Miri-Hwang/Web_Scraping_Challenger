import requests
from bs4 import BeautifulSoup

URL = "http://www.alba.co.kr/"

result = requests.get(URL)
soup = BeautifulSoup(result.text, "html.parser")
brands = soup.find("div", {"id": "MainSuperBrand"}).find_all(
    "li", {"class": "impact"})

brand_list = []


def extract_brands(html):
    company = html.find("span", {"class": "company"}).get_text()
    company_url = html.find("a", {"class": "goodsBox-info"})["href"]
    return {'company': company, 'url': company_url}


def get_brands():
    for brand in brands:
        brand = extract_brands(brand)
        brand_list.append(brand)
    return brand_list


print(get_brands())
