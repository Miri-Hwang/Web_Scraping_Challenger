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


# 하나의 브랜드 채용 리스트를 산출하는 함수
def get_job_details(jobs):
    job_list = []
    for job in jobs:
        place = job.find('td', {'class': 'local first'}
                         ).get_text().replace('\xa0', ' ')

        title = job.find('td', {'class': 'title'}).find(
            'span', {'class': 'company'}).get_text()
        time = job.find('td', {'class': 'data'}).find(
            'span', {'class': 'time'})
        if time is None:
            time = "시간 협의"
        else:
            time = time.get_text()
        pay_icon = job.find('td', {'class': 'pay'}).find(
            'span', {'class': 'payIcon'}).get_text()
        pay_number = job.find('td', {'class': 'pay'}).find(
            'span', {'class': 'number'}).get_text()
        date = job.find('td', {'class': 'last'}).find('strong')
        if date is None:
            date = job.find('td', {'class': 'last'}).string
        else:
            date = str(date).replace('<strong>', '').replace('</strong>', '')
        job_list.append({'place': place, 'title': title, 'time': time,
                         'pay_icon': pay_icon, 'pay_number': pay_number, 'date': date})

    return job_list

# 브랜드 url을 넣으면, 해당 브랜드의 채용 리스트를 반환


def get_jobs(url):
    result = requests.get(url)
    soup = BeautifulSoup(result.text, "html.parser")
    jobs = soup.find('div', {'id': 'NormalInfo'}).find(
        "table").find('tbody').find_all('tr', {'class': ['', 'divide']})

    job_list = get_job_details(jobs)
    return job_list


# 메인 페이지에서 브랜드 리스트 추출
brands = get_brands()

# 각 브랜드 별 채용 리스트 추출
for brand in brands:
    company = brand['company']
    url = brand['url']
    print(get_jobs(url))  # 각 브랜드의 채용 리스트 반환
