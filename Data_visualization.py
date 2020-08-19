# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 18:22:13 2020

@author: rakes
"""


class DataVisualization:
    
    def __init__(self):
        print("Visualization object created")
        
    def boxplot(self,x= None):
        self.x = x
        fig = sns.distplot(self.x)
        return fig
    
    def barplot(self,x= None,y=None,z= None):
        self.x = x
        self.y = y
        self.z = z
        fig = sns.barplot(x=self.x, y=self.y, hue=self.z)
        return fig
    
    