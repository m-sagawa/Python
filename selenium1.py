# -*- coding: Shift-JIS -*-

from selenium import webdriver
import chromedriver_binary
import time

#サイトを開く
driver = webdriver.Chrome()
driver.get("https://a-force.biz/#!")
time.sleep(3)

#新卒採用Q&Aをクリック
driver.find_element_by_xpath("//a[@id='bot-link']").click()
time.sleep(3)

#フレームを切り替える
driver.switch_to_frame(driver.find_element_by_tag_name("iframe"))
time.sleep(3)

#質問内容を入力する
driver.find_element_by_id("tweet").send_keys("採用人数")
time.sleep(3)

#送信ボタンをクリック
driver.find_element_by_xpath("//button[@id='send_btn']").click()
time.sleep(3)

#返事を取得・表示
h = driver.find_elements_by_xpath("//div[@class='alert alert-warning']")
for i in h:
	print(i.text)
	time.sleep(3)

#元のフレームに戻る
driver.switch_to.default_content()

#ブラウザを閉じる
driver.close()