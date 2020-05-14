# -*- coding: utf-8 -*-
"""
Created on Thu May 14 19:04:14 2020

@author: Adi
"""

import os
import random

os.chdir(r'D:\Downloads\Audio\Auto')


i = 0
total = len(os.listdir())
tempic = random.sample(range(total), total)

for file in os.listdir():
    os.rename(file,str(tempic[i])+'_'+file)
    i+=1
    
