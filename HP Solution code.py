#!/usr/bin/env python
# coding: utf-8

# In[3]:


import requests
import bs4


# In[100]:


rating = []
product_name = []
review = []
data = []
base_url = "https://www.pcmag.com/categories/printers/brands/hp?page={}.html"

for n in range(1,9):
    
    url = base_url.format(n)
    res = requests.get(url)
    
    soup = bs4.BeautifulSoup(res.text,"lxml")
    product = soup.select(".w-2\/3.pr-0.md\:flex-row.md\:pr-12.md\:w-3\/4")
    
    for m in range(1,21):
        product_no=product[m-1]
    
        rating.append(product_no.select(".ml-1.mr-3")[0].getText())
        product_name.append(product_no.select("a")[0]['data-item'])
        review.append(product_no.select(".line-clamp-2.text-gray-darker")[0].getText())
    
    
data.append(rating + product_name + review)

    
    


# In[ ]:




