############## Passos Manuais #############
# 1 Logar no SIGE
# 2 Clicar Projeto EAF
# 3 Clicar Estoque
# 4 Clicar Despacho
# 5 Clicar Entregar Material
# 6 Selecionar o técnico
# 7 Clicar em selecionar
# 8 Informar a quantidade de receptores
# 9 Informar o serial no arquivo Serial.txt
# 10 Rodar o código
###########################################
# 9 Atribuir valor a variável serial
# 10 Clicar em filtrar
# 11 Colar o SN
# 12 Selecionar o receptor encontrado
# 13 Clicar em filtrar
# 14 Deletar o que foi escrito
# 15 Repetir o processo até acabar o arquivo
###########################################

import time
import pyautogui

time.sleep(2) # tempo para mudar de aba
with open('Serial.txt','r') as arquivo:
    for linha in arquivo:
        serial = linha
        # clicar em filtrar
        pyautogui.click(1240, 310, duration=0.1)
        # colar o serial
        pyautogui.write(serial)
        # selecionar o receptor
        pyautogui.click(1341, 355, duration=0.1)
        # clicar em filtrar
        pyautogui.click(1240, 310, duration=0.1)
        # Deletar o que foi escrito
        pyautogui.hotkey('ctrl', 'a')
        pyautogui.press('backspace')