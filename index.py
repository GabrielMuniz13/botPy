from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
from datetime import datetime
import requests


def bot():
    try:
        email = 'daniel.sousa@grupobrisanet.com.br'
        password = '008Force'
        placa = 'RIH5G34'

        chrome_options = Options()
        chrome_options.add_argument("-headless")
        driver = webdriver.Chrome(options = chrome_options)
        # driver = webdriver.Chrome()
        driver.get('https://webapp.agilitymonitoramento.com.br')
        time.sleep(8)
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
        time.sleep(3)
        location = driver.find_element(By.XPATH, '//*[@id="localizacao"]').text
        driver.close()
        return location
    except:
        print('error')

bot_token = '6666531730:AAEWtUViScI8FSokfMCVlrvPeXRWHr_gouo'
chat_id = '-4050264337'

def enviar_mensagem_grupo(bot_token, chat_id, mensagem):
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    params = {
        'chat_id': chat_id,
        'text': mensagem
    }

    response = requests.post(url, params=params)
    return response.json()


esperaa = 120
espera = 1200

while(True):
    hora_atual = datetime.now()
    hora_formatada = hora_atual.strftime("%H:%M:%S")      
    local = bot()
    print(local)
    print(hora_formatada)
    mensagem = local
    resposta = enviar_mensagem_grupo(bot_token, chat_id, mensagem)
    print(resposta)
    time.sleep(60)
    


