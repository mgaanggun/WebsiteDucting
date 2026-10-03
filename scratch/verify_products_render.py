import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

options = Options()
options.add_argument("--headless=new")
options.add_argument("--window-size=1400,1000")

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

try:
    # 1. Test products.html (Catalog)
    driver.get("http://localhost:8080/products.html")
    time.sleep(2)
    driver.save_screenshot("C:/Users/FERDY/.gemini/antigravity-ide/brain/c4eb0344-4332-4d17-a863-e218b8eb364a/test_products_catalog.png")
    
    # 2. Test produk-exhaust-hood.html
    driver.get("http://localhost:8080/produk-exhaust-hood.html")
    time.sleep(2)
    driver.save_screenshot("C:/Users/FERDY/.gemini/antigravity-ide/brain/c4eb0344-4332-4d17-a863-e218b8eb364a/test_produk_exhaust_hood.png")

    # 3. Test produk-cleanroom-ducting-pu.html
    driver.get("http://localhost:8080/produk-cleanroom-ducting-pu.html")
    time.sleep(2)
    driver.save_screenshot("C:/Users/FERDY/.gemini/antigravity-ide/brain/c4eb0344-4332-4d17-a863-e218b8eb364a/test_produk_cleanroom_pu.png")

    print("Product pages screenshots captured successfully!")

finally:
    driver.quit()
