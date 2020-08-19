# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 18:23:04 2020

@author: rakes
"""

class Gridsearch:
    def __init__(self):
        print("machine learning object created")
        
    def Linearmodel(self, data):
        X = data.iloc[:,:8]
        y = data.iloc[:,8:]
        X_train,X_test,y_train,y_test = train_test_split(X,y, test_size = 0.2, random_state= 9)
        reg = linear_model.LinearRegression()
        reg.fit(X_train, y_train)
        y_pred = reg.predict(X_test)
        print('Intercept',reg.intercept_)
        print("R2_score : ", r2_score(y_test, y_pred))
        print("mean_squared_error : ", mean_squared_error(y_test, y_pred))
        
        importance = reg.coef_[0]
        # summarize feature importance
        for i,j in enumerate(importance):
            print('Feature: %0d, Score: %.5f' % (i,j))
        # plot feature importance
        plt.bar([x for x in range(len(importance))], importance)
        plt.show()
        