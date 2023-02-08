from selenium import webdriver
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import random
import string

usr=input('Enter Email/ Username:')
pwd=input('Enter Password:')


driver = webdriver.Chrome()
driver.get('https://todo-list-login.firebaseapp.com/')
print ("Opened webpage")
wait = WebDriverWait(driver, timeout=40)

letters = string.ascii_lowercase
item_1 = ''.join(random.choice(letters) for i in range(7))
item_2 = ''.join(random.choice(letters) for i in range(7))
item_3 = ''.join(random.choice(letters) for i in range(7))
item_4 = ''.join(random.choice(letters) for i in range(7))
item_5 = ''.join(random.choice(letters) for i in range(7))
item_6 = ''.join(random.choice(letters) for i in range(7))
item_7 = ''.join(random.choice(letters) for i in range(7))
item_8 = ''.join(random.choice(letters) for i in range(7))
item_9 = ''.join(random.choice(letters) for i in range(7))
item_10 = ''.join(random.choice(letters) for i in range(7))

def login():

    # storing the current window handle to get back to dashboard
    main_page = driver.current_window_handle


    sleep(1)

    github_button = driver.find_element(By.CLASS_NAME, 'btn-github')
    github_button.click()

    # changing the handles to access login page
    for handle in driver.window_handles:
        if handle != main_page:
            login_page = handle
            
    # change the control to signin page        
    driver.switch_to.window(login_page)

    # enter username/email
    username_box = wait.until(EC.presence_of_element_located((By.ID, "login_field")))
    username_box.send_keys(usr)
    print ("Email Id entered")

    # enter password
    password_box = wait.until(EC.presence_of_element_located((By.ID, "password")))
    password_box.send_keys(pwd)
    print ("Password entered")

    # click sign in
    login_button = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'js-sign-in-button')))
    login_button.click()

    # change control to main page
    driver.switch_to.window(main_page)  
    sleep(3)

def add_items():
    items = [item_1, item_2, item_3, item_4, item_5, item_6, item_7, item_8, item_9, item_10]
    for x in items:

        item_box = wait.until(EC.presence_of_element_located((By.XPATH, './/*[@ng-model="home.list"]')))
        item_box.send_keys(x)
        print ("entered")
        sleep(1)

        add_btn = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'task-btn')))
        add_btn.click()

def signout():
    signout_btn = driver.find_element(By.CLASS_NAME, 'btn-default')
    signout_btn.click()
    sleep (2)

def remove_items():
    remove = wait.until(EC.presence_of_all_elements_located((By.XPATH, './/*[@ng-click="home.delete($index)"]')))
    for i in range(4, 10):
        remove[i].click()
        sleep(1)

def second_login():
    github_button = driver.find_element(By.CLASS_NAME, 'btn-github')
    github_button.click()
    sleep(1)

# 1. Login using github account
login()
# 2. Create 10 todo list with random strings
add_items()
# 3. Upon completion logout
signout()
# 4. Login with same account
second_login()
# 5. Delete list from 5-10
remove_items()
# 6. Logout upon completion
signout()
