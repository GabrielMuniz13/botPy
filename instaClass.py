from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
userInsta = 'iagabriwlhj'
password = 'teste1234'

class InstaBot:
    def __init__(self, webdriver):
        self.webdriver = webdriver
        self.webdriver.get('https://instagram.com/')
        time.sleep(2)
        self.user = (By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input')
        self.password = (By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input')
        self.submit = (By.XPATH, '//*[@id="loginForm"]/div/div[3]/button')

        self.inputMsg = (By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/div/div/div/div[1]/div/div[2]/div/div/div/div/div/div[2]/div/div/div[2]/div/div/div[2]/div/div[1]/p')
        
        self.abasClose = [(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/div/div'), (By.XPATH, '/html/body/div[3]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]')]
        self.url = 'https://www.instagram.com/direct/t/6897847780268290/' 

    def login(self):
        try:
            self.webdriver.find_element(*self.user).send_keys(userInsta)
            self.webdriver.find_element(*self.password).send_keys(password)
            time.sleep(1)
            self.webdriver.find_element(*self.submit).click()
        except:
            print('deu ruim')
    def fechaAbas(self):
        try:
            time.sleep(5)
            self.webdriver.find_element(*self.abasClose[0]).click()
            time.sleep(2)
            self.webdriver.find_element(*self.abasClose[1]).click()
            time.sleep(2)
        except:
            print('deu ruim')
    def msg(self, messagem):
        try:
            self.webdriver.get(self.url)
            time.sleep(8)
            self.webdriver.find_element(*self.inputMsg).send_keys(messagem, Keys.RETURN)
        except:
            print('deu ruim')