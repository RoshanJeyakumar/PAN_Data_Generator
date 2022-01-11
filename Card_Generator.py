#!/usr/bin/env python
# coding: utf-8

# # Automatic Card Generation from Template 
# ## *Image Manipulation using Python*
# 
# ---
# 
# ```bash
# pip install pillow
# ```

# In[1]:


import pandas as pd
from PIL import Image, ImageDraw, ImageFont


# In[2]:


df = pd.read_csv("PAN_data.csv")


# In[3]:


df


# In[4]:


records = df.to_dict(orient='records')



# In[5]:


font = ImageFont.truetype("OpenSans-Semibold.ttf", size=17)


# In[6]:


def generate_card(data):
    template = Image.open("Pan_final.jpg")
    draw = ImageDraw.Draw(template)
    draw.text((26,283), str(data['Name']), font=font, fill='black')
    draw.text((29,374), data['Date of Birth'], font=font, fill='black')
    return template


# In[7]:

i = 0
for record in records:
    i+=1
    card = generate_card(record)
    card.save("Record" + str(i) + ".jpg")

