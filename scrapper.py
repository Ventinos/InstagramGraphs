import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager as CM
from bs4 import BeautifulSoup
import preReqs

TIMEOUT = 15
OITO_ODIADOS = {'technologies', 'explore', 'direct', 'blog', 'reels', 'legal', 'about', 'docs'}


def scrape_followers(bot, username, user_input):
    bot.get(f'https://www.instagram.com/{username}/')
    time.sleep(3.5)
    users = set()
    
    #a gente nunca vai pegar seguidor de conta privada por acidente então tirei a verificação
    
    WebDriverWait(bot, TIMEOUT).until(EC.presence_of_element_located((By.XPATH, "//a[contains(@href, '/followers')]"))).click()
    time.sleep(2)
    print(f"[Info] - Scraping followers for {username}...")

    flag = True
    count = 0

    while flag and len(users) < user_input:
        print(f"{len(users)}/{user_input}")
        prev = len(users)
        followers = bot.find_elements(By.XPATH, "//a[contains(@href, '/')]")

        for i in followers:
            if i.get_attribute('href'):
                users.add(i.get_attribute('href').split("/")[3])
            else:
                continue

        if len(users) == prev:
            count += 1

        flag = count < 3

        users = users.difference(OITO_ODIADOS)
        users = users.difference(preReqs.load_credentials()[0])

        ActionChains(bot).send_keys(Keys.END).perform()
        time.sleep(1)

    return set(users)


def scrape():
    credentials = preReqs.load_credentials()
    followers = []
    
    if credentials is None:
        username, password = preReqs.prompt_credentials()
    else:
        username, password = credentials

    user_input = int(input('[Required] - How many followers do you want to scrape (100-2000 recommended): '))

    usernames = input("[Starting Points] - Enter the Instagram usernames you want to scrape (separated by commas): ").split(",")

    options = webdriver.EdgeOptions()
    #options = webdriver.ChromeOptions()
    #adicionei isso aqui pra n mostrar o processo no chrome rolando:
    #options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument("--log-level=3")
    mobile_emulation = {
        "userAgent": "Mozilla/5.0 (Linux; Android 4.2.1; en-us; Nexus 5 Build/JOP40D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/90.0.1025.166 Mobile Safari/535.19"}
    options.add_experimental_option("mobileEmulation", mobile_emulation)

    bot = webdriver.Edge(options=options)
    #bot = webdriver.Chrome(executable_path=CM().install(), options=options)

    preReqs.login(bot, username, password)

    #adicionando listas:
    for user in usernames:
        user = user.strip()
        followers.append(scrape_followers(bot, user, user_input))
    
    #followers eh uma lista de listas de seguidores,
    #followers tem os seguidores do username da relacao
    #retorno de uma dupla de username e seus seguidores
    #relacao = (nome da conta, lista de seguidores) 
    relacao = []
    for i in range(len(usernames)):
        relacao.append((usernames[i], followers[i]))
    return relacao, bot


def scrapeFollowing(bot, accounts, user_input):
    following = []
    usernames = accounts

    #adicionando listas:
    for user in usernames:
        user = user.strip()
        following.append(scrape_followings(bot, user, user_input, accounts))
    
    #followers eh uma lista de listas de seguidores,
    #followers tem os seguidores do username da relacao
    #retorno de uma dupla de username e seus seguidores
    #relacao = (nome da conta, lista de seguidores) 
    relacao = []
    for i in range(len(usernames)):
        relacao.append((usernames[i], following[i]))
    return relacao


def testPopUp(bot):
    try:
        bot.find_element(By.XPATH, '//button[@class="_a9-- _a9_1"]').click()
    except:
        print('No popups this time!')


def scrape_followings(bot, username, user_input, accounts):
    bot.get(f'https://www.instagram.com/{username}/')
    time.sleep(3.5)
    testPopUp(bot)
    users = set()
    
    # vendo se a conta eh privada:
    source = bot.page_source
    soup = BeautifulSoup(source, 'html.parser')
    private = soup.find_all('div', class_='_aady')
    if len(private) > 0:
        print(f"[Info] - {username} is a private account.")
        return users
    
    WebDriverWait(bot, TIMEOUT).until(EC.presence_of_element_located((By.XPATH, "//a[contains(@href, '/following')]"))).click()
    time.sleep(2)
    print(f"[Info] - Scraping following for {username}...")

    flag = True
    count = 0
    lixo = 0

    while len(users) < user_input and flag:
        print(f"{len(users)}/{user_input}")
        following = bot.find_elements(By.XPATH, "//a[contains(@href, '/')]")

        prev = lixo
        prev2 = len(users)

        for i in following:
            if i.get_attribute('href'):
                accName = i.get_attribute('href').split("/")[3]
                if accName in accounts:
                    users.add(accName)
                else:
                    lixo += 1
            else:
                continue

        if lixo == prev and len(users) == prev2 and (prev + prev2) < 1999:
            count += 1

        users = users.difference(OITO_ODIADOS)
        users = users.difference(preReqs.load_credentials()[0])
        flag = count < 3

        ActionChains(bot).send_keys(Keys.END).perform()
        time.sleep(1)

    return set(users)
