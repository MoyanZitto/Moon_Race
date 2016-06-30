#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 30 13:28:42 2016

@author: kevin
"""

import numpy as np 
import pandas as pd
import os

dataframe1 = pd.Series([])
dataframe2 = pd.Series([])
dataframe3 = pd.Series([])

data = open('datalist.txt').readlines()
for i in range(len(data)):
	dataframe1[i] = data[i][9:24]
	dataframe2[i] = data[i][34:49]
	dataframe3[i] = data[i][-3]

dataframe = pd.DataFrame([dataframe1,
                         dataframe2,
                         dataframe3]).T
dataframe.to_csv('dataframe.csv',encoding = 'utf-8',header = False,index = False)
