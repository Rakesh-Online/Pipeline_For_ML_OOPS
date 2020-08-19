# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 18:19:55 2020

@author: rakes
"""

class Data_Understanding:
    
    def __init__(self):
        print("Understanding object created")
    
    def all_about_my_data(self, data):
        
        print("Here is some Basic Ground Info about your Data:\n")
    
        # Shape of the dataframe
        print("Number of Instances:",data.shape[0])
        print("Number of Features:",data.shape[1])
    
        # Summary Stats
        print("\nSummary Stats:")
        print(data.describe())