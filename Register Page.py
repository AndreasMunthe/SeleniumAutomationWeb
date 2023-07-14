from selenium import webdriver
from selenium.webdriver import chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time
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

def Test_Case_1():
    options=webdriver.ChromeOptions()
    options.add_experimental_option("detach",True)
    driver = webdriver.Chrome(options=options)
    driver.get("http://www.thetestingWorld.com/testings")
    driver.maximize_window()

    #TC-001 
    element = driver.find_element(By.XPATH,'/html/body/div[4]/section/ul/li[1]/div/form/div/input[2]').send_keys("\n")  
    driver.save_screenshot("C://Users//Admin//PycharmProjects//pythonProject//SeleniumAutomationWeb//Capture//TC-001.png") 
    check_saved_photos(folder_path, file_extension)
    print("Capture have been saved")

def Test_Case_2():
    options=webdriver.ChromeOptions()
    options.add_experimental_option("detach",True)
    driver = webdriver.Chrome(options=options)
    driver.get("http://www.thetestingWorld.com/testings")
    driver.maximize_window()

    #TC-002
    driver.find_element(By.NAME,'fld_username').send_keys('James')
    element = driver.find_element(By.XPATH,'/html/body/div[4]/section/ul/li[1]/div/form/div/input[2]').send_keys("\n")
    driver.save_screenshot("C://Users//Admin//PycharmProjects//pythonProject//SeleniumAutomationWeb//Capture//TC-002.png")
    check_saved_photos(folder_path, file_extension)

def Test_Case_3():
    options=webdriver.ChromeOptions()
    options.add_experimental_option("detach",True)
    driver = webdriver.Chrome(options=options)
    driver.get("http://www.thetestingWorld.com/testings")
    driver.maximize_window()

    #TC-003
    driver.find_element(By.NAME,'fld_email').send_keys('example@mail.com')
    element = driver.find_element(By.XPATH,'/html/body/div[4]/section/ul/li[1]/div/form/div/input[2]').send_keys("\n")
    time.sleep(2)
    driver.save_screenshot("C://Users//Admin//PycharmProjects//pythonProject//SeleniumAutomationWeb//Capture//TC-003.png")
    check_saved_photos(folder_path, file_extension)

def Test_Case_4():
    options=webdriver.ChromeOptions()
    options.add_experimental_option("detach",True)
    driver = webdriver.Chrome(options=options)
    driver.get("http://www.thetestingWorld.com/testings")
    driver.maximize_window()

    #TC-004
    driver.find_element(By.NAME,'fld_password').send_keys('Password123')
    element = driver.find_element(By.XPATH,'/html/body/div[4]/section/ul/li[1]/div/form/div/input[2]').send_keys("\n")
    time.sleep(2)
    driver.save_screenshot("C://Users//Admin//PycharmProjects//pythonProject//SeleniumAutomationWeb//Capture//TC-004.png")
    check_saved_photos(folder_path, file_extension) 

def Test_Case_5():
    options=webdriver.ChromeOptions()
    options.add_experimental_option("detach",True)
    driver = webdriver.Chrome(options=options)
    driver.get("http://www.thetestingWorld.com/testings")
    driver.maximize_window()

    #TC-005
    driver.find_element(By.NAME,'fld_cpassword').send_keys('Password123')
    element = driver.find_element(By.XPATH,'/html/body/div[4]/section/ul/li[1]/div/form/div/input[2]').send_keys("\n")
    time.sleep(2)
    driver.save_screenshot("C://Users//Admin//PycharmProjects//pythonProject//SeleniumAutomationWeb//Capture//TC-005.png")
    check_saved_photos(folder_path, file_extension)

def Test_Case_6():
    options=webdriver.ChromeOptions()
    options.add_experimental_option("detach",True)
    driver = webdriver.Chrome(options=options)
    driver.get("http://www.thetestingWorld.com/testings")
    driver.maximize_window()

    #TC-006
    driver.find_element(By.NAME,'dob').send_keys('12/12/2012')
    Out=driver.find_element(By.ID,'datepicker')
    Out.send_keys(Keys.ESCAPE)
    element = driver.find_element(By.XPATH,'/html/body/div[4]/section/ul/li[1]/div/form/div/input[2]').send_keys("\n")
    time.sleep(2)
    driver.save_screenshot("C://Users//Admin//PycharmProjects//pythonProject//SeleniumAutomationWeb//Capture//TC-006.png")
    check_saved_photos(folder_path, file_extension)

def Test_Case_7():
    options=webdriver.ChromeOptions()
    options.add_experimental_option("detach",True)
    driver = webdriver.Chrome(options=options)
    driver.get("http://www.thetestingWorld.com/testings")
    driver.maximize_window()

    #TC-007
    driver.find_element(By.NAME,'phone').send_keys('0811124412')   
    element = driver.find_element(By.XPATH,'/html/body/div[4]/section/ul/li[1]/div/form/div/input[2]').send_keys("\n")
    time.sleep(2)
    driver.save_screenshot("C://Users//Admin//PycharmProjects//pythonProject//SeleniumAutomationWeb//Capture//TC-007.png")
    check_saved_photos(folder_path, file_extension)

def Test_Case_8():
    options=webdriver.ChromeOptions()
    options.add_experimental_option("detach",True)
    driver = webdriver.Chrome(options=options)
    driver.get("http://www.thetestingWorld.com/testings")
    driver.maximize_window()

    #TC-008
    driver.find_element(By.NAME,'address').send_keys('Jakarta')    
    element = driver.find_element(By.XPATH,'/html/body/div[4]/section/ul/li[1]/div/form/div/input[2]').send_keys("\n")
    time.sleep(2)
    driver.save_screenshot("C://Users//Admin//PycharmProjects//pythonProject//SeleniumAutomationWeb//Capture//TC-008.png")
    check_saved_photos(folder_path, file_extension)

def Test_Case_9():
    options=webdriver.ChromeOptions()
    options.add_experimental_option("detach",True)
    driver = webdriver.Chrome(options=options)
    driver.get("http://www.thetestingWorld.com/testings")
    driver.maximize_window()

    #TC-009
    RadioButton= driver.find_element(By.XPATH,'//input[@value="home"]')
    RadioButton.click()
    element = driver.find_element(By.XPATH,'/html/body/div[4]/section/ul/li[1]/div/form/div/input[2]').send_keys("\n")
    time.sleep(2)
    driver.save_screenshot("C://Users//Admin//PycharmProjects//pythonProject//SeleniumAutomationWeb//Capture//TC-009.png")
    check_saved_photos(folder_path, file_extension)

def Test_Case_10():
    options=webdriver.ChromeOptions()
    options.add_experimental_option("detach",True)
    driver = webdriver.Chrome(options=options)
    driver.get("http://www.thetestingWorld.com/testings")
    driver.maximize_window()

    #TC-010
    obj=Select(driver.find_element(By.NAME,'sex'))
    obj.select_by_index(1)
    obj.select_by_index(2)
    element = driver.find_element(By.XPATH,'/html/body/div[4]/section/ul/li[1]/div/form/div/input[2]').send_keys("\n")
    time.sleep(2)
    driver.save_screenshot("C://Users//Admin//PycharmProjects//pythonProject//SeleniumAutomationWeb//Capture//TC-010.png")
    check_saved_photos(folder_path, file_extension)

def Test_Case_11():
    options=webdriver.ChromeOptions()
    options.add_experimental_option("detach",True)
    driver = webdriver.Chrome(options=options)
    driver.get("http://www.thetestingWorld.com/testings")
    driver.maximize_window()

    #TC-011
    obj=Select(driver.find_element(By.NAME,'country'))
    obj.select_by_index(2)
    element = driver.find_element(By.XPATH,'/html/body/div[4]/section/ul/li[1]/div/form/div/input[2]').send_keys("\n")
    time.sleep(2)
    driver.save_screenshot("C://Users//Admin//PycharmProjects//pythonProject//SeleniumAutomationWeb//Capture//TC-011.png")
    check_saved_photos(folder_path, file_extension)

def Test_Case_12():
    options=webdriver.ChromeOptions()
    options.add_experimental_option("detach",True)
    driver = webdriver.Chrome(options=options)
    driver.get("http://www.thetestingWorld.com/testings")
    driver.maximize_window()

    #TC-012
    obj=Select(driver.find_element(By.NAME,'state'))
    time.sleep(4)
    obj.select_by_index(2)
    element = driver.find_element(By.XPATH,'/html/body/div[4]/section/ul/li[1]/div/form/div/input[2]').send_keys("\n")
    time.sleep(2)
    driver.save_screenshot("C://Users//Admin//PycharmProjects//pythonProject//SeleniumAutomationWeb//Capture//TC-012.png")
    check_saved_photos(folder_path, file_extension)

def Test_Case_13():
    options=webdriver.ChromeOptions()
    options.add_experimental_option("detach",True)
    driver = webdriver.Chrome(options=options)
    driver.get("http://www.thetestingWorld.com/testings")
    driver.maximize_window()

    #TC-013
    obj=Select(driver.find_element(By.NAME,'city'))
    time.sleep(4)
    obj.select_by_index(1)
    element = driver.find_element(By.XPATH,'/html/body/div[4]/section/ul/li[1]/div/form/div/input[2]').send_keys("\n")
    time.sleep(2)
    driver.save_screenshot("C://Users//Admin//PycharmProjects//pythonProject//SeleniumAutomationWeb//Capture//TC-013.png")
    check_saved_photos(folder_path, file_extension)

def Test_Case_14():
    options=webdriver.ChromeOptions()
    options.add_experimental_option("detach",True)
    driver = webdriver.Chrome(options=options)
    driver.get("http://www.thetestingWorld.com/testings")
    driver.maximize_window()

    #TC-014
    driver.find_element(By.NAME,'zip').send_keys('29121')
        
    element = driver.find_element(By.XPATH,'/html/body/div[4]/section/ul/li[1]/div/form/div/input[2]').send_keys("\n")
    time.sleep(2)
    driver.save_screenshot("C://Users//Admin//PycharmProjects//pythonProject//SeleniumAutomationWeb//Capture//TC-014.png")
    check_saved_photos(folder_path, file_extension)

def Test_Case_15():
    options=webdriver.ChromeOptions()
    options.add_experimental_option("detach",True)
    driver = webdriver.Chrome(options=options)
    driver.get("http://www.thetestingWorld.com/testings")
    driver.maximize_window()

    #TC-015
    driver.find_element(By.LINK_TEXT,"Read Detail").click()
    time.sleep(2)
    driver.find_element(By.LINK_TEXT,"X").click()
    element = driver.find_element(By.XPATH,'/html/body/div[4]/section/ul/li[1]/div/form/div/input[2]').send_keys("\n")
    time.sleep(2)
    driver.save_screenshot("C://Users//Admin//PycharmProjects//pythonProject//SeleniumAutomationWeb//Capture//TC-015.png")
    check_saved_photos(folder_path, file_extension)

    time.sleep(5)


def Test_Cases():
    options=webdriver.ChromeOptions()
    options.add_experimental_option("detach",True)
    driver = webdriver.Chrome(options=options)
    driver.get("http://www.thetestingWorld.com/testings")
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

    #TC-003
    driver.find_element(By.NAME,'fld_email').send_keys('example@mail.com')
    element = driver.find_element(By.XPATH,'/html/body/div[4]/section/ul/li[1]/div/form/div/input[2]').send_keys("\n")
    time.sleep(2)
    driver.save_screenshot("C://Users//Admin//PycharmProjects//pythonProject//SeleniumAutomationWeb//Capture//TC-003.png")
    check_saved_photos(folder_path, file_extension)

    #TC-004
    driver.find_element(By.NAME,'fld_password').send_keys('Password123')
    element = driver.find_element(By.XPATH,'/html/body/div[4]/section/ul/li[1]/div/form/div/input[2]').send_keys("\n")
    time.sleep(2)
    driver.save_screenshot("C://Users//Admin//PycharmProjects//pythonProject//SeleniumAutomationWeb//Capture//TC-004.png")
    check_saved_photos(folder_path, file_extension)

    #TC-005
    driver.find_element(By.NAME,'fld_cpassword').send_keys('Password123')
    element = driver.find_element(By.XPATH,'/html/body/div[4]/section/ul/li[1]/div/form/div/input[2]').send_keys("\n")
    time.sleep(2)
    driver.save_screenshot("C://Users//Admin//PycharmProjects//pythonProject//SeleniumAutomationWeb//Capture//TC-005.png")
    check_saved_photos(folder_path, file_extension)

    #TC-006
    driver.find_element(By.NAME,'dob').send_keys('12/12/2012')
    Out=driver.find_element(By.ID,'datepicker')
    Out.send_keys(Keys.ESCAPE)
    element = driver.find_element(By.XPATH,'/html/body/div[4]/section/ul/li[1]/div/form/div/input[2]').send_keys("\n")
    time.sleep(2)
    driver.save_screenshot("C://Users//Admin//PycharmProjects//pythonProject//SeleniumAutomationWeb//Capture//TC-006.png")
    check_saved_photos(folder_path, file_extension)

    #TC-007
    driver.find_element(By.NAME,'phone').send_keys('0811124412')   
    element = driver.find_element(By.XPATH,'/html/body/div[4]/section/ul/li[1]/div/form/div/input[2]').send_keys("\n")
    time.sleep(2)
    driver.save_screenshot("C://Users//Admin//PycharmProjects//pythonProject//SeleniumAutomationWeb//Capture//TC-007.png")
    check_saved_photos(folder_path, file_extension)

    #TC-008
    driver.find_element(By.NAME,'address').send_keys('Jakarta')    
    element = driver.find_element(By.XPATH,'/html/body/div[4]/section/ul/li[1]/div/form/div/input[2]').send_keys("\n")
    time.sleep(2)
    driver.save_screenshot("C://Users//Admin//PycharmProjects//pythonProject//SeleniumAutomationWeb//Capture//TC-008.png")
    check_saved_photos(folder_path, file_extension)

    #TC-009
    RadioButton= driver.find_element(By.XPATH,'//input[@value="home"]')
    RadioButton.click()
    element = driver.find_element(By.XPATH,'/html/body/div[4]/section/ul/li[1]/div/form/div/input[2]').send_keys("\n")
    time.sleep(2)
    driver.save_screenshot("C://Users//Admin//PycharmProjects//pythonProject//SeleniumAutomationWeb//Capture//TC-009.png")
    check_saved_photos(folder_path, file_extension)

    #TC-010
    obj=Select(driver.find_element(By.NAME,'sex'))
    obj.select_by_index(1)
    obj.select_by_index(2)
    element = driver.find_element(By.XPATH,'/html/body/div[4]/section/ul/li[1]/div/form/div/input[2]').send_keys("\n")
    time.sleep(2)
    driver.save_screenshot("C://Users//Admin//PycharmProjects//pythonProject//SeleniumAutomationWeb//Capture//TC-010.png")
    check_saved_photos(folder_path, file_extension)

    #TC-011
    obj=Select(driver.find_element(By.NAME,'country'))
    obj.select_by_index(2)
    element = driver.find_element(By.XPATH,'/html/body/div[4]/section/ul/li[1]/div/form/div/input[2]').send_keys("\n")
    time.sleep(2)
    driver.save_screenshot("C://Users//Admin//PycharmProjects//pythonProject//SeleniumAutomationWeb//Capture//TC-011.png")
    check_saved_photos(folder_path, file_extension)

    #TC-012
    obj=Select(driver.find_element(By.NAME,'state'))
    time.sleep(4)
    obj.select_by_index(2)
    element = driver.find_element(By.XPATH,'/html/body/div[4]/section/ul/li[1]/div/form/div/input[2]').send_keys("\n")
    time.sleep(2)
    driver.save_screenshot("C://Users//Admin//PycharmProjects//pythonProject//SeleniumAutomationWeb//Capture//TC-012.png")
    check_saved_photos(folder_path, file_extension)

    #TC-013
    obj=Select(driver.find_element(By.NAME,'city'))
    time.sleep(4)
    obj.select_by_index(1)
    element = driver.find_element(By.XPATH,'/html/body/div[4]/section/ul/li[1]/div/form/div/input[2]').send_keys("\n")
    time.sleep(2)
    driver.save_screenshot("C://Users//Admin//PycharmProjects//pythonProject//SeleniumAutomationWeb//Capture//TC-013.png")
    check_saved_photos(folder_path, file_extension)

    #TC-014
    driver.find_element(By.NAME,'zip').send_keys('29121')
        
    element = driver.find_element(By.XPATH,'/html/body/div[4]/section/ul/li[1]/div/form/div/input[2]').send_keys("\n")
    time.sleep(2)
    driver.save_screenshot("C://Users//Admin//PycharmProjects//pythonProject//SeleniumAutomationWeb//Capture//TC-014.png")
    check_saved_photos(folder_path, file_extension)

    #TC-015
    driver.find_element(By.LINK_TEXT,"Read Detail").click()
    time.sleep(2)
    driver.find_element(By.LINK_TEXT,"X").click()
    element = driver.find_element(By.XPATH,'/html/body/div[4]/section/ul/li[1]/div/form/div/input[2]').send_keys("\n")
    time.sleep(2)
    driver.save_screenshot("C://Users//Admin//PycharmProjects//pythonProject//SeleniumAutomationWeb//Capture//TC-015.png")
    check_saved_photos(folder_path, file_extension)

Test_Cases()

    













    





