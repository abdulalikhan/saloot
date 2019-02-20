## What's Saloot?

Saloot is an A.I based personal assistant for Whatsapp. It can automatically respond to new messages from Whatsapp users and groups. It is an open source project built using Python.

### Prerequisites

In order to run Saloot, your system must have the following programs/packages installed:
1. [Selenium Web Driver](https://www.seleniumhq.org/download/)
2. [ChatterBot](https://github.com/gunthercox/ChatterBot)
3. [Google Chrome](https://www.google.com/chrome/)

### Code
Below is the code for Saloot:
```markdown
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
print("                            v1.0")
# print('Whatsapp Personal Assistant')
# print('Coded by Abdul Ali Khan')
name = "John Doe" # Put your name in quotes here

# Launch the web driver and a Chrome window
# To hide all errors from the user, set log level to 3.
chrome_options = Options()
chrome_options.add_argument("log-level=3")
driver = webdriver.Chrome(chrome_options=chrome_options)
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
                        user = driver.find_element_by_xpath('//span[@class = "{}"]//ancestor::div[4]'.format("OUeyt"))
                        user.click()
                        # Find textbox
                        msg_box = driver.find_element_by_class_name('_2S1VP')
                        for elem in driver.find_elements_by_xpath('.//span[@class = "selectable-text invisible-space copyable-text"]'):
                                receivedmsg = elem.text
                                #print(elem.text)
                        msg = str(bot.get_response(receivedmsg))
                        # Tell receiver that this message is from a bot
                        msg_box.send_keys("{0} is currently unavailable. You are currently chatting with his bot, Saloot.".format(name))
                        button = driver.find_element_by_xpath("(//div[@class='weEq5'])[2]").click()
                        try:
                                button.click()
                        except AttributeError as e:
                                print('')
                        msg_box.send_keys(msg)
                        button = driver.find_element_by_xpath("(//div[@class='weEq5'])[2]").click()
                        try:
                                button.click()
                        except AttributeError as e:
                                print('')
                        print('I just sent one reply.')
                        print('If you would like to deactivate me, press CTRL+C.')
                except NoSuchElementException as e2:
                        print('Waiting for new messages...')
                        time.sleep(2) # sleep for two seconds

```

For more details see [GitHub Flavored Markdown](https://guides.github.com/features/mastering-markdown/).

### Jekyll Themes

Your Pages site will use the layout and styles from the Jekyll theme you have selected in your [repository settings](https://github.com/abdulalikhan/saloot/settings). The name of this theme is saved in the Jekyll `_config.yml` configuration file.

### Support or Contact

Having trouble with Pages? Check out our [documentation](https://help.github.com/categories/github-pages-basics/) or [contact support](https://github.com/contact) and we’ll help you sort it out.
