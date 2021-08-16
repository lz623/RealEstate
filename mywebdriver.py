import requests
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# from webdriver_manager.chrome import ChromeDriverManager

def get_soup(url, driver_type='requests'):
    """
    There are different ways to run http request. 
    Requests is the python built-in library.
    Selenium uses a webdriver which mimic the behavior of a browser
    """
    if driver_type == 'requests':
        user_agents = ['Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36']
        headers = {
            'authority': 'scrapeme.live',
            'dnt': '1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'sec-fetch-site': 'none',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-user': '?1',
            'sec-fetch-dest': 'document',
            'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
        }
        page = requests.get(url, headers=headers)
        soup = BeautifulSoup(page.content, 'html.parser')
        return soup
    elif driver_type == 'selenium':
        driver = webdriver.Chrome()
        # driver = webdriver.Chrome(ChromeDriverManager(version="91.0.4472.164").install())
        # driver.implicitly_wait(10)
        driver.get(url)
        
        # delay = 10
        # text_exist = EC.text_to_be_present_in_element((By.ID, "product_price"), 'U')
        # text_exist = EC.presence_of_element_located((By.XPATH, "//span[@id='product_price' and ( contains(text(),'USD') or contains(text(),'On request') )]"))
        # WebDriverWait(driver, delay).until(text_exist)
        
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        driver.quit()
        return soup
    else:
        raise Exception('Wrong webdriver type')
    