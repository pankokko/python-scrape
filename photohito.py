import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import MySQLdb

connection = MySQLdb.connect(
  host='localhost',
  user='root',
  passwd='',
  db='python_db')

cursor = connection.cursor()


# 仮想ブラウザ起動、URL先のサイトにアクセス
path = "/Users/teshigawararyou/Downloads/chromedriver"
URL = 'https://photohito.com/lens/brands/sony/model/e_16-55mm_f2.8_g_sel1655g/?o=recent'
link =  "body > div.wrapper.wrapper_full > article > section > div.photo_list > div > a"

op = Options()
op.add_argument("--disable-gpu");
op.add_argument("--disable-extensions");
op.add_argument("--proxy-server='direct://'");
op.add_argument("--proxy-bypass-list=*");
op.add_argument("--start-maximized");
op.add_argument("--headless");
driver = webdriver.Chrome(path,chrome_options=op)


driver.get(URL)
WebDriverWait(driver, 30).until(
  EC.presence_of_element_located((By.CSS_SELECTOR, link))
)

#各写真詳細ページのURL

from bs4 import BeautifulSoup
soup = BeautifulSoup(driver.page_source, features="html.parser")

#各詳細ページのリンクを取得
for jump in soup.select(link):
  uri = jump.get("href")
  link = "https://photohito.com" + uri

  #詳細ページ内のセレクターを取得
  selector1 = "#exif_area > table > tbody > tr:nth-child(6) > td"
  selector2 = "#exif_area > table > tbody > tr:nth-child(5) > td"

  attributes = [selector1,selector2]

  #各詳細ページにアクセスしセレクターが表示されるまで待つ
  for attribute in attributes:
    driver.get(link)
    WebDriverWait(driver, 30).until(
      EC.presence_of_element_located((By.CSS_SELECTOR, attribute))
    )


  soup = BeautifulSoup(driver.page_source, features="html.parser")
  camera_range = soup.select(selector1)[0].string
  bokah = soup.select(selector2)[0].string
  print(camera_range)
  print(bokah)

  cursor.execute("""INSERT INTO photohito (kyori, bokah)
    VALUES (camera_range, bokah)
    """)

  connection.commit()
 
# 接続を閉じる
connection.close()
