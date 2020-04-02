from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/alert_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    #жмем кнопку
    button = browser.find_element_by_xpath("//button[text()='I want to go on a magical journey!']")
    button.click()
    
    #соглашаемся
    confirm = browser.switch_to.alert
    confirm.accept()
    
    #считаем ответ
    x_element =  browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)
    
    #вводим ответ
    input_value = browser.find_element_by_id("answer")
    input_value.send_keys(str(y))
    
    #нажимаем кнопку
    button = browser.find_element_by_tag_name("button")
    button.click()
    
    

    

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла