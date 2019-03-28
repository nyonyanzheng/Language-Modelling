# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 17:29:00 2019

@author: Yan Zheng
"""


# Quotes Dataset
text = open('./Quotables-master/author-quote.txt', 'r', encoding = "utf8").read().splitlines()
text[0:5]

import re
re.split(r'\t+', text[0])


