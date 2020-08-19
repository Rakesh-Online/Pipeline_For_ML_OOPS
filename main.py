# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 18:33:47 2020

@author: rakes
"""

import pandas as pd 
import numpy as np 


from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error
from sklearn import linear_model
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import normalize

import cleaning
import model_building


class Final_step:
    
    def __init__(self,data):
        
        print('Final Step object created')
        
        #all data
        self.data = data
        
        #Create instance of objects
        #self._clean = cleaning()
        self._Understanding = Data_Understanding()
        #self._visualize = DataVisualization()
        self._gridsearch = Gridsearch()
        
    def data_understanding(self):
        
        self._Understanding.all_about_my_data(self.data)
        
    def gridsearch(self):
        self._gridsearch.Linearmodel(self.data)
        

data = pd.read_csv(r"C:\Users\rakes\Documents\Raq files\Data Science\Data sets\concrete.csv")
    
final = Final_step(data)

final.data_understanding()

