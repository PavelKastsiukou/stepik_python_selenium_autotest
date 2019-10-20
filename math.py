from selenium import webdriver
import math



link = "http://suninjuly.github.io/math.html"
browser = webdriver.Chrome()
browser.get(link)

x_element = browser.find_element_by_id("input_value")
x = 695
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
y = calc(x)
answer = browser.find_element_by_id("answer")
answer.send_keys(y)
robotCheckbox = browser.find_element_by_id("robotCheckbox")
robotCheckbox.click()
robotsRule = browser.find_element_by_id("robotsRule")
robotsRule.click()
address = browser.find_element_by_xpath("//button[@type='submit']")
address.click()




