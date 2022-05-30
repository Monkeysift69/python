from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Firefox()
browser.get('https://docs.google.com/forms/d/e/1FAIpQLSfPmK26sVd36p0bUZQpy0UNt7Z8URpSCaV1uG8ODeoGy0BcqQ/viewform?usp=sf_link')