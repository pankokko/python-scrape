import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from bs4 import BeautifulSoup
import pandas as pd


URL      = "https://itp.ne.jp/keyword/?areaword=&keyword=%E7%97%85%E9%99%A2%E3%83%BB%E5%8C%BB%E9%99%A2"
#詳細ページへのリンクを取得
Selector = ".m-article-card__header__title__link"
path = "/Users/teshigawararyou/Downloads/chromedriver"


op = Options()
op.add_argument("--disable-gpu");
op.add_argument("--disable-extensions");
op.add_argument("--proxy-server='direct://'");
op.add_argument("--proxy-bypass-list=*");
op.add_argument("--start-maximized");
op.add_argument("--headless");
driver = webdriver.Chrome(path,chrome_options=op)

# ページへアクセス
driver.get(URL)

WebDriverWait(driver, 30).until(
  EC.presence_of_element_located((By.CSS_SELECTOR, Selector))
)

#1あたりにつき20件のデータが取得出来ます。
MAX_DATA = 2

for i in range(MAX_DATA):

    try:
      driver.find_element_by_class_name('m-read-more').click()
      time.sleep(7)
    except NoSuchElementException:
      break

soup = BeautifulSoup(driver.page_source, features="html.parser")

for uri in soup.select(Selector):
    link =  uri.get('href')
    URL = link + "about/"
    # 詳細ページから病院情報を取得する
    Selector1 = "body > div.container > div > div > div > div.main > div > article.item.item-table > div > section.item-body.basic > dl:nth-of-type(1) > dd"
    Selector2 = "body > div.container > div > div > div > div.main > div > article.item.item-table > div > section.item-body.basic > dl:nth-of-type(5) > dd > p:nth-of-type(1)"
    Selector3 = "body > div.container > div > div > div > div.main > div > article.item.item-table > div > section.item-body.basic > dl:nth-of-type(4) > dd"
    Selector4 = "body > div.container > div > div > div > div.main > div > article.item.item-table > div > section.item-body.basic > dl:nth-of-type(10) > dd"
    Selector5 = "body > div.container > div > div > div > div.main > div > article.item.item-table > div > section.item-body.basic > dl:nth-of-type(3) > dd > p.tell"
    
    attributes = [Selector1,Selector2,Selector3,Selector4,Selector5]


    # 各病院の詳細ページにアクセス

    for attribute in attributes:
        try:
          driver.get(URL)
          WebDriverWait(driver, 30).until(
          EC.presence_of_element_located((By.CSS_SELECTOR, attribute))
          )
        except :
          driver.get(URL)
          WebDriverWait(driver, 30).until(
          EC.presence_of_element_located((By.CSS_SELECTOR, attribute))
          )
      

    soup = BeautifulSoup(driver.page_source, features="html.parser")
    hospital_name = soup.select(Selector1)[0].string
    address = soup.select(Selector2)[0].string
    fax = soup.select(Selector3)[0].string
    email = soup.select(Selector4)[0].string
    tel = soup.select(Selector5)[0].string
    print(hospital_name)
    print(address)
    print(fax)
    print(email)
    print(tel)

    dataColumns = ['病院名','住所','FAX','電話番号','Email']
    s = pd.Series([hospital_name, fax, tel, address, email])
    df = pd.DataFrame()
    df_append = df.append(s, ignore_index=True)
    df_append.to_csv("itown.csv" , mode="a", header=False, index=False)
