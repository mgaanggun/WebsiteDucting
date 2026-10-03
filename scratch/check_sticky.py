import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
options.add_argument('--window-size=1440,1080')

driver = webdriver.Chrome(options=options)
try:
    driver.get("http://localhost:8080/produk-exhaust-hood.html")
    time.sleep(1)
    
    card = driver.find_element(By.CSS_SELECTOR, ".project-info-card")
    print("Initial card rect:", driver.execute_script("return arguments[0].getBoundingClientRect();", card))
    
    driver.execute_script("window.scrollTo({top: 600, behavior: 'instant'});")
    time.sleep(1)
    print("PageYOffset:", driver.execute_script("return window.pageYOffset;"))
    print("Card rect after scroll 600:", driver.execute_script("return arguments[0].getBoundingClientRect();", card))
    
finally:
    driver.quit()
