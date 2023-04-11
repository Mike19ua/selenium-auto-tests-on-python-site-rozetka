from selenium import webdriver
from time import sleep

from selenium.webdriver.common.by import By

username = "********@gmail.com" #Your mail
password = "********" #Your pass

url = "https://rozetka.com.ua/ua/signin/"


driver = webdriver.Chrome(executable_path='C:/Users/Dell/PycharmProjects/selenium/chromedriver.exe')
driver.implicitly_wait(5)

driver.get(url)
driver.maximize_window()
driver.find_element(By.ID, "auth_email").send_keys(username)
sleep(3)
driver.find_element(By.ID, "auth_pass").send_keys(password)
sleep(3)
driver.find_element(By.XPATH, "//button[@class='button button--large button--green auth-modal__submit ng-star-inserted']").click


print("Login is Successfully")