from selenium import webdriver
from time import sleep
from random import randint
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

# 1. Hvor mange brugte biler er der at vælge i mellem
# 2. Udskriv alle biler af mærket Ford
# 3. Åben de 5 dyreste biler med selenium i decending order og vis dem med et bar chart
# https://www.dba.dk/biler/biler/

class DbaCars():
    def __init__(self):
        self.driver = webdriver.Chrome('chromedriver.exe')
        self.driver.set_window_position(0, 0)
        self.driver.set_window_size(1024, 768)
        self.driver.get('https://www.dba.dk/biler/biler/')
        sleep(2)

        amountOfCars = self.driver.find_element_by_xpath(
            '//*[@id="srpNavigators"]/div[15]/div/ul/li[1]/small').text
        sleep(randint(3, 6))
        print("Antal brugte biler på DBA: "+amountOfCars)

        amountOfFord = self.driver.find_element_by_xpath(
            '//*[@id="srpNavigators"]/div[2]/div/div/ul[1]/li[4]/a/small').text
        sleep(randint(3, 6))
        print("Antal Ford biler på DBA: " + amountOfFord)

        self.driver2 = webdriver.Chrome('chromedriver.exe')
        self.driver2.set_window_position(500, 0)
        self.driver2.set_window_size(1024, 768)
        self.driver2.get('https://www.dba.dk/biler/biler/?sort=price-desc')
        sleep(2)

        car1 = self.driver2.find_element_by_xpath(
                    '//*[@id="content"]/div[1]/section/table/tbody/tr[4]/td[6]/a').text
        car1name = self.driver2.find_element_by_xpath(
                    '//*[@id="content"]/div[1]/section/table/tbody/tr[4]/td[2]/div/a[1]').text
        print("Car 1 Name " + car1name + "Price " + car1)

        car2 = self.driver2.find_element_by_xpath(
                    '//*[@id="content"]/div[1]/section/table/tbody/tr[5]/td[6]/a').text
        car2name = self.driver2.find_element_by_xpath(
                    '//*[@id="content"]/div[1]/section/table/tbody/tr[5]/td[2]/div/a[1]').text
        print("Car 2 Name " + car2name + "Price " + car2)

        car3 = self.driver2.find_element_by_xpath(
                    '//*[@id="content"]/div[1]/section/table/tbody/tr[6]/td[6]/a').text
        car3name = self.driver2.find_element_by_xpath(
                    '//*[@id="content"]/div[1]/section/table/tbody/tr[6]/td[2]/div/a[1]').text
        print("Car 3 Name " + car3name + "Price " + car3)

        car4 = self.driver2.find_element_by_xpath(
                    '//*[@id="content"]/div[1]/section/table/tbody/tr[7]/td[6]/a').text
        car4name = self.driver2.find_element_by_xpath(
                    '//*[@id="content"]/div[1]/section/table/tbody/tr[7]/td[2]/div/a[1]').text
        print("Car 4 Name " + car4name + "Price " + car4)

        car5 = self.driver2.find_element_by_xpath(
                    '//*[@id="content"]/div[1]/section/table/tbody/tr[8]/td[6]/a').text
        car5name = self.driver2.find_element_by_xpath(
                    '//*[@id="content"]/div[1]/section/table/tbody/tr[8]/td[2]/div/a[1]').text
        print("Car 5 Name " + car5name + "Price " + car5)

        cars = (car1name, car2name, car3name, car4name, car5name)
        y_pos = np.arange(len(cars))
        price = [car1,car2,car3,car4,car5]
        plt.bar(y_pos, price, align='center', alpha=0.5)
        plt.xticks(y_pos, cars)
        plt.ylabel('Price')
        plt.title('5 most expensive cars on dba')
        plt.show()

def main():
    DbaCars()

if __name__ == '__main__':
    main()
