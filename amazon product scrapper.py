from selenium import webdriver
from selenium.webdriver.common.by import By

keyword = "latest smartphone"

driver = webdriver.Chrome()
driver.get('https://www.amazon.in/s?hidden-keywords=B0C7QS9M38+%7C+B08TV2P1N8+%7C+B09N3ZNHTY+%7C+B07PR1CL3S+%7C+B0BSGQTVP1+%7C+B0BKG5PQ6T+%7C+B0CC8VF47L+%7C+B09YRYCWF8+%7C+B0BW8TXJJ2+%7C+B0BW9NWMPL+%7C+B08JQN8DGZ+%7C+B0BZ4DJ7GZ+%7C+B071Z8M4KX+%7C+B0BKZFKQ3G+%7C+B0BVRDWC9C+%7C+B09LHXTXMX+%7C+B0BYZ26QGB+%7C+B09NYK3CF2+%7C+B0CC5VH2LW+%7C+B09MTRDQB5+%7C+B0BBTYDK6Y+%7C+B0C7CNFKJ3+%7C+B08MSYDMZ7+%7C+B08JMC1988+%7C+B09GFRV7L5+%7C+B09X74RB6D+%7C+B0BTDNZQWJ+%7C+B072PQRS12+%7C+B0856HNMR7+%7C+B07KXR889N+%7C+B01FSYQ2A4+%7C+B08CVTJ7NJ+%7C+B07T2CZCMR+%7C+B0B4NW64R1+%7C+B07NBWT3Z2+%7C+B08H9Z3XQW+%7C+B0BBVBCL3F+%7C+B07SMH67DJ+%7C+B0C7QWGZ6Z+%7C+B01J82IYLW+%7C+B08JM7X6RY+%7C+B0B12Q8K2X+%7C+B0BR5CMNNT+%7C+B0BBTYBLJV+%7C+B01MF8MB65+%7C+B08CVTT65T+%7C+B09JGRDGDG+%7C+B0BTDRVFW1+%7C+B0BZHRB9J1+%7C+B0C592CYFJ&_encoding=UTF8&content-id=amzn1.sym.9c8f8322-71f0-487d-87cc-e704eb7c4ec9&pd_rd_r=39d89d13-d28f-4c3e-a170-7280f89c04af&pd_rd_w=xzweg&pd_rd_wg=eMnaF&pf_rd_p=9c8f8322-71f0-487d-87cc-e704eb7c4ec9&pf_rd_r=2STERX59YREQT847D3VG&ref=pd_gw_unk')
driver.maximize_window()

driver.find_element(By.XPATH, "/html/body/center/p[2]/font/b/a").click()

# Clicking on the search bar
search_bar = driver.find_element(By.ID, 'twotabsearchtextbox')
search_bar.send_keys(keyword)
search_button = driver.find_element(By.ID, "nav-search-submit-button")
search_button.click()

items_data = []

# Scrape data from the next 5 items
items = driver.find_elements(By.CSS_SELECTOR, 'div.s-result-item[data-asin]')[2:7]

for index, item in enumerate(items):
    item_details = {}
    
    # Scraping Name
    name_element = item.find_element(By.CSS_SELECTOR, 'span.a-size-medium.a-color-base.a-text-normal')
    item_details['Name'] = name_element.text if name_element else 'Name not available'
    
    # Scraping Price
    price_element = item.find_element(By.CSS_SELECTOR, 'span.a-price-whole')
    price = price_element.text if price_element else 'Price not available'
    item_details['Price'] = price
    
    # Scraping Ratings
    ratings_element = item.find_element(By.CSS_SELECTOR, 'div.a-row.a-size-small span')
    ratings = ratings_element.get_attribute('aria-label') if ratings_element else ''
    item_details['Rating'] = float(ratings[:3]) if ratings else 0.0

    # Append item details to the list
    items_data.append(item_details)

highest_rating = 0
highest_rated_item_number = 0

# Printing the scraped data
for i, item in enumerate(items_data, start=1):
    print()
    print(f"Item {i} Details:")
    print(f"Name: {item.get('Name')}")
    print(f"Price: Rs. {item.get('Price')}")
    print(f"Rating: {item.get('Rating')} / 5.0")
    print()


driver.quit()

