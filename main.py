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
options.add_experimental_option('detach', True)
options.add_argument('--incognito')

def run():
    ##################### Part 1 #######################
    chrome_driver = webdriver.Chrome(options=options)
    chrome_driver.get(FAST_FINGERS)

    ##################### Part 2 #######################
    start_wait = WebDriverWait(chrome_driver, 30)
    #exit()









if __name__ == '__main__':
    run()
