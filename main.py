
import requests
from bs4 import BeautifulSoup
url =  "https://www.codewithharry.com/"


#get HTML
r = requests.get(url)
htmlContent = r.content
# print(htmlContent)

#Parse the HTML
soup = BeautifulSoup(htmlContent, 'html.parser')
# print(soup.prettify)

#html tree Traversal
title = soup.title
#Tag
# print(type(title))  

#Navigable string
# print(type(title.string ))

#Beautifulsoup
# print(type(soup))

#Comment




#Get all paragraphs
paras = soup.find_all('p')
# print(paras)

#Get all anchor tag
a = soup.find_all('a')
# print('a')

# Get First paragraph
# print(soup.find('p'))

#Get class of any element in the HTML page
# print(soup.find('p')['class'])

#Find all the elements with class lead
# print(soup.find_all("p", class_="lead"))

#Get the text from the soup
print(soup.find('p').get_text())