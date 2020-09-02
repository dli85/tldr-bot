import re
import requests
from bs4 import BeautifulSoup

articleWeb = input('What is the link of the article that you would like to crawl: ')
outputName = input('What do you want to name your text file (ends in .txt): ')
articleData = requests.get(articleWeb)
data = BeautifulSoup(articleData.text, "html.parser")

final_text = ""
for i in data.find_all('p'):
    if '.' in i.getText():
        final_text = final_text + i.getText()

final_text = re.sub('\[\d+\]', '', final_text)

for i in data.find_all('h1'):
    articleTitle = i.getText()
    break

if '.txt' in outputName:
    pass
else:
    outputName = articleTitle + '.txt'

f = open(outputName, 'w')
f.write(final_text)
