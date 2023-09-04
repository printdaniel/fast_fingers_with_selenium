import time
from constantes import  *

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import element_to_be_clickable
from selenium.webdriver.support.expected_conditions import presence_of_all_elements_located
from selenium.webdriver.support.ui import WebDriverWait


options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')
options.add_argument('--disable-extensions')
options.add_experimental_option('detach', True) # para que no se cierre
options.add_argument('--incognito') # para que muestre menos publicidad

def step1():
    ##################### Part 1 #######################
    chrome_driver = webdriver.Chrome(options=options)
    chrome_driver.get(FAST_FINGERS)

    ##################### Part 2 #######################
    start_wait = WebDriverWait(chrome_driver, 30)

    deny_button = start_wait.until(
            element_to_be_clickable(
                By.XPATH,"//*[@id='CybotCookiebotDialogBodyButtonDecline']"
                )
            ).click()



div_elements = start_wait.until(EC.element_to_be_clickable((By.XPATH, //*[@id="words"]))



if __name__ == '__main__':
    step1()
