from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path='C:/Users/Dell/PycharmProjects/selenium/chromedriver.exe')
driver.implicitly_wait(5)

driver.get("https://rozetka.com.ua/")

search = driver.find_element(By.XPATH, "//input[@class='search-form__input ng-untouched ng-pristine ng-valid']")
search.send_keys('nba hoodie', Keys.ENTER)

expected_text = 'nba hoodie'
actual_text = driver.find_element(By.XPATH, "//h1[@class='catalog-heading ng-star-inserted']").text

assert expected_text == actual_text, f'Error, Expected text:{expected_text}, but actual_text:{actual_text}'

driver.quit()