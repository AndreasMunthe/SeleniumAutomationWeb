from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import os

def check_saved_photos(folder_path, file_extension=".png"):
    files = os.listdir(folder_path)
    photo_count = 0
    
    for file in files:
        if file.endswith(file_extension):
            photo_count += 1
    
    if photo_count > 0:
        print(f"{photo_count} photo(s) with the extension '{file_extension}' have been saved in the folder.")
    else:
        print(f"No photos with the extension '{file_extension}' have been saved in the folder.")

# Example usage
folder_path = "C://Users//Admin//PycharmProjects//pythonProject//SeleniumAutomationWeb//Capture//"
file_extension = ".png"


def launchBrowser():
    chrome_options=Options()
    URL="http://www.thetestingWorld.com/testings"
    service = Service('C:\\Users\\Admin\\PycharmProjects\\pythonProject\\SeleniumAutomationWeb\\chromedriver.exe')
    driver = webdriver.Chrome(service=service)
    driver.get(URL)
    driver.maximize_window()

   #TC-001
    element = driver.find_element(By.XPATH,'/html/body/div[4]/section/ul/li[1]/div/form/div/input[2]').send_keys("\n")  
    driver.save_screenshot("C://Users//Admin//PycharmProjects//pythonProject//SeleniumAutomationWeb//Capture//TC-001.png") 
    check_saved_photos(folder_path, file_extension)
    print("Capture have been saved")

    
    #TC-002
    driver.find_element(By.NAME,'fld_username').send_keys('James')
    element = driver.find_element(By.XPATH,'/html/body/div[4]/section/ul/li[1]/div/form/div/input[2]').send_keys("\n")
    driver.save_screenshot("C://Users//Admin//PycharmProjects//pythonProject//SeleniumAutomationWeb//Capture//TC-002.png")
    check_saved_photos(folder_path, file_extension)



    while(True):
       pass
launchBrowser()








"""
options=webdriver.ChromeOptions()
options.add_experimental_option('detach',True)
driver=webdriver.Chrome(options=options)
driver.get("http://www.thetestingWorld.com/testings")


#TC-001
element = driver.find_element(By.XPATH,'/html/body/div[4]/section/ul/li[1]/div/form/div/input[2]').send_keys("\n")
assert element.text == "Please fill out field"
driver.save_screenshot("Capture_TC-001.png")

time.sleep(5)
"""









