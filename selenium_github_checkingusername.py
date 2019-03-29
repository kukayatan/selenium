from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.implicitly_wait(20)

driver.get("http://www.github.com")


signing_link = driver.find_element_by_link_text("Sign in")

# enter user name and password for github and the user name thad should be found on the page after sign in
var_user = "xxxxxx"
var_pass = "xxxxxx"
var_username = "xxxxx"

signing_link.click()
user = driver.find_element_by_id("login_field")
user.send_keys(var_user)
passw = driver.find_element_by_id("password")
passw.send_keys(var_pass)
passw.submit()
profile_link = driver.find_element_by_class_name("user-profile-link")
link_label = profile_link.get_attribute("innerHTML")


try:
    assert var_username in link_label
    print("The user name was found !")
except AssertionError:
    print('Houston, we have a problem. The user name was not found !')
