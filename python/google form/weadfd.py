from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Chrome()
browser.get('https://forms.gle/jTkoNzMGCTALaFnA7')

"""input = browser.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[3]/div[2]/span/span')
input.click()"""

time.sleep(10)

#Username
username = "kn.38614@kanlayanee.ac.th"
user = browser.find_element_by_xpath('//*[@id="identifierId"]')
user.send_keys(username)

#Click next button
UserNext = browser.find_element_by_xpath('//*[@id="identifierNext"]/div/button/span')
UserNext.click()

time.sleep(2)

#Password
password = "123456789zaza"
psw = browser.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input')
psw.send_keys(password)

#Click next button
next = browser.find_element_by_xpath('//*[@id="passwordNext"]/div/button/span')
next.click()

time.sleep(5)


