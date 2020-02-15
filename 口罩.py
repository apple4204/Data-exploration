from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
import time
import os

os.makedirs('./img/', exist_ok=True)

chrome_options = Options()
chrome_options.add_argument('headless')

path = 'C:\python\chromedriver.exe'
driver = webdriver.Chrome(path, chrome_options=chrome_options)
driver.get("https://yasco.com.tw/tw/mask.asp")
driver.find_element_by_id("city_p").click()
time.sleep(3)
Select(driver.find_element_by_id("city_p")).select_by_visible_text(u"新北市")
time.sleep(3)
driver.find_element_by_xpath("//select[@id='city_p']/option[4]").click()
time.sleep(3)
driver.find_element_by_id("area_p").click()
time.sleep(3)
Select(driver.find_element_by_id("area_p")).select_by_visible_text(u"中和區")
time.sleep(3)
driver.find_element_by_xpath("//select[@id='area_p']/option[16]").click()
time.sleep(3)
driver.find_element_by_id("search_p").click()

time.sleep(3)
html = driver.page_source


driver.get_screenshot_as_file('./img/456.jpg')


driver.close()
print(html[:200])

