import unittest
from selenium import webdriver
import time

class TestAbs(unittest.TestCase):
 def test_abs1(self):

  link = "http://suninjuly.github.io/registration1.html"
  browser = webdriver.Chrome()
  browser.get(link)

# Ваш код, который заполняет обязательные поля
  firstname = browser.find_element_by_xpath("//input[@class='form-control first']")
  firstname.send_keys("Вася")
  lastname = browser.find_element_by_xpath("//input[@class='form-control second']")
  lastname.send_keys("Васин")
  email = browser.find_element_by_xpath("//input[@class='form-control third']")
  email.send_keys("Vasya@tut.by")
  telephone = browser.find_element_by_xpath("//input[@placeholder='Введите телефон:']")
  telephone.send_keys("123456")
  address = browser.find_element_by_xpath("//input[@placeholder='Введите адрес:']")
  address.send_keys("123456")
 # Отправляем заполненную форму
  button = browser.find_element_by_css_selector("button.btn")
  button.click()

# Проверяем, что смогли зарегистрироваться
# ждем загрузки страницы
  time.sleep(1)

# находим элемент, содержащий текст
  welcome_text_elt = browser.find_element_by_tag_name("h1")
# записываем в переменную welcome_text текст из элемента welcome_text_elt
  welcome_text = welcome_text_elt.text

# с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
  self.assertEqual("Поздравляем! Вы успешно зарегистировались!", welcome_text)

 def test_abs2(self):
  link = "http://suninjuly.github.io/registration2.html"
  browser = webdriver.Chrome()
  browser.get(link)

# Ваш код, который заполняет обязательные поля
  firstname = browser.find_element_by_xpath("//input[@class='form-control first']")
  firstname.send_keys("Вася")
  lastname = browser.find_element_by_xpath("//input[@placeholder='Введите фамилию']")
  lastname.send_keys("Васин")
  email = browser.find_element_by_xpath("//input[@class='form-control third']")
  email.send_keys("Vasya@tut.by")
  telephone = browser.find_element_by_xpath("//input[@placeholder='Введите телефон:']")
  telephone.send_keys("123456")
  address = browser.find_element_by_xpath("//input[@placeholder='Введите адрес:']")
  address.send_keys("123456")
  # Отправляем заполненную форму
  button = browser.find_element_by_css_selector("button.btn")
  button.click()

# Проверяем, что смогли зарегистрироваться
# ждем загрузки страницы
  time.sleep(1)

# находим элемент, содержащий текст
  welcome_text_elt = browser.find_element_by_tag_name("h1")
# записываем в переменную welcome_text текст из элемента welcome_text_elt
  welcome_text = welcome_text_elt.text

# с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
  self.assertEqual("Поздравляем! Вы успешно зарегистировались!" == welcome_text)

if __name__ == "__main__":
    unittest.main()
