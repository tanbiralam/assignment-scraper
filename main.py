from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import json
import time

chrome_driver_path = "chromedriver/chromedriver.exe"

chrome_options = Options()
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--start-maximized")

service = Service(chrome_driver_path)

driver = webdriver.Chrome(service=service, options=chrome_options)

url = "https://www.otipy.com/category/vegetables-1"

driver.get(url)

time.sleep(2)

last_height = driver.execute_script("return document.body.scrollHeight")
while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(1)
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

html = driver.page_source

soup = BeautifulSoup(html, 'html.parser')

driver.quit()

product_list = soup.find_all('div', class_='style_card__v4i84')

products = []

for product in product_list:
    name = product.find('h3', class_='style_prod_name__QllSp')
    selling_price = product.find('span', class_='style_selling_price__GaIsF')
    standard_price = product.find('span', class_='style_striked_price__4ghn5')
    final_price = product.find('p', class_='style_final_price__FERLK')
    quantity = product.find('span', class_='style_prod_qt__cXcqe')

    product_data = {
        "Name": name.text.strip() if name else "N/A",
        "Standard Price": selling_price.text.strip().replace('/pc', '') if selling_price else "N/A",
        "Selling Price": standard_price.text.strip() if standard_price else "N/A",
        "MRP": final_price.text.strip().split()[0] if final_price else "N/A",
        "Quantity": quantity.text.strip() if quantity else "N/A"
    }

    products.append(product_data)

print(json.dumps(products, indent=4))

with open('products.json', 'w') as json_file:
    json.dump(products, json_file, indent=4)

print("Data successfully saved to products.json")
