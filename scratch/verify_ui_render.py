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
    # 1. Test index.html
    driver.get("http://localhost:8080/index.html")
    time.sleep(2)
    driver.save_screenshot("C:/Users/FERDY/.gemini/antigravity-ide/brain/c4eb0344-4332-4d17-a863-e218b8eb364a/test_index_top.png")
    
    # Scroll to CTA & footer
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(1)
    driver.save_screenshot("C:/Users/FERDY/.gemini/antigravity-ide/brain/c4eb0344-4332-4d17-a863-e218b8eb364a/test_index_footer.png")

    # 2. Test services.html
    driver.get("http://localhost:8080/services.html")
    time.sleep(1)
    driver.save_screenshot("C:/Users/FERDY/.gemini/antigravity-ide/brain/c4eb0344-4332-4d17-a863-e218b8eb364a/test_services.png")

    # 3. Test ducting-exhaust.html
    driver.get("http://localhost:8080/ducting-exhaust.html")
    time.sleep(1)
    driver.save_screenshot("C:/Users/FERDY/.gemini/antigravity-ide/brain/c4eb0344-4332-4d17-a863-e218b8eb364a/test_exhaust.png")

    print("Screenshots captured successfully!")

finally:
    driver.quit()
