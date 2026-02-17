import os
import requests
import re
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from deep_translator import GoogleTranslator
from collections import Counter

def run_local_scraping():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    wait = WebDriverWait(driver, 10)
    
    try:
        driver.get("https://elpais.com/opinion/")

        try:
            cookie_btn = wait.until(EC.element_to_be_clickable((By.ID, "didomi-notice-agree-button")))
            cookie_btn.click()
        except:
            pass

        articles = driver.find_elements(By.TAG_NAME, "article")[:5]
        
        headers_es = []
        os.makedirs("downloaded_images", exist_ok=True)

        for i, article in enumerate(articles):
            title = article.find_element(By.TAG_NAME, "h2").text
            headers_es.append(title)
            
            content = article.find_element(By.TAG_NAME, "p").text
            print(f"\nARTICLE {i+1}\nTitle (ES): {title}\nContent: {content}")

            try:
                img_url = article.find_element(By.TAG_NAME, "img").get_attribute("src")
                img_data = requests.get(img_url).content
                with open(f"downloaded_images/img_{i+1}.jpg", 'wb') as f:
                    f.write(img_data)
            except:
                print("Image not found for this article.")

        translator = GoogleTranslator(source='es', target='en')
        headers_en = [translator.translate(h) for h in headers_es]
        
        print("\n--- TRANSLATED HEADERS ---")
        for h in headers_en: print(h)

        all_words = " ".join(headers_en).lower()
        words = re.findall(r'\b\w+\b', all_words)
        
        counts = Counter(words)
        
        print("\n--- REPEATED WORDS (>2) ---")
        for word, count in counts.items():
            if count > 2:
                print(f"'{word}': {count}")

    finally:
        driver.quit()

if __name__ == "__main__":
    run_local_scraping()
