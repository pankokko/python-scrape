import time
from selenium import webdriver

# 仮想ブラウザ起動、URL先のサイトにアクセス
driver = webdriver.Chrome("/Users/teshigawararyou/Downloads/chromedriver")
driver.get('https://itp.ne.jp/keyword/?areaword=&keyword=%E7%97%85%E9%99%A2%E3%83%BB%E5%8C%BB%E9%99%A2')
time.sleep(2)


for i in range(10):
  driver.find_element_by_class_name('m-read-more').click()
  time.sleep(7)

from bs4 import BeautifulSoup
soup = BeautifulSoup(driver.page_source, features="html.parser")
# タイトルをターミナル上に表示
