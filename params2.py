from selenium import webdriver
import time
import math
import pytest


@pytest.fixture(scope="function")
def driver():
    print("\nstart browser for test..")
    driver = webdriver.Chrome()
    yield driver
    print("\nquit browser..")
    driver.quit()
@pytest.mark.parametrize('number', [236895,236896,236897,236898,236899,236903,236904,236905])
class TestLogin(object):
 def test_guest_should_see_login_link(self, driver, number):
  link = "https://stepik.org/lesson/{}/step/1".format(number)
  driver = webdriver.Chrome()
  driver.get(link)
  answer = math.log(int(time.time()))
  driver.implicitly_wait(10)
  tel = driver.find_element_by_xpath("//textarea[@placeholder='Type your answer here...']")
  tel.send_keys(str(answer))
  driver.implicitly_wait(10)
  tel2 = driver.find_element_by_xpath("//button[@class='submit-submission ']").click()
  hint = driver.find_element_by_xpath("//pre[@class='smart-hints__hint']").text
  assert "Correct!" == hint