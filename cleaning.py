# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 07:06:00 2020

@author: rakes
"""

class cleaning:
    
    def __init__(self):
        print("Cleaning Object Created")
    
    def get_missing_values(self, data):
        
        print('='*20, " Checking Missing Values", "="*20)
        
        missing_values = data.isnull().sum()
        
        missing_values.sort_values(ascending = False, inplace = True)
        
        return missing_values
    
    def fillna(self, data, fill_strategies):
        for columns, strategies in fill_strategies.items():
            if strategies == 'None':
                data[columns] = data[columns].fillna('None')
            elif strategies == 'Mean':
                data[columns] = data[columns].fillna(data[column].mean())
            else:
                print("{}: There is no such Strategy".format(strategies))
        return data


