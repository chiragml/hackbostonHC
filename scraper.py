import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path= 'D:/1761424/Hackathons/Boston Hacks/chromedriver/chromedriver_win32/chromedriver.exe')
driver.get('https://en.wikipedia.org/wiki/Depression_(mood)')
time.sleep(10)

result= []
content = driver.page_source
soup = BeautifulSoup(content)

attributes = ['Depression', 'anxiety', 'suicide', 'ocd', 'low self esteem', 'EasyNote']

tags = []

attributes = list((map(lambda x: x.lower(), attributes)))

for str in attributes:
    a_tags = soup.find_all('a', text= lambda t: t and str in t)
    if len(a_tags) != 0:
        tags.append(a_tags)
        for text in a_tags:
            result.append(text.get_text())

    span_tags = soup.find_all('span', text= lambda t: t and str in t)
    if len(span_tags) != 0:
        tags.append(span_tags)
        for text in span_tags:
            result.append(text.get_text())

    li_tags = soup.find_all('li', text= lambda t: t and str in t)
    if len(li_tags) != 0:
        tags.append(li_tags)
        for text in li_tags:
            result.append(text.get_text())

    p_tags = soup.find_all('p', text= lambda t: t and str in t)
    if len(p_tags) != 0:
        tags.append(p_tags)
        for text in p_tags:
            result.append(text.get_text())


print(result)
