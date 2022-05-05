#!/usr/bin/env python
# coding: utf-8

# In[28]:


# Import Splinter, BeautifulSoup, and Pandas
from splinter import Browser
from bs4 import BeautifulSoup as soup
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager


# In[29]:


# Set the executable path and initialize Splinter
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# In[30]:


# Visit the Mars NASA news site
url = 'https://redplanetscience.com/'
browser.visit(url)

# Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)


# In[31]:


# Convert the browser html to a soup object and then quit the browser
html = browser.html
news_soup = soup(html, 'html.parser')

slide_elem = news_soup.select_one('div.list_text')


# In[32]:


slide_elem.find('div', class_='content_title')


# In[33]:


# Use the parent element to find the first a tag and save it as `news_title`
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title


# In[34]:


# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p


# # JPL Space Images

# In[35]:


# Visit URL
url = 'https://spaceimages-mars.com'
browser.visit(url)


# In[36]:


# Full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()


# In[37]:


html = browser.html
img_soup = soup(html, 'html.parser')
img_soup


# In[38]:


# Relative Image URL
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel


# In[39]:


img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url


# # Mars Facts

# In[40]:


df = pd.read_html('https://galaxyfacts-mars.com')[0]
df.head()


# In[41]:


df.columns=['Description', 'Mars', 'Earth']
df.set_index('Description', inplace=True)
df


# In[42]:


df.to_html()


# # D1: Scrape High-Resolution Mars’ Hemisphere Images and Titles

# In[43]:


# 1. Use browser to visit the URL 
url = 'https://marshemispheres.com/'
browser.visit(url)


# In[45]:


# browser.find_by_css('a.product-item h3')[0].click()
# element = browser.find_link_by_text('Sample').first
# print(element['href'])
# browser.find_by_css("h2.title").text


# In[46]:


# 2. Create a list to hold the images and titles.
hemisphere_image_urls = []


# In[47]:


# 3. Write code to retrieve the image urls and titles for each hemisphere.
for i in range(4):
    #create empty dictionary
    hemispheres = {}
    browser.find_by_css('a.product-item h3')[i].click()
    element = browser.find_link_by_text('Sample').first
    img_url = element['href']
    title = browser.find_by_css("h2.title").text
    hemispheres["img_url"] = img_url
    hemispheres["title"] = title
    hemisphere_image_urls.append(hemispheres)
    browser.back()


# In[48]:


# 4. Print the list that holds the dictionary of each image url and title.
hemisphere_image_urls


# In[49]:


# 5. Quit the browser
browser.quit()


# In[ ]:




