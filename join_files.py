# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 14:17:11 2019

@author: Yan Zheng
"""

import json

# Read data from source 1: data scrapped from website
data1 = []
with open('pickup_lines_cleaned.json', 'r', encoding = "utf8") as json_data:
    for line in json_data: 
        data1.append(json.loads(line))

data2 = []
for line in range(len(data1)): 
    data2.append(data1[line]["text"])

# Check for empty elements
for i in range(len(data1)):
    if data1[i]["text"] =='':
        print(str(i) + ' is empty')

# Read data from source 2: github        
data3 = open('pickup_lines_github.txt', 'r', encoding = "utf8").read().splitlines()

# Check for empty elements
for i in range(len(data3)):
    if data3[i] =='':
        print(str(i) + ' is empty')

# Join both data source
data = data2 + data3

# Remove duplicated and empty data
data_unique = [i for i in list(set(data)) if i != '']
        

outFile = open("pickup_lines_all.txt", "w", encoding = "utf8")
for line in data_unique:
  # write line to output file
  outFile.write(line)
  outFile.write("\n")
outFile.close()

