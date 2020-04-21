URL   = "https://itp.ne.jp/keyword/?areaword=&keyword=%E7%97%85%E9%99%A2%E3%83%BB%E5%8C%BB%E9%99%A2"
# ランキング内の画像がターゲット
Selector = ".m-article-card__header__title__link"
#↓↓↓↓自身の環境にあったパスに変更してください↓↓↓↓↓
path = "/Users/teshigawararyou/Downloads/chromedriver"
# 必須
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

# Selenium用オプション quiitaの記事からコピー
op = Options()
op.add_argument("--disable-gpu");
op.add_argument("--disable-extensions");
op.add_argument("--proxy-server='direct://'");
op.add_argument("--proxy-bypass-list=*");
op.add_argument("--start-maximized");
op.add_argument("--headless");
driver = webdriver.Chrome(path,chrome_options=op)

# ページアクセス
driver.get(URL)
WebDriverWait(driver, 30).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, Selector))
)

#さらに表示ボタンが表示されなくなるまで無限ループ
# while True:
#     driver.find_element_by_class_name('m-read-more').click()
#     time.sleep(8)
#     if not driver.find_element_by_class_name('m-read-more').click():
#         break
MAX_DATA = 10

for i in range(MAX_DATA):
  driver.find_element_by_class_name('m-read-more').click()
  time.sleep(7)


soup = BeautifulSoup(driver.page_source, features="html.parser")
for uri in soup.select(Selector):
    link =  uri.get('href')
    URL = link + "about/"
    # 詳細ページから病院情報を取得する
    Selector1 = "body > div.container > div > div > div > div.main > div > article.item.item-table > div > section.item-body.basic > dl:nth-child(1) > dd"
    Selector2 = "body > div.container > div > div > div > div.main > div > article.item.item-table > div > section.item-body.basic > dl:nth-child(5) > dd > p:nth-child(1)"
    Selector3 = "body > div.container > div > div > div > div.main > div > article.item.item-table > div > section.item-body.basic > dl:nth-child(4) > dd"
    Selector4 = "body > div.container > div > div > div > div.main > div > article.item.item-table > div > section.item-body.basic > dl:nth-child(10) > dd"
    Selector5 = "body > div.container > div > div > div > div.main > div > article.item.item-table > div > section.item-body.basic > dl:nth-child(3) > dd > p.tell"
    path = "/Users/teshigawararyou/Downloads/chromedriver"
    
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.common.by import By
    from selenium.webdriver.common.keys import Keys
    from bs4 import BeautifulSoup

    # Selenium用オプション quiitaの記事を参考にしてコピーしました
    op = Options()
    op.add_argument("--disable-gpu");
    op.add_argument("--disable-extensions");
    op.add_argument("--proxy-server='direct://'");
    op.add_argument("--proxy-bypass-list=*");
    op.add_argument("--start-maximized");
    op.add_argument("--headless");
    driver = webdriver.Chrome(path,chrome_options=op)

    # 各病院の詳細ページにアクセス
    driver.get(URL)
    WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, Selector1))
    )
    driver.get(URL)
    WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, Selector2))
    )
    driver.get(URL)
    WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, Selector3))
    )
    driver.get(URL)
    WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, Selector4))
    )
    
    driver.get(URL)
    WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, Selector5))
    )

    soup = BeautifulSoup(driver.page_source, features="html.parser")
    hospital_name = soup.select(Selector1)[0].string
    address = soup.select(Selector2)[0].string
    fax = soup.select(Selector3)[0].string
    email = soup.select(Selector4)[0].string
    tel = soup.select(Selector5)[0].string
    
    print(hospital_name)
    print(fax)
    print(tel)
    print(address)
    print(email)