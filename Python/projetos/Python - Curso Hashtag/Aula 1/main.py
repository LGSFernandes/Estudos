# Lógica de Automação:

    # 1. Abrir o Navegador

        # 1.1 : Abrir o Windows
        # 1.2 : Digitar o nome do Navegador
        # 1.3 : Acessar o Navegador     

    # 2. Entrar no Sistema

        # 2.1 : Digitar o Link do Sistema
        # 2.2 : Pressionar Enter para acessar o Link

    # 3. Fazer Login

        # 3.1 : Clicar no campo de email
        # 3.2 : Digitar o email
        # 3.3 : Pressionar Tab para ir para o campo de senha
        # 3.4 : Digitar a senha
        # 3.5 : Pressionar Tab para ir para o botão de login
        # 3.6 : Pressionar Enter para acessar o sistema

    # 4. Abrir a Base de Dados
    # 5. Cadastrar os Produtos
    # 6. Repetir o Passo 4 até o fim

import pyautogui
import time
import pandas

# Alguns Comandos:

    # pyautogui.click -> clica
    # pyautogui.write -> escreve um texto
    # pyautogui.press -> aperta uma tecla
    # pyautogui.hotkey -> combinação de teclas (atalhos)

pyautogui.PAUSE = 1

pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.press('enter')

link = 'https://dlp.hashtagtreinamentos.com/python/intensivao/login'

pyautogui.write(link)
pyautogui.press('enter')
time.sleep(3)

pyautogui.click(x=789, y=474)
pyautogui.write('pythonimpressionador@gmail.com')
pyautogui.press('tab')
pyautogui.write('sua senha muito muito muito dificilima')
pyautogui.press('tab')
pyautogui.press('enter')
time.sleep(4)

tabela = pandas.read_csv(r'C:\Users\Cliente\Documents\Python\projetos\Python - Curso Hashtag\Aula 1\produtos.csv')

for linha in tabela.index:


    pyautogui.click(x=791, y=361)

    codigo = str(tabela.loc[linha, 'codigo'])

    pyautogui.write(codigo)
    pyautogui.press('tab')

    marca = str(tabela.loc[linha, 'marca'])

    pyautogui.write(marca)
    pyautogui.press('tab')

    tipo = str(tabela.loc[linha, 'tipo'])

    pyautogui.write(tipo)
    pyautogui.press('tab')

    categoria = str(tabela.loc[linha, 'categoria'])

    pyautogui.write(categoria)
    pyautogui.press('tab')

    preco = str(tabela.loc[linha, 'preco_unitario'])

    pyautogui.write(preco)
    pyautogui.press('tab')

    custo = str(tabela.loc[linha, 'custo'])

    pyautogui.write(custo)
    pyautogui.press('tab')

    obs = str(tabela.loc[linha, 'obs'])

    if (obs != 'nan'):
        pyautogui.write(obs)
    pyautogui.press('tab')

    pyautogui.press('tab')
    pyautogui.press('enter')
    pyautogui.scroll(5000)

