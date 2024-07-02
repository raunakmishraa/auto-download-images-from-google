from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pyautogui
user_input = input("What do you want to search?")
driver = webdriver.Chrome(r'C:\Users\DELL\chromedriver\chromedriver.exe')
driver.get('https://images.google.com/?gws_rd=ssl')
box = driver.find_element_by_xpath('//*[@id="sbtc"]/div/div[2]/input')
box.send_keys(user_input)
box.send_keys(Keys.ENTER)
last_height = driver.execute_script('return document.body.scrollHeight')
while True:
    driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
    time.sleep(2)
    new_height = driver.execute_script('return document.body.scrollHeight')
    if new_height == last_height:
        break
    last_height = new_height
for i in range(1,25):
    try:
        image = driver.find_element_by_xpath('//*[@id="islrg"]/div[1]/div[' + str(i)+ ']/a[1]/div[1]/img').screenshot(r'C:\Users\DELL\OneDrive\Desktop\PDSC Workshop\nepal' + str(i) + '.png')
    except:
        print("Sorry, An error occurred, please try again")
