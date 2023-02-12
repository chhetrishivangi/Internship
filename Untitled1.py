#!/usr/bin/env python
# coding: utf-8

# # WEB SCRAPING ASSIGNMENT-1

# Write a python program to scrape mentioned details from dineout.co.in and make data frame

# In[1]:


from bs4 import BeautifulSoup
import requests


# In[2]:


page= requests.get("https://www.dineout.co.in/delhi-restaurants/buffet-special")
page


# In[3]:


soup=BeautifulSoup(page.content)
soup


# In[4]:


Restaurantname =[]


# In[5]:


for i in soup.find_all("a",class_="restnt-name ellipsis"):
    Restaurantname.append(i.text)
    
Restaurantname


# In[6]:


Cuisine=[]


# In[7]:


for i in soup.find_all("span",class_="double-line-ellipsis"):
    Cuisine.append(i.text.split('|')[1])
    
Cuisine


# In[8]:


Location=[]


# In[9]:


for i in soup.find_all("div",class_="restnt-loc ellipsis"):
    Location.append(i.text)
    
Location


# In[10]:


Ratings=[]


# In[11]:


for i in soup.find_all("div",class_="restnt-rating rating-4"):
    Ratings.append(i.text)
    
Ratings


# In[12]:


Images=[]


# In[13]:


for i in soup.find_all("img",class_="no-img"):
    Images.append(i.get("data-src"))

Images


# In[14]:


import pandas as pd
df = pd.DataFrame({'Restaurantname':Restaurantname,'Cuisine':Cuisine,'Location':Location,'Ratings':Ratings,'Images_URL':Images})


# In[15]:


df


# 
# 
# 
# Write a python program to scrape mentioned news details from https://www.cnbc.com/world/?region=world  and make data frame
# 

# In[16]:


from bs4 import BeautifulSoup
import requests


# In[17]:


page=requests.get('https://www.cnbc.com/world/?region=world')

page


# In[18]:


news=BeautifulSoup(page.content)

news


# In[19]:


Headline=[]
for i in news.find_all('a',class_='LatestNews-headline'):
   Headline.append(i.text)
Headline


# In[20]:


Time=[]


# In[21]:


for i in news.find_all("time",class_="LatestNews-timestamp"):
    Time.append(i.text)

Time


# In[22]:


url = "https://www.cnbc.com/world/?region=world"
webpage = requests.get(url) 
trav = BeautifulSoup(webpage.content, "html.parser")
for link in trav.find_all('a'):
    print(type(link), " ", link)


# In[23]:


trav.text


# In[25]:


import pandas as pd
df=pd.DataFrame({"News":Headline,"Time":Time,})
df


# 
# Write a python program to scrape the details of most downloaded articles from AI in last 90 days

# In[26]:


from bs4 import BeautifulSoup
import requests


# In[27]:


page= requests.get("https://www.journals.elsevier.com/artificial-intelligence/most-downloaded-articles")
page


# In[28]:


soup=BeautifulSoup(page.content)
soup


# In[29]:


titles=[]

for i in soup.find_all("h2",class_="sc-1qrq3sd-1 gRGSUS sc-1nmom32-0 sc-1nmom32-1 btcbYu goSKRg"):
    titles.append(i.text)

titles


# In[30]:


Author=[]

for i in soup.find_all("span",class_="sc-1w3fpd7-0 dnCnAO"):
    Author.append(i.text)

Author


# In[31]:


Date=[]

for i in soup.find_all("span",class_="sc-1thf9ly-2 dvggWt"):
    Date.append(i.text)

Date


# In[35]:


url = "https://www.journals.elsevier.com/artificial-intelligence/most-downloaded-articles"
webpage = requests.get(url) 
trav = BeautifulSoup(webpage.content, "html.parser")
for link in trav.find_all('a'):
    print(type(link), " ", link)


# In[37]:


trav.text  


# In[38]:


import pandas as pd
df=pd.DataFrame({"Title":titles,"Author":Author,"Published Date":Date,"url":"https://www.journals.elsevier.com/artificial-intelligence/most-downloaded-articles"})
df


#  Write s python program to display list of respected former presidents of India(i.e. Name , Term of office) from https://presidentofindia.nic.in/former-presidents.htm and make data frame. 

# In[39]:


from bs4 import BeautifulSoup
import requests


# In[40]:


page= requests.get("https://presidentofindia.nic.in/former-presidents.htm")
page


# In[41]:


soup=BeautifulSoup(page.content)
soup


# In[42]:


Name=[]
for i in soup.find_all('h3'):
    Name.append(i.text)

Name


# In[43]:


Term=[]
for i in soup.find_all('p'):
    Term.append(i.text)
    
Term


# In[44]:


import pandas as pd
df=pd.DataFrame({"PresidentiaL List":Name})
df


# 
# Write a python program to display IMDB’s Top rated 50 movies’ data (i.e. name, rating, year of release) and make data frame

# In[45]:


from bs4 import BeautifulSoup
import requests


# In[46]:


page= requests.get("https://www.imdb.com/search/title/?groups=top_100") 
page


# In[47]:


soup=BeautifulSoup(page.content)
soup


# In[48]:


def get_movie_titles(soup):
    
    selection_class="lister-item-header"
    movie_title_tags=soup.find_all('h3',{'class':selection_class})
    movie_titles=[]

    for tag in movie_title_tags:
        title = tag.find('a').text
        movie_titles.append(title)
        
        
    return movie_titles


# In[49]:


titles = get_movie_titles(soup)
titles


# In[50]:


Ratings=[]
def get_movie_rating(soup):
    rating_selector="inline-block ratings-imdb-rating"         
    movie_rating_tags=soup.find_all('div',{'class':rating_selector})
    movie_rating_tagss=[] 
    for tag in movie_rating_tags:
        movie_rating_tagss.append(tag.get_text().strip())
    return movie_rating_tagss


# In[51]:


Ratings = get_movie_rating(soup)
Ratings


# In[52]:


year=[]
for i in soup.find_all("span",class_="lister-item-year text-muted unbold"):
    year.append(i.text)

year


# In[53]:


import pandas as pd
df = pd.DataFrame({'Name':titles,'ratings':Ratings,'year':year})
df


# Write a python program to display IMDB’s Top rated 50 Indian movies’ data (i.e. name, rating, year of release) and make data frame.

# In[54]:


from bs4 import BeautifulSoup
import requests


# In[55]:


page= requests.get("https://www.imdb.com/list/ls079077479/") 
page


# In[56]:


soup=BeautifulSoup(page.content)
soup


# In[58]:


def get_movie_name(soup):
    
    selection_class="lister-item-header"
    movie_name_tags=soup.find_all('h3',{'class':selection_class})
    movie_name=[]

    for tag in movie_name_tags:
        title = tag.find('a').text
        movie_name.append(title)
        
        
    return movie_name


# In[59]:


name = get_movie_name(soup)
name[:50]


# In[60]:


def get_movie_rating(soup):
    rating_selector="ipl-rating-widget"            
    movie_rating_tags=soup.find_all('div',{'class':"ipl-rating-star small"})
    movie_rating_tagss=[]
    for tag in movie_rating_tags:
        movie_rating_tagss.append(tag.get_text().strip())
    return movie_rating_tagss


# In[61]:


ratings = get_movie_rating(soup)
ratings[:50]


# In[62]:


def get_movie_year(soup):
    year_selector = "lister-item-year text-muted unbold"           
    movie_year_tags=soup.find_all('span',{'class':year_selector})
    movie_year_tagss=[]
    for tag in movie_year_tags:
        movie_year_tagss.append(tag.get_text().strip()[1:5])
    return movie_year_tagss


# In[63]:


years = get_movie_year(soup)
years[:50]


# In[64]:


import pandas as pd 
df = pd.DataFrame({'Name':name,'ratings':ratings,'year':years})
df.head(50)


# Top 10 ODI teams in women’s cricket along with the records for matches, points and rating.

# In[65]:


import requests
from bs4 import BeautifulSoup


# In[66]:


page=requests.get('https://www.icc-cricket.com/rankings/womens/team-rankings/odi')
page


# In[67]:


soup=BeautifulSoup(page.content)
soup


# In[71]:


Team=[]


# In[72]:


for i in soup.find_all('span',class_='u-hide-phablet'):
    Team.append(i.text)
Team


# In[73]:


match=[]


# In[74]:


for i in soup.find_all('td',class_='table-body__cell u-center-text'):
  match.append(i.text)
match


# In[75]:


rating=[]
for i in soup.find_all('td',class_="table-body__cell u-text-right rating"):
    rating.append(i.text)
rating


# Top 10 women’s ODI Batting players along with the records of their team and rating

# In[76]:


import requests
from bs4 import BeautifulSoup


# In[77]:


page=requests.get('https://www.icc-cricket.com/rankings/womens/player-rankings/odi/batting')
page


# In[78]:


soup=BeautifulSoup(page.content)
soup


# In[80]:


player_name=[]

for i in soup.find_all('td',class_='table-body__cell rankings-table__name name'):
   player_name.append(i.text)

player_name


# In[81]:


Team=[]
for i in soup.find_all('span',class_='table-body__logo-text'):
  Team.append(i.text)
Team


# In[82]:


Rating=[]
for i in soup.find_all('td',class_='table-body__cell rating'):
  Rating.append(i.text)
Rating


# In[84]:


import pandas as pd
df=pd.DataFrame({"Player Name":player_name, "Team": Team, "Rating":Rating})
df.head(10)


# 
# Top 10 women’s ODI all-rounder along with the records of their team and rating

# In[85]:


import requests
from bs4 import BeautifulSoup


# In[86]:


page=requests.get('https://www.icc-cricket.com/rankings/womens/player-rankings/odi/all-rounder')
page


# In[87]:


soup=BeautifulSoup(page.content)
soup


# In[88]:


player_name=[]
for i in soup.find_all('td',class_='table-body__cell rankings-table__name name'):
   player_name.append(i.text)
player_name


# In[89]:


Team=[]
for i in soup.find_all('span',class_='table-body__logo-text'):
  Team.append(i.text)
Team


# In[90]:


Rating=[]
for i in soup.find_all('td',class_='table-body__cell rating'):
  Rating.append(i.text)
Rating


# In[91]:


import pandas as pd
df=pd.DataFrame({"Player Name":player_name, "Team": Team, "Rating":Rating})
df.head(10)


# 
# Top 10 ODI teams in men’s cricket along with the records for matches, points and rating

# In[93]:


import requests
from bs4 import BeautifulSoup


# In[94]:


page=requests.get('https://www.icc-cricket.com/rankings/mens/team-rankings/odi')
page


# In[95]:


page=BeautifulSoup(page.content)
page


# In[96]:


country=[]
for i in page.find_all('span',class_='u-hide-phablet'):
    country.append(i.text)

country


# In[97]:


match=[]
for i in page.find_all('td',class_='table-body__cell u-center-text'):
    match.append(i.text)
match


# In[98]:


rating=[]
for i in page.find_all('td',class_='table-body__cell u-text-right rating'):
    rating.append(i.text)
rating


# 
# Top 10 ODI Batsmen along with the records of their team and rating

# In[99]:


import requests
from bs4 import BeautifulSoup


# In[100]:


page=requests.get('https://www.icc-cricket.com/rankings/mens/player-rankings/odi/batting')
page


# In[101]:


soup=BeautifulSoup(page.content)
soup


# In[102]:


player_name=[]
for i in soup.find_all('td',class_='table-body__cell rankings-table__name name'):
   player_name.append(i.text)
player_name


# In[103]:


Team=[]
for i in soup.find_all("span",class_='table-body__logo-text'):
  Team.append(i.text)
Team


# In[104]:


Rating=[]
for i in soup.find_all('td',class_='table-body__cell rating'):
  Rating.append(i.text)
Rating


# In[105]:


import pandas as pd
df=pd.DataFrame({"Team": Team, "Rating":Rating, "player_name":player_name})
df.head(10)


# Top 10 ODI bowlers along with the records of their team and rating.

# In[106]:


import requests
from bs4 import BeautifulSoup


# In[107]:


page=requests.get('https://www.icc-cricket.com/rankings/mens/player-rankings/odi/bowling')
page


# In[108]:


soup=BeautifulSoup(page.content)
soup


# In[109]:


player_name=[]
for i in soup.find_all('td',class_='table-body__cell rankings-table__name name'):
   player_name.append(i.text)
player_name


# In[110]:


Team=[]
for i in soup.find_all('span',class_='table-body__logo-text'):
  Team.append(i.text)
Team


# In[111]:


Rating=[]
for i in soup.find_all('td',class_='table-body__cell rating'):
  Rating.append(i.text)

Rating


# In[113]:


import pandas as pd
df=pd.DataFrame({"Player Name":player_name, "Team": Team, "Rating":Rating})
df.head(10)


#  Write a python program to display all the header tags from wikipedia.org and make data frame. 

# In[116]:


from bs4 import BeautifulSoup
import requests


# In[117]:


page= requests.get("https://en.wikipedia.org/wiki/Main_Page")
page


# In[118]:


soup=BeautifulSoup(page.content)
soup


# In[119]:


titles = soup.find_all(['h1', 'h2','h3','h4','h5','h6'])


# In[120]:


titles


# In[121]:


print('List all the header tags :', *titles, sep='\n\n')


# In[122]:


import pandas as pd
df=pd.DataFrame({"List":titles})
df


# In[ ]:




