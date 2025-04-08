import pyautogui
pyautogui.PAUSE = 0.5 #Delay para executar todos os comandos da automatização
import time

#Passo 1: entrar no sistema da empresa - https://dlp.hashtagtreinamentos.com/python/intensivao/login
#abrir o Chrome
pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.press('enter')

#digitar o site
pyautogui.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login')
pyautogui.press('enter')
time.sleep(3) #espera 3 segundos apenas nesse comando

#Passo 2: fazer login

#preencher email
time.sleep(3)
pyautogui.click(x=711, y=379)
pyautogui.write('magalredacao@gmail.com')

#preencher senha
pyautogui.press('tab')
pyautogui.write('asenhaepassword')

#apertar botão 'logar
pyautogui.press('tab')
pyautogui.press('enter')
time.sleep(3) #aqui serve para precaver caso o site demore para carregar

#Passo 3: importar a base de dados
import os
import pandas as pd

# Caminho absoluto da pasta onde está este script
caminho_base = os.path.dirname(os.path.abspath(__file__))

# Caminho completo do arquivo produtos.csv
caminho_arquivo = os.path.join(caminho_base, 'produtos.csv')

# Leitura do arquivo
tabela = pd.read_csv(caminho_arquivo)

# Exibe os dados
print(tabela.head())

#Passo 4: cadastrar um produto
for linha in tabela.index:
    pyautogui.click(x=685, y=261)

    codigo = tabela.loc[linha, 'codigo']
    pyautogui.write(codigo)

    pyautogui.press('tab')
    marca = tabela.loc[linha, 'marca']
    pyautogui.write(marca)

    pyautogui.press('tab')
    tipo = tabela.loc[linha, 'tipo']
    pyautogui.write(tipo)

    pyautogui.press('tab')
    categoria = str(tabela.loc[linha, 'categoria'])
    pyautogui.write(categoria)

    pyautogui.press('tab')
    preco_unitario = str(tabela.loc[linha, 'preco_unitario'])
    pyautogui.write(preco_unitario)

    pyautogui.press('tab')
    custo = str(tabela.loc[linha, 'custo'])
    pyautogui.write(custo)

    pyautogui.press('tab')
    obs = str(tabela.loc[linha, 'obs'])
   
    if obs != 'nan':
        pyautogui.write(obs)

    pyautogui.press('tab')
    pyautogui.press('enter')

    pyautogui.scroll(10000) #para voltar para o início da página