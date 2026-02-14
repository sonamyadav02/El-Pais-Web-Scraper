import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.by import By
from deep_translator import GoogleTranslator
from collections import Counter
from threading import Thread
import json

load_dotenv()

BS_USERNAME = os.getenv("BS_USERNAME")
BS_ACCESS_KEY = os.getenv("BS_ACCESS_KEY")
URL = f"https://{BS_USERNAME}:{BS_ACCESS_KEY}@hub-cloud.browserstack.com/wd/hub"

caps = [
    {"browserName": "Chrome", "os": "Windows", "os_version": "11"},
    {"browserName": "Safari", "os": "OS X", "os_version": "Ventura"},
    {"browserName": "Firefox", "os": "Windows", "os_version": "10"},
    {"browserName": "iPhone", "device": "iPhone 14 Pro", "real_mobile": "true"},
    {"browserName": "Android", "device": "Google Pixel 7", "real_mobile": "true"}
]

def run_on_cloud(capability):
    options = ChromeOptions()
    
    bstack_options = {
        "projectName": "El Pais Scraping Project",
        "buildName": "Build 1.1 - Protocol Fix",
        "sessionName": f"Test on {capability.get('browserName') or capability.get('device')}",
    }
    
    options.set_capability('bstack:options', bstack_options)
    for key, value in capability.items():
        options.set_capability(key, value)

    driver = webdriver.Remote(command_executor=URL, options=options)
    
    try:
        driver.get("https://elpais.com/opinion/")
        wait = WebDriverWait(driver, 15)
        articles = wait.until(EC.presence_of_all_elements_located((By.TAG_NAME, "article")))[:5]

        try:
            cookie_btn = wait.until(EC.element_to_be_clickable((By.ID, "didomi-notice-agree-button")))
            cookie_btn.click()
        except:
            pass

        headers_es = [art.find_element(By.TAG_NAME, "h2").text for art in articles]

        translator = GoogleTranslator(source='es', target='en')
        headers_en = [translator.translate(h) for h in headers_es]
        
        counts = Counter(" ".join(headers_en).lower().split())
        print(f"\n--- SUCCESS: {capability.get('browserName') or capability.get('device')} ---")
        print(f"Repeated Words (>2): { {w: c for w, c in counts.items() if c > 2} }")

    except Exception as e:
        print(f"Error on {capability.get('browserName') or capability.get('device')}: {e}")
    finally:
        driver.quit()

threads = []
for i in range(5):
    t = Thread(target=run_on_cloud, args=(caps[i],))
    threads.append(t)
    t.start()

for t in threads:
    t.join()