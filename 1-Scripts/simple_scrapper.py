#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 15 15:31:25 2022

Simple Scrapper based on the tutorial video:
https://www.youtube.com/watch?v=vIjXuYRLge8

It is an adaptation, considering a different website.

@author: gnmandrade
"""

from urllib.request import urlopen
from bs4 import BeautifulSoup

import pandas as pd

#####
# Download the data
#####

# Define the page to scrappe
url_to_scrappe = 'https://casa.sapo.pt/comprar-apartamentos/lisboa/'

# Create the communication interface
request_page = urlopen(url_to_scrappe)

# Get the data in the page
page_html = request_page.read()

# Close the connection
request_page.close()



#####
# Open chanel to store data
#####

filename = '2-Outputs/store_products.csv'
f = open(filename, 'w')

header = "property_type;property_location;price\n"

f.write(header)

#####
# Process the data
#####

# Create BeautifulSoup object
html_soup = BeautifulSoup(page_html, 'html.parser')

# Get list of items
store_items = html_soup.find_all('div', class_="property-info-content")

# Iterate lists of items to get name and price
for store_item in store_items:
    property_type = store_item.find('div', class_ = "property-type").text
    property_location = store_item.find('div', class_ = "property-location").text
    price = store_item.find('div', class_ = "property-price-value").text
    
    f.write(property_type + ';' + property_location + ';' + price + '\n')

#####
# Close chanel to store data
#####

f.close()