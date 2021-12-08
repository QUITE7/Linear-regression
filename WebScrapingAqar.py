# -*- coding: utf-8 -*-
"""
Created on Sat Nov 27 16:40:03 2021

@author: Huawei
"""

from bs4 import BeautifulSoup
import pandas as pd
import requests
#import re







#brands = [soup.select('p.brand')]
#description =[soup.select('p.description')]
#pre_reduction =[soup.select('span.pre_reduction')]
#reduction =[soup.select('span.reduction')]
#reduction_tag =[soup.select('span.reduction_tag')]

brands=[]
description=[]
pre_reduction=[]
reduction=[]
reduction_tag=[]

list = []


url="https://sa.aqar.fm/%D9%81%D9%84%D9%84-%D9%84%D9%84%D8%A8%D9%8A%D8%B9/%D8%A7%D9%84%D8%B1%D9%8A%D8%A7%D8%B6/"
for pageN in range(100):#we want 100   
   
    i=pageN+1700
    page=str(i)
    url1="https://sa.aqar.fm/%D9%81%D9%84%D9%84-%D9%84%D9%84%D8%A8%D9%8A%D8%B9/%D8%A7%D9%84%D8%B1%D9%8A%D8%A7%D8%B6/"
    url=url1+page

    response = requests.get(url)
    page=response.content
    soup = BeautifulSoup(page, "lxml")
    
    brands = soup.select('a.listTitle')#name
    reduction =soup.select('span.price')#price
    description =soup.select('span.size')#area
    pre_reduction =soup.select('span.bed')#rooms    

    reduction_tag =soup.select('span.bath')#bath

    for index in range(0, len(pre_reduction)):
	     brands_string = brands[index].get_text()
	     des_string = description[index].get_text()
	     pre_string = pre_reduction[index].get_text()
	     red_string = reduction[index].get_text()
	     tag_string = reduction_tag[index].get_text()
	

	     data = {"Estate": brands_string,
			"Area": des_string,
			"Roams": pre_string,
			"Price": red_string,
			"Baths": tag_string}
	     list.append(data)
    
    
df1 = pd.DataFrame(list)
df1['city']="riyad"
df1.to_csv('NewData16.csv')
df1


