import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
options.add_argument('--window-size=1440,1080')

driver = webdriver.Chrome(options=options)
try:
    driver.get("http://localhost:8080/index.html")
    time.sleep(1)
    driver.execute_script("document.documentElement.style.scrollBehavior = 'auto'; window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(1)
    ss_path = "C:/Users/FERDY/.gemini/antigravity-ide/brain/c4eb0344-4332-4d17-a863-e218b8eb364a/test_footer_index_actual.png"
    driver.save_screenshot(ss_path)
    print("Saved to", ss_path)
finally:
    driver.quit()
