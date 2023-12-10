import time
import argparse
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import pyperclip

parser = argparse.ArgumentParser()
parser.add_argument("keyword", help = "input keyword")
args = parser.parse_args()
#keyword = "목동맛집"

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

# 불필요한 에러 메시지 없애기
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])

#driver = webdriver.Chrome(ChromeDriverManager().install())
#driver.get ("https://www.naver.com")

browser = webdriver.Chrome(options=chrome_options)
search_blog_link = f"https://search.naver.com/search.naver?where=blog&sm=tab_viw.blog&query={args.keyword}"
browser.get(search_blog_link)


first_posting = "#sp_blog_1 > div > div.detail_box > div.title_area > a"
blogger_id_list = []
WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, first_posting)))
for _ in range(3) :
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)

for idx in range (1,100) :
    blogger_selector = f"#sp_blog_{idx} > div > div.detail_box > div.title_area > a"
    blog_a_link = browser.find_element(By.CSS_SELECTOR, blogger_selector)
    blog_real_link = blog_a_link.get_attribute("href")
    blogger_id_list.append(blog_real_link.split("/")[3] + "@naver.com")
print(args.keyword, " email ", blogger_id_list)
browser.quit()

time.sleep(3)
