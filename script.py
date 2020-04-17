URL      = "https://qiita.com" # <= ここにスクレイピングしたい対象URLを書いてください
Selector = ".tr-ItemList_subLabel"  # <= ここにスクレイピングしたい対象のCSSセレクタを書いてくださ
Selector2 = ".tr-Item_title"  # <= ここにスクレイピングしたい対象のCSSセレクタを書いてくださ
path = "/Users/teshigawararyou/Downloads/chromedriver"
# 必須
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

# Selenium用オプション
op = Options()
op.add_argument("--disable-gpu");
op.add_argument("--disable-extensions");
op.add_argument("--proxy-server='direct://'");
op.add_argument("--proxy-bypass-list=*");
op.add_argument("--start-maximized");
op.add_argument("--headless");
driver = webdriver.Chrome(path,chrome_options=op)

# Seleniumでサイトアクセス
# スクレイピングしたい対象が描写されるまでWait
# time.sleep()はご法度！指定した時間待っても描写されない事はままあるので。
driver.get(URL)
WebDriverWait(driver, 30).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, Selector))
)

soup = BeautifulSoup(driver.page_source, features="html.parser")
el = soup.select(Selector)[0].string
print(el)