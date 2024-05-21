import requests
from bs4 import BeautifulSoup


def scrap_product(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    got_links = soup.find_all('a', {'class': 'product-item-link'})
    got_price = soup.find_all("span", {"class": "price-container"})
    # specifications = soup.find_all("a", {"class": "data"})
    images = soup.find_all("img", {"class": "product-image-photo"})
    # print(image)
    # print(specifications)
    for image in images:
        print(image['data-amsrc'])
    for a in got_links:
        print(a["href"])
        print(a.text)
    for i in got_price:
        print(i.text)


scrap_product("https://myshop.pk/mobiles-smartphones-tablets/wearable-gadgets")


def scrap_page(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    got_links = soup.find_all('a', {'class': 'image-link'})

    for a in got_links:
        print(a['href'])
        # print(a.text)


scrap_page("https://myshop.pk/")
