#!  /usr/bin/python3
import time
from selenium import  webdriver;    # http://selenium-python.readthedocs.io/api.html

driver = webdriver.Chrome()
driver.get('http://play.typeracer.com/')

linkToHit = driver.find_element_by_link_text('Enter a typing race')
linkToHit.click()
time.sleep(15)
# driver.set_page_load_timeout(60)  # Its asynchronous

# Get all the span tags that contain attribute unselectable
allText = driver.find_elements_by_xpath('//span[@unselectable]')

# https://www.w3schools.com/xml/xpath_syntax.asp
# http://www.xmlfiles.com/examples/

textToType = ""
for idx in range(0, len(allText)):
    if idx == len(allText) - 1 and allText[idx].text[0] != ',':
        textToType += " "
    textToType += allText[idx].text
textToType += ' '

print(textToType)

boxToType = driver.find_element_by_class_name('txtInput')
# boxToType.send_keys(textToType)
for curChar in textToType:
    boxToType.send_keys(curChar)
    time.sleep(0.06)


