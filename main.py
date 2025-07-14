import random
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import ChromeOptions
from dotenv import load_dotenv
from os import getenv
from time import sleep
load_dotenv("variables.env")

chrome_options = ChromeOptions()
chrome_options.binary_location = "/usr/bin/google-chrome-stable"
chrome_options.add_experimental_option("detach",True)
user = input("Enter the user name : ")
driver = Chrome(service=Service("/usr/local/bin/chromedriver"),options=chrome_options)
driver.get("https://www.instagram.com")
WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="loginForm"]/div[1]/div[1]/div/label/input'))).send_keys(getenv("p_no"))
WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="loginForm"]/div[1]/div[2]/div/label/input'))).send_keys(getenv("password"),Keys.RETURN)
sleep(8)
driver.get(f"https://www.instagram.com/{user}/")
sleep(2)
if driver.find_elements(By.LINK_TEXT, "Go back to Instagram."):
    print("No account found by this name")
else:
    driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div[2]/div/div/div[1]/div[2]/div/div[1]/section/main/div/header/section[3]/ul/li[2]/div/a/span').click()
    WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[4]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div')))
    all_account = driver.find_element(By.XPATH,'/html/body/div[4]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div')
    accounts = [account for account in all_account.find_elements(By.XPATH,"./div")]
    for account in accounts:
        sleep(random.uniform(2, 6))
        account.find_element(By.TAG_NAME,"button").click()



