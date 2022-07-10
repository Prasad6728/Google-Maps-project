
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

s = Service("D:/chromedriver_win32/chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.get("https://www.google.com/maps/@10.7828364,78.2885026,7z")


Place = driver.find_element("class name", "tactile-searchbox-input")
Place.send_keys("bangalore")
Submit = driver.find_element("id", "searchbox-searchbutton")
Submit.click()


time.sleep(4)
directions = driver.find_element("class name", "EgL07d")
directions.click()

time.sleep(2)
destination = driver.find_element("xpath", "//div[@class='sbib_b']/input")
destination.send_keys("chennai")
search = driver.find_element("xpath", "//button[@jstcache='981']")
search.click()


time.sleep(5)
Bus = driver.find_element("xpath", "//div[@jstcache='1223']/span")
print("Bus Travel:", Bus.text)
time.sleep(2)
Train = driver.find_element("css selector", "[class*='LoJzbe']")
print("Train Travel:", Train.text)








