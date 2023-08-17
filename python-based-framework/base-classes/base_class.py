from selenium import webdriver

class BaseClass:
  def setup_method(self):
    self.driver = webdriver.Chrome()
    return self.driver

  def teardown_method(self):
    self.driver.quit()
  
