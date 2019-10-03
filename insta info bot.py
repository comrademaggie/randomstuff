#!/usr/bin/env python
# coding: utf-8

# In[13]:


from time import sleep 
from random import randint
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


# In[17]:


followers = []
posts = []
following = []
description = []
url_from_ig = []


# In[18]:


driver = webdriver.Chrome('C:\\Windows\\System32\\Webdrivers\\chromedriver.exe')


# In[19]:




for link in df['ig_link']:
    try: 
        driver.get(link)
        followers.append(driver.find_element_by_xpath(".//*[@id='react-root']/section/main/div/header/section/ul/li[2]/a/span[@title]").get_attribute("title"))
        posts.append(driver.find_element_by_xpath(".//*[@id='react-root']/section/main/div/header/section/ul/li/a/span").text)
        following.append(driver.find_element_by_xpath(".//*[@id='react-root']/section/main/div/header/section/ul/li[3]/a/span").text)
    except: 
        followers.append(None)
        posts.append(None)
        following.append(None)

    try: 
        description.append(driver.find_element_by_xpath(".//*[@id='react-root']/section/main/div/header/section/div/span").text)
    except: 
        description.append(None)

    try: 
        url_from_ig.append(driver.find_element_by_xpath(".//*[@id='react-root']/section/main/div/header/section/div/span/following-sibling::a").text)

    except: 
        url_from_ig.append(None)
    


    sleep(randint(1,5))


df['followers'] = followers
df['posts'] = posts
df['following'] = following
df['description'] = description
df['url_from_ig'] = url_from_ig

