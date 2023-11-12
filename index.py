from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import instaClass



def bot():
    try:
        email = 'daniel.sousa@grupobrisanet.com.br'
        password = '008Force'
        placa = 'RIH5G34'

        chrome_options = Options()
        chrome_options.add_argument("-headless")
        # driver = webdriver.Chrome(options = chrome_options)
        driver = webdriver.Chrome()
        driver.get('https://webapp.agilitymonitoramento.com.br')
        time.sleep(5)
        driver.find_element(By.XPATH, '//*[@id="txtUsername"]/div/div[1]/input').send_keys(email)
        driver.find_element(By.XPATH, '//*[@id="txtSenha"]/div/div[1]/input').send_keys(password)
        driver.find_element(By.XPATH, '//*[@id="btnSenha"]/div').click()
        driver.find_element(By.XPATH, '//*[@id="Menu_1"]').click()
        time.sleep(5)
        driver.find_element(By.XPATH, '//*[@id="GridInternaIdgridRecipienteRastreamento"]/div/div[5]/div[1]/table/tbody/tr[2]/td[5]/div/div[2]/div/div/div[1]/input').send_keys(placa)
        time.sleep(2)
        driver.find_element(By.XPATH, '//*[@id="GridInternaIdgridRecipienteRastreamento"]/div/div[6]/div[2]/table/tbody/tr[1]/td[5]').click()
        time.sleep(2)
        driver.find_element(By.XPATH, '//*[@id="UnidadeRastreada"]/a/i').click()
        time.sleep(2)
        location = driver.find_element(By.XPATH, '//*[@id="localizacao"]').text
        driver.close()
        return location
    except:
        print('error')


instaBot = instaClass.InstaBot(webdriver.Chrome())
instaBot.login()
instaBot.fechaAbas()

esperaa = 120
espera = 1200

while(True):
    
    local = bot()
    print(local)
    instaBot.msg(local)
    time.sleep(20)
    


