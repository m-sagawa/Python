# -*- coding: Shift-JIS -*-

from selenium import webdriver
import chromedriver_binary
import time

#�T�C�g���J��
driver = webdriver.Chrome()
driver.get("https://a-force.biz/#!")
time.sleep(3)

#�V���̗pQ&A���N���b�N
driver.find_element_by_xpath("//a[@id='bot-link']").click()
time.sleep(3)

#�t���[����؂�ւ���
driver.switch_to_frame(driver.find_element_by_tag_name("iframe"))
time.sleep(3)

#������e����͂���
driver.find_element_by_id("tweet").send_keys("�̗p�l��")
time.sleep(3)

#���M�{�^�����N���b�N
driver.find_element_by_xpath("//button[@id='send_btn']").click()
time.sleep(3)

#�Ԏ����擾�E�\��
h = driver.find_elements_by_xpath("//div[@class='alert alert-warning']")
for i in h:
	print(i.text)
	time.sleep(3)

#���̃t���[���ɖ߂�
driver.switch_to.default_content()

#�u���E�U�����
driver.close()