import os
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
    url = "http://localhost:8080/produk-exhaust-hood.html"
    driver.get(url)
    time.sleep(2)
    
    # Find CTA button
    btn = driver.find_element(By.CSS_SELECTOR, ".project-cta .btn-main")
    print("Button text:", btn.text)
    print("Button href:", btn.get_attribute("href"))
    print("Button target:", btn.get_attribute("target"))
    
    # Scroll to the button
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", btn)
    time.sleep(1)
    
    # Screenshot element or section
    card = driver.find_element(By.CSS_SELECTOR, ".project-info-card")
    screenshot_path = "C:/Users/FERDY/.gemini/antigravity-ide/brain/c4eb0344-4332-4d17-a863-e218b8eb364a/test_wa_button.png"
    card.screenshot(screenshot_path)
    print("Screenshot saved to:", screenshot_path)

finally:
    driver.quit()
