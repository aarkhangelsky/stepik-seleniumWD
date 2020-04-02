from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    x_element =  browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)
    input_value = browser.find_element_by_id("answer")
    input_value.send_keys(str(y))
    button = browser.find_element_by_tag_name("button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    robot_option1 = browser.find_element_by_id("robotCheckbox")
    robot_option1.click()
    robot_option2 = browser.find_element_by_id("robotsRule")
    robot_option2.click()
    button.click()
    #print (x,y)
   
    
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()