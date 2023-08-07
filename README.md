# testing_automation_web_practice_Amazon
This repository is a practice project for web automation for Amazon website
Below are some areas of coverage
Ideally this will be developed and expanded from set up to reporting part of the framework

# Automation Testing Framework
This repository contains the Automation Testing Framework for web app automation, including both Python-based and Java-based setups.

## Python-Based Framework

### Environment Setup

Step 1: Environment Setup

1.1 Install Python (minumun verion is 3.9)</br>
    Download and install the latest Python version from the official website.
    
    https://www.python.org/downloads/
  
1.2 Install IDE
    Choose an IDE like PyCharm or Visual Studio Code.
    Py-Charm:
    
    https://www.jetbrains.com/pycharm/download/?section=mac
    
1.3 Install Selenium WebDriver
    Run the following command on terminal within the project directory:

    pip install selenium

1.4 WebDriver Setup
    Download the WebDriver for the browsers you want to test (e.g., ChromeDriver for Chrome).</br>
    <i>Following the links below for each browser of your choice</i></br>
    
  1.4.1 ChromeDriver:
    
    https://chromedriver.chromium.org/downloads
    
  1.4.2 FirefoxDriver
  
      https://github.com/mozilla/geckodriver/releases
    
  1.4.3 EdgeDriver
  
    https://learn.microsoft.com/en-us/microsoft-edge/webdriver-chromium/?tabs=c-sharp#download-microsoft-edge-webdriver

  1.4.4 InternetExplorerDriver
  
      https://www.microsoft.com/en-us/download/details.aspx?id=44069#:~:text=To%20install%20the%20IE%20WebDriver,program%20from%20its%20current%20location.
    
### Creating the Test Framework

Step 2: Creating the Test Framework

2.1 Create Base Classes
    Create a base class to handle common functionalities such as setting up WebDriver.


    class BaseClass:
        def setup_method(self):
            self.driver = webdriver.Chrome()
        def teardown_method(self):
            self.driver.quit()
            
2.2 Implement Page Object Model (POM)
    Create classes for web pages and their elements.


    class LoginPage:
        def __init__(self, driver):
            self.driver = driver
            self.username_field = driver.find_element_by_id("username")
            self.password_field = driver.find_element_by_id("password")

    def login(self, username, password):
        self.username_field.send_keys(username)
        self.password_field.send_keys(password)
        self.password_field.submit()

2.3 Write Test Cases
Write test cases using Python's unittest or pytest framework.
    
    class TestLogin:
            def setup_method(self):
                self.login_page = LoginPage(BaseClass().setup_method())

    def test_login(self):
        self.login_page.login("user", "password")
        assert "Dashboard" in self.login_page.driver.title

    def teardown_method(self):
        BaseClass().teardown_method()

### Reporting
...

### CI/CD Integration

Step 4: CI/CD Integration

4.1 Choose a CI/CD Platform
    Platforms like Jenkins or GitLab CI work well.

4.2 Create a Pipeline
    Write a script that will install dependencies, run tests, and generate reports.

4.3 Integrate with Source Control
    Connect your CI/CD platform with your version control (like Git).

## Java-Based Framework

### Environment Setup
...

### Creating the Test Framework
...

### Reporting
...

### CI/CD Integration
...
