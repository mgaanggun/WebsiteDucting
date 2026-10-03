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
    for page in ["index.html", "produk-exhaust-hood.html", "services.html"]:
        driver.get(f"http://localhost:8080/{page}")
        time.sleep(1)
        footer = driver.find_element(By.CSS_SELECTOR, "#footer")
        driver.execute_script("arguments[0].scrollIntoView();", footer)
        time.sleep(0.5)
        name = page.replace(".html", "")
        ss_path = f"C:/Users/FERDY/.gemini/antigravity-ide/brain/c4eb0344-4332-4d17-a863-e218b8eb364a/test_footer_{name}.png"
        driver.save_screenshot(ss_path)
        print(f"Captured {page} footer to: {ss_path}")
finally:
    driver.quit()
