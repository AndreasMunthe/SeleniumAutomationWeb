from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

options=webdriver.ChromeOptions()
options.add_experimental_option('detach',True)
driver1=webdriver.Chrome(options=options)
driver1.get("http://www.thetestingWorld.com/testings")
