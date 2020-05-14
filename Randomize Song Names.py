# -*- coding: utf-8 -*-
"""
Created on Thu May 14 19:04:14 2020

@author: Adi
"""

'''
Randomize the order of the files in a specific folder.
Generates random numbers based on the number of files.
Attaches random numbers to the beginning of the file name.
Does not repeat the random numbers.
'''

import os
import random

os.chdir(r'D:\Downloads\Audio\Auto')


i = 0
total = len(os.listdir())
tempic = random.sample(range(total), total)

for file in os.listdir():
    os.rename(file,str(tempic[i])+'_'+file)
    i+=1
    
