from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

URL = 'https://translate.google.com/?sl=iw&tl=iw&text={}&op=translate'
SLEEP = 1

class API:
    def __init__(self):
        self.driver = self.start_driver()

    def start_driver():
        options = Options()
        options.add_argument('--headless')

        return webdriver.Firefox(options=options)

    def speak(self, text: str):
        self.driver.get(URL.format(text))
        sleep(SLEEP)

        sound = self.driver.find_elements_by_tag_name('button')[33]
        self.driver.execute_script('arguments[0].scrollIntoView(true);', sound)
        sound.click()
        sleep(len(text.split(' ')) / 2 + 1)

    def __del__(self):
        self.driver.quit()

