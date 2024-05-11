#passo a passo do projeto ( automatizaçao de cadastro )

#instalando e importando bibliotecas
#pa a instalar : pip install pyautogui ( no terminal )
#importando pyautogui e time para o codigo
import pyautogui
import time

# colocando uma pausa a cada linha para delay
pyautogui.PAUSE = 0.5

# COMANDOS PYAUTOGUI QUE VAMOS USAR 
#pyautogui.click -> para clicar com o mouse 
#pyautogui.press -> para pressionar uma tecla 
#pyautogui.write -> para escrever um texto
#pyautogui.hotkey-> para apertar um conjunto de teclas ( crtl+t ctrl+c ctrl+v )
#pyautogui.position-> para posiçao do mouse (x y)

#let's  go

# 1. abrir o sistema da empresa
# link :( https://dlp.hashtagtreinamentos.com/python/intensivao/login )

# - abrir navegador (chrome)
pyautogui.press ("win")
pyautogui.write ("chrome")
pyautogui.press ("enter")
time.sleep(1.5)
pyautogui.click(x=664, y=418)
time.sleep(3)


# no meu caso terei que selecionar o perfil no chrome entao pedirei a posiçao atraves desse comando abaixo
# time.sleep(5)

# print(pyautogui.position())
# farei uma new file para colocar essa comando e encontrar todas as posiçoes do mouse que eu precisar 
# nao esquece de importar as bibliotecas la no auxiliar(new file) 

# - entrar no site do sistema 
pyautogui.write(" https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

# aqui pode ser que demore alguns seg para carregar o site
time.sleep(2)

# 2. fazer o login
pyautogui.click(x=549, y=369)
pyautogui.write("dayadev2024@gmail.com")



pyautogui.press("tab") # possou para o campo da senha 
pyautogui.write("dayadev2024") 


pyautogui.press("tab") # passou para o botao
pyautogui.press("enter")
time.sleep(2)

# 3. abrir/importar a baes de dados para cadastrar
#instalando e importando bibliotecas
#para instalar : pip install pandas numpy openpyxl(para obter funcionalidades adicionais)
#importando pandas para o codigo

import pandas as pd

tabela= pd.read_csv("produtos.csv")
print(tabela)

# 4. cadastrar um produto 
# str = string = texto
# for = usar a informaçao contida para nesse caso cada linha da tabela
# para cada linha da minha tabela.index(linha) quero cadastrar numa coluna

for linha in tabela.index:
    codigo=str(tabela.loc[linha,"codigo"])
    #clicar no campo do codigo
    pyautogui.click(x=543, y=255)
    #preencher o codigo
    pyautogui.write(codigo)
    #passar para o proximo campo
    pyautogui.press("tab")
    #marca
    pyautogui.write(str(tabela.loc[linha,"marca"]))
    #passar para o proximo campo
    pyautogui.press("tab")
    #tipo
    pyautogui.write(str(tabela.loc[linha,"tipo"]))
    #passar para o proximo campo
    pyautogui.press("tab")
    #categoria
    pyautogui.write(str(tabela.loc[linha,"categoria"]))
    #passar para o proximo campo
    pyautogui.press("tab")
    #preço
    pyautogui.write(str(tabela.loc[linha,"preco_unitario"]))
    #passar para o proximo campo
    pyautogui.press("tab")
    #custo
    pyautogui.write(str(tabela.loc[linha,"custo"]))
    #passar para o proximo campo
    pyautogui.press("tab")
    #obs
    obs = str(tabela.loc[linha,"obs"])
    if obs != "nan":                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                
        pyautogui.press(obs)
    #passa para o proximo campo
    pyautogui.press("tab")
    #apertar botao eviar
    pyautogui.press("enter")
    pyautogui.scroll(5000)


#nao quero que na obs apareça (naN) quando n houver resposta 
# para isso vamos tornar obs numa variavel 
# entao trataremos uma condiçao no python com if


