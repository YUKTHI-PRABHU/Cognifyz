#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests 
   
r = requests.get('https://cognifyz.com/') 
print(r)  
print(r.content)


# In[2]:


import requests 
r = requests.get('https://cognifyz.com/') 
print(r.url) 
print(r.status_code)


# In[3]:


import requests 
from bs4 import BeautifulSoup 
r = requests.get('https://cognifyz.com/') 
print(r) 
soup = BeautifulSoup(r.content, 'html.parser') 
print(soup.prettify()) 


# In[4]:


import requests 
from bs4 import BeautifulSoup  
r = requests.get('https://cognifyz.com/') 
soup = BeautifulSoup(r.content, 'html.parser')  
print(soup.title) 
print(soup.title.name) 
print(soup.title.parent.name) 


# In[ ]:




