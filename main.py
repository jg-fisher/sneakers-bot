from selenium import webdriver
import time

s = SnkrsBot(url)

class SnkrsBot:

    def __init__(self, sneaker_url):
        self.sneaker_url =  sneaker_url
        self.driver = webdriver.Chrome('./chromedriver.exe')
    
    def get_price(self):
        self.driver.get(self.sneaker_url)
        price = self.driver.find_element_by_xpath('//div[@data-test="product-price"]')
        return int(price.get_attribute('innerHTML').strip('$'))

def main():
    url = 'https://www.nike.com/t/kd13-chill-basketball-shoe-kbKpNV'
    bot = SnkrsBot(url)

    last_price = None
    while 1:
        price = bot.get_price()
        if last_price:
            if price < last_price:
                print(f"Price dropped: {last_price - price}")
            elif price > last_price:
                print(f"Price rose: {price - last_price}")
            else:
                print(f"Price stayed: {price}")
        last_price = price
        time.sleep(3)

if __name__ == "__main__":
    main()