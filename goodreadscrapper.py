from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import json
import time

# Set up the Selenium WebDriver with Service
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

base_url = "https://www.goodreads.com/author/quotes/6567971.Lana_Del_Rey?page="
quotes_data = []

for page_num in range(1, 13):
    url = base_url + str(page_num)
    driver.get(url)
    time.sleep(3)  

    soup = BeautifulSoup(driver.page_source, 'html.parser')

    quotes = soup.find_all('div', class_='quoteDetails')
    for quote in quotes:
        quote_text = quote.find('div', class_='quoteText').get_text(strip=True)
        tags = [tag.get_text() for tag in quote.find_all('a', class_='smallText')]

        quotes_data.append({
            "quote": quote_text,
            "tags": tags
        })

with open('lana_del_rey_quotes.json', 'w') as file:
    json.dump(quotes_data, file, indent=4)

print(f"{len(quotes_data)}saved to 'lana_del_rey_quotes.json'")

driver.quit()
