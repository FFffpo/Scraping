from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(
    executable_path="C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe")
driver.get('http://pythonscraping.com/pages/files/form.html')

firstnameField = driver.find_element_by_name('firstname')
lastnameField = driver.find_element_by_name('lastname')
submitButton = driver.find_element_by_id('submit')

# Method1
firstnameField.send_keys('Zhif')
lastnameField.send_keys('W')
submitButton.click()

# Method2
# actions=ActionChains(driver)
# actions.click(firstnameField).send_keys('Zhif').click(lastnameField).send_keys('W').send_keys(Keys.RETURN)
# 回车键
# actions.perform

print(driver.find_element_by_tag_name('body').text)

driver.close()

# myElement.click()
# myElement.click_and_hold()
# myElement.release()
# myElement.double_click()
# myElement.send_keys_to_element('content')
