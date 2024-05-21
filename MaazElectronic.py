import requests
from bs4 import BeautifulSoup


def scrap_product(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    product_links = soup.find_all('a', {'rel': 'tag'})
    description = soup.find_all('div', {'class': 'type-product '})
    print(description)

    for image in product_links:
        print(image['href'])


scrap_product("https://maazelectronics.pk/product/")

def scrap_page(url):

    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    product_links = soup.find_all('a', {'rel': 'tag'})
    for image in product_links:
        print(image['href'])

scrap_page("https://maazelectronics.pk/shop")
