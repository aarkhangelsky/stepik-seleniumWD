from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/explicit_wait2.html"
try:

    browser = webdriver.Chrome()
    browser.get(link)
    
    #Ждем цену
    WebDriverWait(browser, 12).until(
            EC.text_to_be_present_in_element((By.ID, "price"), "$100")
        )
    button = browser.find_element_by_xpath("//button[text()='Book']")
    button.click()
    
    #считаем ответ
    x_element =  browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)
    
    #вводим ответ
    input_value = browser.find_element_by_id("answer")
    input_value.send_keys(str(y))
    
    #нажимаем кнопку
    button = browser.find_element_by_xpath("//button[text()='Submit']")
    button.click()
    

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла