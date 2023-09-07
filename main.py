from constantes import  *
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import element_to_be_clickable
from selenium.webdriver.support.expected_conditions import presence_of_all_elements_located
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')
options.add_argument('--disable-extensions')
options.add_experimental_option('detach', True) # para que no se cierre


#  Paso uno: ejecución del controlador
chrome_driver = webdriver.Chrome(options=options)
chrome_driver.get(FAST_FINGERS)
start_wait = WebDriverWait(chrome_driver, 30)

# Paso dos: denegar el acceso a cockies
deny_button = start_wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='CybotCookiebotDialogBodyButtonDecline']")))
deny_button.click()


# Paso tres: obtener las palabras de la caja
def get_word_in_box(driver, indice: int):
    """ 
    Para obtener las palabras opté por hacerlo de a una palabra, obtener la lista
    completa no sirve ya que no se cargan completamente

    Args:
        driver: controlador
        indice: indice para el bucle for
    """
    wait = WebDriverWait(chrome_driver, 10)
    span_elements = wait.until(EC.element_to_be_clickable((By.XPATH, f"//*[@id='row1']/span[{indice}]")))
    
    # span_elements = chrome_driver.find_element(By.XPATH,f"//*[@id='row1']/span[{indice}]")
    palabra = span_elements.text
    return palabra

def send_keys(string: str, driver):
    """ 
    Envía caracter a caracter la palabra obtenida, más un espacio en blanco
    Args:
        string: palabra extraída de la caja
        driver: controlador Selenium
    """
    input_element = chrome_driver.find_element(By.XPATH, "//*[@id='inputfield']")
    
    for char in string:
        input_element.send_keys(char)
        time.sleep(1/110)
    input_element.send_keys(" ")


def run(driver):
    palabra = get_word_in_box(chrome_driver, 1)
    count = 1
    while palabra:
        send_keys(palabra, chrome_driver)
        count += 1
        palabra = get_word_in_box(chrome_driver, count)

if __name__ == '__main__':
    run(chrome_driver)
