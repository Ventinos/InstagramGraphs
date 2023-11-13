import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager as CM
from bs4 import BeautifulSoup
from src import preReqs
from src import serializer

TIMEOUT = 15
OITO_ODIADOS = {'technologies', 'explore', 'direct', 'blog', 'reels', 'legal', 'about', 'docs', 'eddjik_jr', 'Not_A_Burner01'}


def scrape_followers(bot, username, user_input):
    bot.get(f'https://www.instagram.com/{username}/')
    time.sleep(3.5)
    users = set()
    
    WebDriverWait(bot, TIMEOUT).until(EC.presence_of_element_located((By.XPATH, "//a[contains(@href, '/followers')]"))).click()
    time.sleep(2)
    print(f"[Info] - Scraping followers for {username}...")

    flag = True
    count = 0

    print(f"{len(users)}/{user_input}")
    while flag and len(users) < user_input:
        prev = len(users)
        followers = bot.find_elements(By.XPATH, "//a[contains(@href, '/')]")

        for i in followers:
            if i.get_attribute('href'):
                users.add(i.get_attribute('href').split("/")[3])
            else:
                continue

        if len(users) == prev:
            count += 1

        flag = count < 5

        ActionChains(bot).send_keys(Keys.END).perform()
        time.sleep(1)
        print(f"{len(users)}/{user_input}")
    
    users = users.difference(OITO_ODIADOS)
    users = users.difference(username)
    users = list(users)[:user_input]
    return set(users)


def initDriver():
    options = webdriver.EdgeOptions()
    #options = webdriver.ChromeOptions()
    #adicionei isso aqui pra n mostrar o processo no chrome rolando:
    #options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument("--log-level=3")
    mobile_emulation = {
        "userAgent": "Mozilla/5.0 (Linux; Android 4.2.1; en-us; Nexus 5 Build/JOP40D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/90.0.1025.166 Mobile Safari/535.19"}
    options.add_experimental_option("mobileEmulation", mobile_emulation)

    driver = webdriver.Edge(options=options)
    return driver


def scrape():
    prompt = int(input('[Required] - Select an account:\nThomas Burner[0]\nThomas Burner II[2]\n'))
    credentials = preReqs.load_credentials(prompt)
    followers = []
    
    if credentials is None:
        username, password = preReqs.prompt_credentials()
    else:
        username, password = credentials

    user_input = int(input('[Required] - How many followers do you want to scrape (100-2000 recommended): '))

    usernames = input("[Starting Points] - Enter the Instagram usernames you want to scrape (separated by commas): ").split(",")

    
    #bot = webdriver.Chrome(executable_path=CM().install(), options=options)

    bot = initDriver()
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
    usernames = list(accounts)
    usernames.sort()
    prompt = int(input('[Required]\nResume scraping[1 ]\nRestart[2]'))

    if prompt == 1:
        following = serializer.deserializeStructure2('TempFollowings')
        print(following)
        cnt = preReqs.load_current()
        print(f"[Info] - Current progression: {cnt}/{len(usernames)}")
        usernames = usernames[cnt:]
    else:
        cnt = 0
        following = []

    #adicionando listas:
    for i in range(0, len(usernames), 1):
        user = usernames[i]
        user = user.strip()
        (flag, foll) = scrape_followings(bot, user, user_input, accounts)
        if flag:
            print("[Success]")
            following.append(foll)
            if i % 5 == 0:
                print(f"[Checkpoint!] - {cnt + i + 1}/{len(usernames)}")
                serializer.serializeStructure2(following, 'TempFollowings')
                with open('CurrentFollowing.txt', 'w') as file:
                    file.write(f"{i + cnt + 1}")

        else:
            print("[Info] - Instagram is being uncooperative, saving context and aborting")
            serializer.serializeStructure2(following, 'TempFollowings')
            with open('CurrentFollowing.txt', 'w') as file:
                file.write(f"{i + cnt}")
            exit()
    
    #followers eh uma lista de listas de seguidores,
    #followers tem os seguidores do username da relacao
    #retorno de uma dupla de username e seus seguidores
    #relacao = (nome da conta, lista de seguindo)
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
        return (True, users)
    
    WebDriverWait(bot, TIMEOUT).until(EC.presence_of_element_located((By.XPATH, "//a[contains(@href, '/following')]"))).click()
    time.sleep(2)
    print(f"[Info] - Scraping following for {username}...")

    flag = True
    flagAux = False
    count = 0
    count2 = 0
    lixo = 0

    print(f"{lixo} - {len(users)} - {user_input}")

    while lixo + len(users) < user_input and flag:
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

        if lixo == prev and len(users) == prev2:
            count += 1

        if (lixo - prev) == 16:
            count2 += 1

        flagAux = count2 < 5
        flag = count < 3 and flagAux
        ActionChains(bot).send_keys(Keys.END).perform()
        time.sleep(1)

        print(f"{lixo} - {len(users)} - {user_input}")

    sucesso = len(users) != 0 or flagAux

    users = users.difference(OITO_ODIADOS)
    users = users.difference(username)

    return (sucesso, users)
