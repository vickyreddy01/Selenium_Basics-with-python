#Import webdriver from selenium

from selenium import webdriver

#You can use downloaded path to launch the browsers
# Create a WebDriver instance for Chrome
driver = webdriver.Chrome()


#To open or navigate to url. Use "get" method. Take https://www.google.com/ as example and run the python file

driver.get("https://www.google.com/")

driver.maximize_window()    # Helps to maximize the window.

