import time
import preReqs
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager as CM
from bs4 import BeautifulSoup


def scrape_followers(bot, username):
    bot.get(f'https://www.instagram.com/{username}/')
    time.sleep(3.5)

    users = set()

    # vendo se a conta eh privada:
    source = bot.page_source
    soup = BeautifulSoup(source, 'html.parser')
    private = soup.find_all('div', class_='_aady')
    if len(private) > 0:
        return users

    WebDriverWait(bot, TIMEOUT).until(
        EC.presence_of_element_located((By.XPATH, "//a[contains(@href, '/followers')]"))).click()
    time.sleep(2)

    print(f"Scraping followers for {username}...")

    flag = True
    count = 0

    while flag:
        prev = len(users)
        followers = bot.find_elements(By.XPATH, "//a[contains(@href, '/')]")

        for i in followers:
            if i.get_attribute('href'):
                users.add(i.get_attribute('href').split("/")[3])
                print("Total:", len(users))
            else:
                continue

        if len(users) == prev:
            count += 1

        flag = count < 6

        ActionChains(bot).send_keys(Keys.END).perform()
        time.sleep(1)

    return users


def scrape_follows(bot, username):
    bot.get(f'https://www.instagram.com/{username}/')
    time.sleep(3.5)

    users = set()

    # vendo se a conta eh privada:
    source = bot.page_source
    soup = BeautifulSoup(source, 'html.parser')
    private = soup.find_all('div', class_='_aady')
    if len(private) > 0:
        return users

    WebDriverWait(bot, TIMEOUT).until(
        EC.presence_of_element_located((By.XPATH, "//a[contains(@href, '/following')]"))).click()
    time.sleep(2)

    print(f"Scraping follows for {username}...")

    flag = True
    count = 0

    while flag:
        prev = len(users)
        followers = bot.find_elements(By.XPATH, "//a[contains(@href, '/')]")

        for i in followers:
            if i.get_attribute('href'):
                users.add(i.get_attribute('href').split("/")[3])
                print("Total:", len(users))
            else:
                continue

        if len(users) == prev:
            count += 1

        flag = count < 6

        ActionChains(bot).send_keys(Keys.END).perform()
        time.sleep(1)

    return users

def scrape():
    credentials = preReqs.load_credentials()

    if credentials is None:
        username, password = preReqs.prompt_credentials()
    else:
        username, password = credentials

    usernames = ["comppet.ufu", "bateriacomputaria", "aaacompufu"]
    options = webdriver.ChromeOptions()
    # options.add_argument("--headless")
    options.add_argument('--no-sandbox')
    options.add_argument("--log-level=3")

    mobile_emulation = {
        "userAgent": "Mozilla/5.0 (Linux; Android 4.2.1; en-us; Nexus 5 Build/JOP40D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/90.0.1025.166 Mobile Safari/535.19"}
    options.add_experimental_option("mobileEmulation", mobile_emulation)

    bot = webdriver.Chrome(executable_path=CM().install(), options=options)

    preReqs.login(bot, username, password)

    comps = set()

    for user in usernames:
        user = user.strip()
        comps.update(scrape_followers(bot, user))

    bot.quit()

    return comps


if __name__ == '__main__':
    TIMEOUT = 15
    scrape()
