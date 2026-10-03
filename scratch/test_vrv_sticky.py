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
    driver.get("http://localhost:8080/produk-ducting-vrv.html")
    time.sleep(1)
    
    # Scroll down 500px
    driver.execute_script("window.scrollTo({top: 500, behavior: 'instant'});")
    time.sleep(0.5)
    
    sidebar = driver.find_element(By.CSS_SELECTOR, ".product-sticky-sidebar")
    rect = driver.execute_script("return arguments[0].getBoundingClientRect();", sidebar)
    print("VRV page at scroll 500px - sidebar rect:", rect)
    
    ss_path = "C:/Users/FERDY/.gemini/antigravity-ide/brain/c4eb0344-4332-4d17-a863-e218b8eb364a/test_vrv_sticky.png"
    driver.save_screenshot(ss_path)
    print("Screenshot saved to:", ss_path)
finally:
    driver.quit()
