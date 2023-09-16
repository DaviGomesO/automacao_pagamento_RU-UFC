from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from dotenv import load_dotenv
import os
import base64

load_dotenv()
num_cartao = os.getenv('NUMERO_CARTAO')
num_matricula = os.getenv('MATRICULA')
qtd_creditos = os.getenv('QUANTIDADE_CREDITOS')

chromedriver_exe = r'chromedriver.exe'
options = Options()
options.add_argument("start-maximized")

driver = webdriver.Chrome(service=Service(chromedriver_exe), options=options)
driver.get('https://si3.ufc.br/public//jsp/restaurante_universitario/consulta_comensal_ru.jsf')

sleep(3)
input_num_cartao = driver.find_element(by=By.XPATH, value='//*[@id="form"]/table/tbody/tr[1]/td/input') 
# input_num_cartao = driver.find_element(by=By.NAME, value='form:j_id_jsp_1091681061_2')
input_num_cartao.send_keys(num_cartao)

sleep(2)
# input_num_matricula = driver.find_element(by=By.XPATH, value='//*[@id="form"]/table/tbody/tr[2]/td/input')
input_num_matricula = driver.find_element(by=By.NAME, value='form:j_id_jsp_1091681061_3')
input_num_matricula.send_keys(num_matricula)

sleep(2)
botao_consultar = driver.find_element(by=By.XPATH, value='//*[@id="form"]/table/tfoot/tr/td/input')
# botao_consultar = driver.find_element(by=By.NAME, value='form:j_id_jsp_1091681061_4')
botao_consultar.click()

sleep(3)
input_qtd_creditos = driver.find_element(by=By.ID, value='form:qtdCreditos')
# input_qtd_creditos.send_keys(qtd_creditos)
driver.execute_script(f"arguments[0].value = '{qtd_creditos}';", input_qtd_creditos)

sleep(1)
selec_pix_credito = driver.find_element(by=By.ID, value='form:j_id_jsp_540432864_5:0')
selec_pix_credito.click()

sleep(2)
botao_pagar = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.ID, "form:btPagTesouro")))
botao_pagar.click()

sleep(2)
botao_confirmar_pagamento = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.ID, "modalForm2:btConfirmarPagtesouro")))
botao_confirmar_pagamento.click()

sleep(4)
# Encontre o iframe pelo nome, índice ou elemento
iframe = driver.find_element(by=By.ID, value='iFrameResizer0')
# Alternar para o iframe
driver.switch_to.frame(iframe)

sleep(2)
selec_pix = driver.find_element(by=By.XPATH, value='/html/body/div[1]/div/div[3]/div[2]/div[1]/div[3]/div[1]')
selec_pix.click()

sleep(2)
botao_pagar = driver.find_element(by=By.ID, value='btnPgto')
botao_pagar.click()

sleep(2)
qr_code = driver.find_element(by=By.XPATH, value='//img[@class="qr-code-img"]')
src_qr_code = qr_code.get_attribute('src')
codigo_pix = driver.find_element(by=By.XPATH,value='//*[@id="app"]/div/div[5]/div[2]/div/div[2]/div/div[2]/div/div/div[2]/div/p').text

base = src_qr_code.replace("data:image/png;base64,","")

# Decodifique a string base64 para bytes
imagem_bytes = base64.b64decode(base)

# Salve os bytes da imagem em um arquivo PNG
with open("qr_code.png", "wb") as arquivo:
    arquivo.write(imagem_bytes)

print("Imagem salva com sucesso como 'qr_code.png'")

# Salva o código do pix em outro arquivo txt
with open("codigo_pix.txt","w") as arquivo:
    arquivo.write(codigo_pix)

print(f"Código do Pix salvo em 'codigo_pix.txt'")

# Para sair do iframe e voltar para o contexto padrão da página principal
driver.switch_to.default_content()
driver.quit()