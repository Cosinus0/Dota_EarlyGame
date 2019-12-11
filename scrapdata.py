# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 17:16:01 2019

@author: Nathan
"""

import requests
import lxml.html as lh
import pandas as pd
from collections import Counter
import matplotlib.pyplot as plt

####
#### Scrap Table Cells
####

url = 'https://dota2.gamepedia.com/Table_of_hero_attributes'

# Create a handle, page, to handle the contents of the website
page = requests.get(url)

# Table into a dataframe
data = pd.read_html(page.text)

# The table I need into dataframe
df = data[0]
Atts_lst = ['STR','STR','INT','AGI','AGI','STR','INT','INT','STR','AGI','AGI','STR','STR','AGI','STR','STR','INT','AGI','STR','INT','INT','INT','INT','INT','INT','STR','STR','AGI','STR','STR','STR','AGI','INT','INT','AGI','INT','AGI','STR','INT','STR','INT','AGI','INT','STR','STR','INT','INT','STR','INT','INT','AGI','AGI','STR','STR','STR','AGI','AGI','AGI','AGI','AGI','AGI','INT','INT','STR','AGI','INT','STR','INT','INT','AGI','AGI','AGI','STR','INT','STR','INT','INT','AGI','AGI','INT','STR','INT','AGI','INT','INT','INT','STR','AGI','STR','AGI','AGI','STR','INT','STR','INT','AGI','AGI','STR','STR','INT','STR','STR','AGI','STR','STR','STR',
            'AGI','AGI','AGI','AGI','INT','INT','INT','AGI','INT','INT','INT','STR','INT']

# Replacing nan column with Atts_lst

df['A'] = Atts_lst

# Pickle dataframe

df.to_pickle("./HeroData.pkl")
