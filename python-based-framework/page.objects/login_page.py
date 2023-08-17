from selenium.webdriver.common.by import By

class LoginPage:
  def __init__(self, driver):
    self.driver = driver
    self.username_field = driver.find_element_by_id("username")
    self.password_field = driver.find_element_by_id("password")

def login(self, username, password):
  self.username_field.send_keys(username)
  self.password_field.send_keys(password)
  self.password_field.submit()
  
