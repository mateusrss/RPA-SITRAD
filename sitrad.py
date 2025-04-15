import pyautogui
import time
from datetime import datetime
import os
os.chdir(r"C:\Users\Logistica1\Desktop\RPA SITRAD")


hoje = datetime.today() # pega a data de hoje
data_inicio = hoje.strftime('%d/%m/%Y') + " 00:00"
data_fim = hoje.strftime('%d/%m/%Y') + " 23:55"
data_formatada = hoje.strftime('%d-%m-%Y') # formata a data para o formato do sitrad
pyautogui.FAILSAFE = True  # Se mover o mouse pro canto superior esquerdo, o script para

# pego a posicao do mouse e imprimo na tela
def posicao_mouse():
    #print("Você tem 2 segundos para posicionar o mouse na tela.")
    time.sleep(2)
    posicao = pyautogui.position()
    print(f"A posição do mouse é: {posicao}")
    
    return pyautogui.click(posicao)


pyautogui.click(x=131, y=748) # posicao do sitrad na barra de tarefas

time.sleep(3)

pyautogui.click(x=406, y=69) # posicao da aba relatorio no sitrad

time.sleep(2)

pyautogui.click(x=283, y=390) # clico na posicao do grafico

time.sleep(2)

pyautogui.click(x=710, y=685) # clico na posicao do botao pra gerar o relatorio

time.sleep(2)

pyautogui.click(x=173, y=261)

time.sleep(1)
pyautogui.click(x=705, y=679)

time.sleep(1)

pyautogui.click(x=250, y=237)
pyautogui.write("temperatura") # escrevo o nome do relatorio

time.sleep(2)

pyautogui.doubleClick(x=504, y=398) #clico aonde escrevo a data
time.sleep(1)
pyautogui.write(data_inicio) # escrevo a data formatada
time.sleep(2)
pyautogui.press("tab")
time.sleep(2)   
pyautogui.doubleClick(x=675, y=399) # clico aonde escrevo a data final
time.sleep(2)
pyautogui.write(data_fim) # escrevo a data formatada
time.sleep(1)
pyautogui.click(x=177, y=263)
time.sleep(1)
pyautogui.click(x=702, y=672) #clico no gerar
time.sleep(14)
pyautogui.click(x=42, y=184)
time.sleep(2)
pyautogui.click(x=59, y=224)

time.sleep(3)
pyautogui.write(f"temperatura {data_formatada}") # escrevo o nome do relatorio

time.sleep(3)

# Tenta localizar a imagem na tela
localizacao = pyautogui.locateCenterOnScreen("area_trabalho.png", confidence=0.8)
localizacao_salvar = pyautogui.locateCenterOnScreen("salvar.png", confidence=0.8)
if localizacao:
    print(f"Imagem encontrada na posição: {localizacao}")
    pyautogui.click(localizacao)
    time.sleep(2)
else:
    print("Imagem não encontrada.")

if localizacao_salvar:
    print(f"Imagem encontrada na posição: {localizacao_salvar}")
    pyautogui.click(localizacao_salvar)
    time.sleep(2)  
else:
    print("⚠️ Imagem 'salvar.png' não encontrada na tela.")

pyautogui.press("enter") 
time.sleep(3)

pyautogui.hotkey("win", "d") # minimiza todas as janelas
time.sleep(2)
local_relatorio =  pyautogui.locateCenterOnScreen("image.png", confidence=0.5)

pyautogui.click(x=32, y=57) # clico no relatorio
time.sleep(2)

pyautogui.hotkey("win")
time.sleep(2)
pyautogui.write("outlook")
time.sleep(2)
pyautogui.press("enter") # clico no outlook
time.sleep(3)
novo_email = pyautogui.locateCenterOnScreen("novo_email.png", confidence=0.8) # localiza o botao novo email
pyautogui.click(novo_email) # clico no botao novo email
time.sleep(2)

email = [
    "carecamateus22@gmail.com ,",
    "tadeu@nutripar.com.br , ",
    "vendas@nutripar.com.br , ",
    "ederson@nutripar.com.br"
]
for destinatario in email:
    pyautogui.write(destinatario) # escrevo o email
    time.sleep(1)
inserir = pyautogui.locateCenterOnScreen("inserir.png", confidence=0.8) # localiza o botao inserir
time.sleep(1)
pyautogui.click(inserir) # clico no botao inserir
time.sleep(2)
anexar_arquivo = pyautogui.locateCenterOnScreen("anexar_arquivo.png", confidence=0.8) # localiza o botao anexar arquivo
pyautogui.click(anexar_arquivo) # clico no botao anexar arquivo
time.sleep(2)

area_trabalho_email = pyautogui.locateCenterOnScreen("area_trabalho.png",confidence=0.8)
pyautogui.click(area_trabalho_email) #area de trabalho do e-mail que clico pra ter certeza que esta na aba certa

nome_do_arquivo_email = pyautogui.locateCenterOnScreen("nome do arquivo.png",confidence=0.8)
pyautogui.click(nome_do_arquivo_email)
time.sleep(1)
pyautogui.write(f"temperatura {data_formatada}.png") # escrevo o nome do relatorio
time.sleep(1.3)


pyautogui.press("enter") # pressiono enter para anexar o arquivo

for _ in range(2):
    pyautogui.press("tab")
    time.sleep(0.2)
time.sleep(1)
pyautogui.write(f"Relatorio de temperatura do dia {data_formatada}") # escrevo o assunto do email
time.sleep(2)
pyautogui.press("tab") # pressiono tab para ir para o corpo do email
time.sleep(1)
pyautogui.press("tab") # pressiono tab para ir para o corpo do email
pyautogui.write(f"Boa noite, \n\nSegue o relatorio de temperatura do dia {data_formatada}. \n\nAtenciosamente, Mateus Rodrigues") # escrevo o corpo do email  
time.sleep(2)
enviar_final = pyautogui.locateCenterOnScreen("enviar_final.png", confidence=0.8) # localiza o botao enviar
pyautogui.click(enviar_final) # clico no botao enviar

time.sleep(2.3)
pyautogui.hotkey("win", "d")
time.sleep(1)

pyautogui.click(x=32, y=57)
time.sleep(0.8)
pyautogui.press("esc")
pyautogui.press("del") #depois de enviar apago o arquivo
