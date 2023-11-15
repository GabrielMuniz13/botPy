from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from datetime import datetime
import requests

bot_token = '6666531730:AAEWtUViScI8FSokfMCVlrvPeXRWHr_gouo'
chat_id = '-1002009679647'
espera = 550
horaInicio = 7
horaFim = 24

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--verbose')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--no-sandbox')
# chrome_options.binary_location = "/usr/bin/google-chrome"

def bot():
    try:
        email = 'daniel.sousa@grupobrisanet.com.br'
        password = '008Force'
        placa = 'RIH5G34'
                                                         
        driver = webdriver.Chrome(options=chrome_options)
        driver.get('https://webapp.agilitymonitoramento.com.br')
        time.sleep(15)
        driver.find_element(By.XPATH, '//*[@id="txtUsername"]/div/div[1]/input').send_keys(email)
        driver.find_element(By.XPATH, '//*[@id="txtSenha"]/div/div[1]/input').send_keys(password)
        driver.find_element(By.XPATH, '//*[@id="btnSenha"]/div').click()
        driver.find_element(By.XPATH, '//*[@id="Menu_1"]').click()
        time.sleep(15)
        driver.find_element(By.XPATH, '//*[@id="GridInternaIdgridRecipienteRastreamento"]/div/div[5]/div[1]/table/tbody/tr[2]/td[5]/div/div[2]/div/div/div[1]/input').send_keys(placa)
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="GridInternaIdgridRecipienteRastreamento"]/div/div[6]/div[2]/table/tbody/tr[1]/td[5]').click()
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="UnidadeRastreada"]/a/i').click()
        time.sleep(15)
        location = driver.find_element(By.XPATH, '//*[@id="localizacao"]').text
        driver.close()
        return location
    except:
        print('error')
        return -1

def enviar_mensagem_grupo(bot_token, chat_id, mensagem):
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    params = {
        'chat_id': chat_id,
        'text': mensagem,
        'parse_mode': 'HTML'
    }

    response = requests.post(url, params=params)
    return response.json()

def active():
    hora_atual = datetime.now()
    hora = int(hora_atual.strftime("%H"))s
    print(hora)
    if(hora>=horaInicio and hora<=horaFim):
        return True
    else:
        return False
while(True):
    while(active()):
        msg = bot()
        if(msg!=-1):
            link = 'https://www.google.com/maps/search/'
            link = link+msg

            msg = f'<b>{msg}</b>'
            msg = msg.upper()
            link = f'<a href="{link}">Abrir no maps</a>'
            
            resposta1 = enviar_mensagem_grupo(bot_token, chat_id, msg)
            # resposta2 = enviar_mensagem_grupo(bot_token, chat_id, link)
            print(resposta1)
            # espera de 10 minutos
            time.sleep(espera)
        else:
            time.sleep(1)
    time.sleep(1)

