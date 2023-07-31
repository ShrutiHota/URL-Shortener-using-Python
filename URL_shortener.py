#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pyshorteners
long_url = input("Enter the URL to shorten: ")
 
#TinyURL shortener service
type_tiny = pyshorteners.Shortener()
short_url = type_tiny.tinyurl.short(long_url)
 
print("The Shortened URL is: " + short_url)


# In[ ]:




