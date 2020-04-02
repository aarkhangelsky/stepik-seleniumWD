from selenium import webdriver
import time

try: 
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    input_FN =  browser.find_element_by_css_selector(".first_block .form-group.first_class .form-control.first")
    input_FN.send_keys("Ivan")
    input_LN = browser.find_element_by_css_selector(".first_block .form-group.second_class .form-control.second")
    input_LN.send_keys("Ivanov")
    input_Email = browser.find_element_by_css_selector(".first_block .form-group.third_class .form-control.third")
    input_Email.send_keys("Ivanov@Ivan.ru")
    
    
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
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()