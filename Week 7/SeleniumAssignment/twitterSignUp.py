from selenium import webdriver
from time import sleep
#from secrets import pwSignup
from random import randint
from selenium.common.exceptions import NoSuchElementException
import re

#THIS ASSUMES THAT YOU HAVE MADE A GMAIL BEFOREHAND
#MADE BY STEINGRIMUR JONSSON

class TwitterSignUpBot():
    def __init__(self, username, email, password):
        self.driver = webdriver.Chrome('chromedriver.exe')
        self.driver.set_window_position(0, 0)
        self.driver.set_window_size(1024, 768)
        self.driver.get('https://twitter.com/i/flow/signup')
        sleep(2)

        #Inputs username
        self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[1]/div[2]/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div[2]/label/div/div[2]/div/input').send_keys(
            username)
        sleep(1)

        # Clicks on use email instead
        self.driver.find_element_by_xpath(
            "//div[@role = 'button']/span").click()
        sleep(1)

        #Inputs email
        self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[1]/div[2]/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div[3]/label/div/div[2]/div/input').send_keys(
            email)
        sleep(1)

        #Clicks next
        def clickNext():
            self.driver.find_element_by_xpath(
                '//*[@id="react-root"]/div/div/div[1]/div[2]/div/div/div/div[2]/div[2]/div/div/div[2]/div[1]/div/div/div/div[3]/div/div/span/span').click()
            sleep(randint(3, 6))

        # Clicks next
        clickNext()

        #Clicks next, skips "Want to recive emails and notifications"
        clickNext()

        #Clicks Sign up
        self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[1]/div[2]/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[4]/div/span/span').click()
        #Wait 20 sec to make sure the email it at the top (TODO maybe make a filter to look for the right email and then make an interval loop that keeps checking for the right email.)
        sleep(10)

        #Opens Gmail and finds the last email with verification code
        self.driver2 = webdriver.Chrome('chromedriver.exe')
        self.driver2.set_window_position(500, 0)
        self.driver2.set_window_size(1024, 768)
        self.driver2.get('https://accounts.google.com/signin/v2/identifier?continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&service=mail&sacu=1&rip=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin')
        sleep(2)

        # Inputs email on gmail
        self.driver2.find_element_by_xpath(
            '//*[@id="identifierId"]').send_keys(
            email)
        sleep(1)

        # Clicks next
        self.driver2.find_element_by_xpath(
            '//*[@id="identifierNext"]/span/span').click()
        sleep(randint(3, 6))

        # Inputs email password
        self.driver2.find_element_by_xpath(
            '//*[@id="password"]/div[1]/div/div[1]/input').send_keys(
            password)
        sleep(1)

        # Clicks next
        self.driver2.find_element_by_xpath(
            '//*[@id="passwordNext"]/span/span').click()
        sleep(randint(3, 6))

        # Clicks on the safety verify button
        try:
            self.driver2.find_element_by_xpath(
                '//*[@id="yDmH0d"]/c-wiz[2]/c-wiz/div/div[1]/div/div/div/div[2]/div[3]/div/div[2]/div/span/span').click()
            sleep(randint(3, 6))
        except NoSuchElementException:
            pass

        #TODO MAKE IF POP UP FOR VERIFY AND HANGOUT POPUP(NEED POP UP XPATH)

        # Clicks next
        #self.driver2.find_element_by_xpath(
         #   '//*[@id=":3"]').click()
        # sleep(randint(3, 6))

        # Gets the code string value
        preEmailCode = self.driver2.find_element_by_xpath(
            '//*[@id=":2y"]/span').text
        sleep(randint(3, 6))
        emailCode = int(re.search(r'\d+', preEmailCode).group())

        #Inputs email verification code
        self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[1]/div[2]/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[2]/label/div/div[2]/div/input').send_keys(
            str(emailCode))
        sleep(1)

        #Clicks next
        clickNext()

        # Inputs password for Twitter
        self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[1]/div[2]/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div[3]/div/label/div/div[2]/div/input').send_keys(
            password)
        sleep(1)

        # Clicks next
        #TODO CLICK NEXT SEEMS TO BE THE SAME NEXT XPATH IN MOST CASES CLEAN CODE UP IN FUTURE
        clickNext()

        # Clicks Skip for now
        # TODO ADD PROFILE PICTURE FOR COMPANY OR BRAND
        clickNext()

        # Clicks Skip for now
        # TODO ADD PROFILE DESCRIPTION FOR COMPANY OR BRAND
        clickNext()

        # Clicks Not now for adding contacts
        self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[1]/div[2]/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[1]/div[3]/div[2]/div/span/span').click()
        sleep(randint(3, 6))

        # Clicks Skip for now
        clickNext()

        # Clicks Next
        clickNext()

        # Clicks Skip for now and Dont allow notifications
        self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[1]/div[2]/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div/div[3]/div[2]/div/span/span').click()
        sleep(randint(3, 6))

        #NOW THE TWITTER ACCOUNT IS CREATED AND IS LOGGED IN.

    def tweet(self, msg):
        # click blue 'Tweet' button
        self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div/div[3]/a').click()
        sleep(randint(2, 3))
        # Enter tweet
        self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[1]/div[2]/div/div/div/div[2]/div[2]/div/div[3]/div/div/div/div[1]/div/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div/div/div/div/div/span').send_keys(
            msg)
        sleep(randint(3, 5))
        # Tweet it!
        self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[1]/div[2]/div/div/div/div[2]/div[2]/div/div[3]/div/div/div/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[4]').click()
        sleep(2)

def main():
    #TODO MAKE USERNAME, EMAIL FORM INPUT
    #INPUT GMAIL DETAILS
    username = "username"
    gmail = "email@gmail.com"
    pwSignup = "ThisPasswordWontWork"

    my_bot = TwitterSignUpBot(username, gmail, pwSignup)
    try:
        my_bot.tweet('It worked! :D')
    except:
        print('Error tweeting')

if __name__ == '__main__':
    main()
