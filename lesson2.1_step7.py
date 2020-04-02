from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    x_element =  browser.find_element_by_id("treasure")  
    x = x_element.get_attribute("valuex")
    print (x)
    y = calc(x)
    input_value = browser.find_element_by_id("answer")
    input_value.send_keys(str(y))
    robot_option1 = browser.find_element_by_id("robotCheckbox")
    robot_option1.click()
    robot_option2 = browser.find_element_by_id("robotsRule")
    robot_option2.click()
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    #print (x,y)
   
    
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()