import time
import os
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager as CM


def save_credentials(username, password):
    with open('credentials.txt', 'w') as file:
        file.write(f"{username}\n{password}")


def load_credentials():
    if not os.path.exists('credentials.txt'):
        return None

    with open('credentials.txt', 'r') as file:
        lines = file.readlines()
        if len(lines) >= 2:
            return lines[0].strip(), lines[1].strip()

    return None

def prompt_credentials():
    username = input("Enter your Instagram username: ")
    password = input("Enter your Instagram password: ")
    save_credentials(username, password)
    return username, password


def login(bot, username, password):
    bot.get('https://www.instagram.com/accounts/login/')
    time.sleep(1)

    # Check if cookies need to be accepted
    try:
        element = bot.find_element(By.XPATH, "/html/body/div[4]/div/div/div[3]/div[2]/button")
        element.click()
    except NoSuchElementException:
        print("[Info] - Instagram did not require to accept cookies this time.")

    print("[Info] - Logging in...")
    username_input = WebDriverWait(bot, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='username']")))
    password_input = WebDriverWait(bot, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='password']")))

    username_input.clear()
    username_input.send_keys(username)
    password_input.clear()
    password_input.send_keys(password)

    login_button = WebDriverWait(bot, 2).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']")))
    login_button.click()
    time.sleep(10)

def getLastCheckpoint(filename):
    # Verify if the file exists
    if os.path.isfile(filename):
        with open(filename, 'r') as file:
            # Read the file content and get the last checkpoint in it:
            content = file.read()
            if content:
                checkpoint = content.strip()
            else:
                checkpoint = None
    else:
        # If the file does not exist, returns the last checkpoint as none
        checkpoint = None
    return checkpoint

#talvez isso aqui seja util:
"""
# Abrir o arquivo em modo de escrita e anexar
with open(nome_arquivo, 'a') as arquivo:
    # Realizar outras operações antes de escrever no arquivo
    for item in lista_de_strings:
        # Se o último item for None, escrever os itens na ordem natural
        if ultimo_item is None:
            arquivo.write(item + '\n')
        # Caso contrário, escrever a partir do último item encontrado
        elif item == ultimo_item:
            ultimo_item = None  # Reiniciar para escrever na ordem natural
        # Realizar outras operações antes de escrever no arquivo
        # (coloque suas operações aqui)
"""