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
    
    sidebar = driver.find_element(By.CSS_SELECTOR, ".product-sticky-sidebar")
    
    for scroll_y in [0, 200, 400, 600, 800, 1000]:
        driver.execute_script(f"window.scrollTo({{top: {scroll_y}, behavior: 'instant'}});")
        time.sleep(0.3)
        rect = driver.execute_script("return arguments[0].getBoundingClientRect();", sidebar)
        print(f"Scroll {scroll_y}: sidebar top = {rect['top']}, bottom = {rect['bottom']}, height = {rect['height']}")
        
    # Capture screenshot while scrolled at 600px
    driver.execute_script("window.scrollTo({top: 600, behavior: 'instant'});")
    time.sleep(0.5)
    ss_path = "C:/Users/FERDY/.gemini/antigravity-ide/brain/c4eb0344-4332-4d17-a863-e218b8eb364a/test_sticky_scrolled.png"
    driver.save_screenshot(ss_path)
    print("Screenshot saved to:", ss_path)
finally:
    driver.quit()
