import random
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
import time

email = "********@gmail.com"
password = "**********"

chrome_driver_path = "C:\Chrome Development\chromedriver.exe"

service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)

QUOTES = []


def quotes(tag):
    options = Options()
    options.add_argument('--disable-blink-features=AutomationControlled')
    scrape = []
    time.sleep(10)
    driver.get(f"https://www.whatshouldireadnext.com/quotes/tags/{tag}")
    get_quotes = True

    while get_quotes:
        global QUOTES
        quotes = driver.find_elements(By.CLASS_NAME, "quote-card__text")
        authors = driver.find_elements(By.CLASS_NAME, "quote-card__author")
        books = driver.find_elements(By.CLASS_NAME, "quote-card__book")

        for quote, author, book in zip(quotes, authors, books):
            if book.text == "":
                book_name = ""
            else:
                book_name = book.text

            scrape.append([quote.text, author.find_element(By.TAG_NAME, "a").text, book_name])

        QUOTES += scrape

        try:
            get = driver.find_element(By.CLASS_NAME, "next")
            next_button = get.find_element(By.TAG_NAME, "a")

        except NoSuchElementException:
            get_quotes = False

        else:
            next_button.click()


quotes("books")
quotes("government")
quotes("philosophy")
quotes("power")
quotes("computers")
quotes("truth")
quotes("war")
quotes("wisdom")
quotes("anxiety")
quotes("educated")
quotes("education-system")
quotes("engineering")
quotes("environment")
quotes("agriculture")
quotes("climate-change")
quotes("compassion")
quotes("consciousness")
quotes("deep-thoughts")
quotes("empathy")
quotes("global-warming")
quotes("history")
quotes("humanity")
quotes("privacy")
quotes("mathematics")
quotes("knowledge-wisdom")
    

tweet = True
while tweet:
    rand_no = random.randint(0, len(QUOTES))
    tweet_quote = QUOTES[rand_no]

    time.sleep(600)
    driver.get("https://mobile.twitter.com/?logout=1663217440715")

    driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/div[1]/div/div[3]/div[5]/a/div/span/span').click()

    type_email = driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div/main/div/div/div/div[2]/div[2]/div/div[5]/label/div/div[2]/div/input')
    type_email.send_keys(email)

    driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div/main/div/div/div/div[2]/div[2]/div/div[6]/div').click()

    type_password = driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div/main/div/div/div/div[2]/div[2]/div[1]/div/div/div/div[3]/div/label/div/div[2]/div[1]/input')
    type_password.send_keys(password)

    driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div/main/div/div/div/div[2]/div[2]/div[2]/div/div/div[1]/div/div/div/div/span/span').click()

    driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div[3]/a/div/svg').click()

    text_path = driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[3]/div/div/div[1]/div/div/div/div/div[2]/div[1]/div/div/div/div/div/div[2]/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div')
    text_path.send_keys(f"{tweet_quote[0]}\n-{tweet_quote[1]}\n({tweet_quote[2]})")

    driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/div/div/div/div/div[3]/div/div/div').click()




