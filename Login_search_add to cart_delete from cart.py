from selenium import webdriver
from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
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
driver.find_element(By.XPATH, "//button[@class='button button--large button--green auth-modal__submit ng-star-inserted']").click()
sleep(3)
search = driver.find_element(By.XPATH, "//input[@class='search-form__input ng-untouched ng-pristine ng-valid']")
search.send_keys('tarmak los angeles lakers', Keys.ENTER)
sleep(3)
driver.find_element(By.XPATH, "//div[@data-goods-id='362817279']").click()
sleep(3)
driver.find_element(By.XPATH, "//a[@href='https://rozetka.com.ua/ua/362817279/p362817279/photo/']").click()
sleep(3)
driver.find_element(By.XPATH, "//button[@class='buy-button button button--with-icon button--green button--medium buy-button--tile ng-star-inserted']").click()
sleep(3)
driver.find_element(By.XPATH, "//button[@aria-controls='cartProductActions0']").click()
sleep(3)
driver.find_element(By.XPATH, "//button[@class='button button--medium button--with-icon button--link']").click()
sleep(3)

actual_text = driver.find_element(By.XPATH, "//h4[@class='cart-dummy__heading']").text
expected_text = 'Кошик порожній'
assert actual_text == expected_text