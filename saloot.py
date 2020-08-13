from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
import time
from chatterbot import ChatBot
bot = ChatBot('saloot')
print("               __            __ ")
print("   _________ _/ /___  ____  / /_")
print("  / ___/ __ `/ / __ \/ __ \/ __/")
print(" (__  ) /_/ / / /_/ / /_/ / /_  ")
print("/____/\__,_/_/\____/\____/\__/  ")
print("                            v1.2")
print('Whatsapp Personal Assistant')
print('Coded by Abdul Ali Khan')
name = "John Doe" # Put your name in quotes here

# Launch the web driver and a Chrome window
# To hide all errors from the user, set log level to 3.
chrome_options = Options()
chrome_options.add_argument("log-level=3")
driver = webdriver.Chrome(options=chrome_options)
driver.get('https://web.whatsapp.com/')

# Main
print("Hello! My name is Saloot. I am now your Whatsapp Assistant.")
print("As your assistant, I will be responsible for responding to your messages in your absence.")
print("To activate me, type saloot. If you wish to deactivate me, type bye in this console or use CTRL+C.")
choice = ""
while ((choice != "saloot") and (choice != "bye")):
        choice = input("[#]~ ")
if choice == "bye":
        print("Goodbye")
        exit
elif choice == "saloot":
        # Scan the QR code before pressing any key.
        input('Please scan the QR code and then hit enter.')
        done = False
        while done == False:
                try:
                        # Find newest unread message
                        user = driver.find_element_by_xpath('//span[@class = "{}"]//ancestor::div[4]'.format("eJ0yJ _8Uqu5"))
                        user.click()
                        # Find textbox
                        msg_box = driver.find_element_by_class_name('_3uMse')
                        for elem in driver.find_elements_by_xpath('.//span[@class = "selectable-text invisible-space copyable-text"]'):
                                receivedmsg = elem.text
                                #print(elem.text)
                        msg = str(bot.get_response(receivedmsg))
                        # Tell receiver that this message is from a bot
                        # msg_box.send_keys("{0} is currently unavailable. You are currently chatting with his bot, Saloot.".format(name))
                        # button = driver.find_element_by_xpath("(//div[@class='_1JNuk'])[2]").click()
                        # try:
                        #        button.click()
                        # except AttributeError as e:
                        #        print('')
                        msg_box.send_keys(msg)
                        button = driver.find_element_by_xpath("(//div[@class='_1JNuk'])[2]").click()
                        try:
                                button.click()
                        except AttributeError as e:
                                print('')
                        print('I just sent one reply.')
                        print('If you would like to deactivate me, press CTRL+C.')
                except NoSuchElementException as e2:
                        print('Waiting for new messages...')
                        time.sleep(2) # sleep for two seconds
