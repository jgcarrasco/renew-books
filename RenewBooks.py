from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def renew(dni, pin):
    driver = webdriver.Chrome()
    driver.get("http://gaudi.ua.es/uhtbin/cgisirsi/x/0/x/29/124/X/3")
    elems = driver.find_elements_by_name("user_id")
    elems[2].send_keys(dni)
    elems = driver.find_elements_by_name("password")
    elems[2].send_keys(pin)
    elems[2].send_keys(Keys.RETURN)

    #Hemos logueado, renovamos los libros
    elem = driver.find_element_by_id("renew_all")
    elem.click()
    elem = driver.find_elements_by_class_name("searchbutton")
    elem[0].click()
    driver.close()
    return True
