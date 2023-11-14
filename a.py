from selenium import webdriver
import chromedriver_autoinstaller

# Garante que o chromedriver está instalado na versão correta
chromedriver_autoinstaller.install()

# Configurar as opções do Chrome, se necessário
chrome_options = webdriver.ChromeOptions()
# Adicione opções adicionais, se necessário
chrome_options.add_argument('--headless')
chrome_options.add_argument('--verbose')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--no-sandbox')
chrome_options.binary_location = "/usr/bin/google-chrome"

# Inicializar o driver do Chrome
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.google.com")
print(driver.title)
# Agora, você pode continuar com o restante do seu código
driver.quit()