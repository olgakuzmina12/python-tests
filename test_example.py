from selenium import webdriver
from time import sleep

wd = webdriver.Chrome()

# Login test
wd.get("https://connect.whil.com")

username = wd.find_element_by_name("email")
username.clear()
username.send_keys("svetlannnka@gmail.com")


password = wd.find_element_by_name("password")
password.clear()
password.send_keys("Passw0rd!")
sleep(2)

wd.find_element_by_xpath("//footer[contains(@class,'footerDesktop')]//button[@type='submit']").click()
sleep(2)

welcome = wd.find_element_by_xpath("//header/span[contains(@class, 'greeting')]")
text = welcome.text
assert 'Welcome' in text, 'Error, cannot find Welcome'

wd.close()
wd.quit()