from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time


try: 
    #link = "http://suninjuly.github.io/selects2.html"
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    x =  browser.find_element_by_id("num1").text
    y =  browser.find_element_by_id("num2").text
    summ = int(x) + int(y)
    
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(str(summ)) 
    
    button = browser.find_element_by_css_selector("button")
    button.click()
     
       
    
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()