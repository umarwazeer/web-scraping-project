import requests
from bs4 import BeautifulSoup

URL = "https://maazelectronics.pproduct-short-descriptionk/"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")
results = soup.find_all("div", calss="product-short-description")

response = results.text
# response = results.text
print(results)


def product_page(text, price):
    print("dash")


# for link in links:
#     product_link = results.text

page_images = soup.find_all("img",
                            src="https://maazelectronics.pk/wp-content/uploads/2019/09/775-motor-chuck-scaled-300x300.jpg")

