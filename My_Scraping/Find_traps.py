from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement

driver = webdriver.Chrome(
    executable_path="C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe")
driver.get('http://pythonscraping.com/pages/itsatrap.html')
links = driver.find_elements_by_tag_name('a')
for link in links:
    if not link.is_displayed():
        print('The link {} is a trap'.format(link.get_attribute('href')))

fields = driver.find_elements_by_tag_name('input')
for field in fields:
    if not field.is_displayed():
        print('Do not change value of {}'.format(field.get_attribute('name')))

driver.close()
# 通过is_displayed()找到对用户隐藏的表单
