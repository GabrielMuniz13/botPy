from selenium import webdriver

# Especifique o caminho para o Chromedriver

# Configurar as opções do Chrome
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')  # Execute o Chrome em modo headless (sem interface gráfica)

# Iniciar o navegador Chrome
driver = webdriver.Chrome( options=chrome_options)

# Exemplo de uso: abrir o Google e imprimir o título da página
driver.get("https://www.google.com")
print(driver.title)

# Fechar o navegador
driver.quit()
