import re
import pandas as pd
from bs4 import BeautifulSoup
import requests 
import csv
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import time
from selenium import webdriver 
   
#selecting Firefox as the browser 
#in order to select Chrome  
# webdriver.Chrome() will be used 
driver = webdriver.Chrome(executable_path = 'D:\chromedriver') 
   
#URL of the website  
url = "https://main.sci.gov.in/judgments"
   
#opening link in the browser 
driver.get(url) 
time.sleep(5)

elements = driver.find_element_by_link_text("Judgment Date").click()
time.sleep(5)


element = driver.find_element_by_id("ansCaptcha")
element.send_keys("4839")     #todo this for just key for test here make dynamic keys
time.sleep(5)


element = driver.find_element_by_id("v_getJBJ") 
element.click()


#target = driver.find_element_by_xpath('z-link]') 
#target.click()


get_ipython().magic('matplotlib inline')

page="https://main.sci.gov.in/judgments"
r = requests.get(page,verify = False)
c = r.content
#print(c)


# In[3]:

#Parse the html. This is done with BeautifulSoup.
soup = BeautifulSoup(c,"html.parser")
from html_table_parser import HTMLTableParser 
#print(soup)

for tx in soup.find_all('table'):
    pass
 #    print(tx.prettify())
     
     


#s = soup('<select class="z-link">XL</option></select>', 'html.parser')
#print(s)
#results = [str(i.text) for i in s.find_all('option')]

title=soup.title

    
td = soup.find_all("tabbed-nav") 
#print(td)   

rows = soup.find_all('tr')
#table = rows.feed(xhtml) 
#print(table)
#print(rows[:5])
str_cells = str(rows)
cleantext = BeautifulSoup(str_cells, "lxml").get_text()
#p.feed(xhtml) 
#print(cleantext)


import lxml.html

root = lxml.html.fromstring(page.content)
main_data = []
#lxml uses cssselect to get all table rows marked by tr
main_table = root.cssselect('tr')
#then iterate through that list and use cssselect to get td columns
for tr in main_table:
    tds = tr.cssselect('td')
#only append rows with 12 columns
    if len(tds) == 12:
#append a dictionary with data from columns to list
        main_data.append({'Diary Number':tds[0].text_content(), 
    'Case Number	C.A. No.':tds[1].text_content(), 
    'Petitioner Name	':tds[4].text_content(), 
'Respondent Name':tds[7].text_content(), 
'Petitioner':tds[10].text_content(),
'Respondent':tds[10].text_content()


})


print (len(main_data))
#creates csv writer object called countries.csv
writer = csv.writer(open('D:\Supermecourt.csv', 'wb'))      #todo give path here for write data
#writes the first row of the csv with the headers


writer.writerow(['Diary Number', 'Case Number	C.A. No', 'Petitioner Name', 'Respondent Name', 'Petitioner','Respondent'])
#iterates through data
for i in main_data:
#j becomes a list of all items for each dict object in the list
    j = i.items()
#csv writer writes rows based on previously created list
    writer.writerow([j[0][1].encode("utf8"), j[4][1], j[2][1], j[3][1], j[1][1]])
    







































