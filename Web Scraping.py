


import requests 
   
r = requests.get('https://cognifyz.com/') 
print(r)  
print(r.content)




import requests 
r = requests.get('https://cognifyz.com/') 
print(r.url) 
print(r.status_code)




import requests 
from bs4 import BeautifulSoup 
r = requests.get('https://cognifyz.com/') 
print(r) 
soup = BeautifulSoup(r.content, 'html.parser') 
print(soup.prettify()) 





import requests 
from bs4 import BeautifulSoup  
r = requests.get('https://cognifyz.com/') 
soup = BeautifulSoup(r.content, 'html.parser')  
print(soup.title) 
print(soup.title.name) 
print(soup.title.parent.name) 






