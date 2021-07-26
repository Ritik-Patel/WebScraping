import requests
from bs4 import BeautifulSoup
import pandas as pd

name=[] #List to store name of the series
ratings=[]
genre=[]
year=[]

url = "https://www.imdb.com/search/title/?title_type=tv_series&num_votes=100000,"
content = requests.get(url).content

soup = BeautifulSoup(content,"html.parser")

for a in soup.findAll('div', attrs={'class':'lister-item mode-advanced'}):
    h = a.find('h3', attrs={'class':'lister-item-header'})
    a_name=h.find('a', href=True)
    a_rating=a.find('div', attrs={'class':'inline-block ratings-imdb-rating'})
    a_genre=a.find('span', attrs={'class':'genre'})
    a_year=a.find('span', attrs={'class':'lister-item-year text-muted unbold'})
    name.append(a_name.text)
    ratings.append(a_rating.text.strip("\n"))
    genre.append(a_genre.text.strip("\n"))
    year.append(a_year.text)


df=pd.DataFrame({'Series Title':name, 'Years':year, 'Rating':ratings, 'Genre':genre})
df.to_csv('DS-PR1-18IT099.csv', index=False, encoding="utf-8-sig")

df