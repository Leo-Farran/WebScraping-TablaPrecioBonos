import requests
from bs4 import BeautifulSoup
import pandas as pd


page = requests.get('http://bonos.ecobolsar.com.ar/eco/')
soup = BeautifulSoup(page.text, 'html5lib')


tag = soup.find('table' , {'class' : 'tablapanel tablapanel2 tablesorter'})

columns = [j.text for j in tag.find_all('th')]
data = []
for td in tag.find_all('tr'):
    row = [i.text for i in td.find_all('td')]
    data.append(row)
df = pd.DataFrame(data=data,columns=columns)
df = df.dropna(how='all')
print(df)