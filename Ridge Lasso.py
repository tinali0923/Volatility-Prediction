# -*- coding: utf-8 -*-
"""
Created on Sat Dec 02 20:11:38 2017

@author: Shawn Z
"""

from sklearn import linear_model
from sklearn import metrics
from sklearn.model_selection import cross_val_score
import matplotlib.pyplot as plt
from sklearn.model_selection import KFold

#--------------------------------Split Data-------------------------------------
def train_test_split(X, y, test_size=0.2):
    i = int((1 - test_size) * X.shape[0]) + 1
    X_train, X_test = np.split(X, [i])
    y_train, y_test = np.split(y, [i])
    return X_train, X_test, y_train, y_test

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.33)

X_train.set_index(range(len(X_train))) #reset index to 0,1,2...
Y_train.set_index(range(len(X_train)))

#------------------------------Cross Validation-------------------------------
kf = KFold(n_splits=5)
error_l2=[]
lamb2_list=[]

for lamb in range(10):
    # Iterate different lamb 
    reg_l2=linear_model.Ridge (alpha = lamb*0.05, normalize=True)
    error_list=[]
    for train_index, test_index in kf.split(X_train):
        # for each lamb, perform 5 fold corss validation
        X_ctrain, X_ctest = X_train.iloc[train_index], X_train.iloc[test_index]
        Y_ctrain, Y_ctest = Y_train.iloc[train_index], Y_train.iloc[test_index]
               
        reg_l2.fit(X_ctrain,Y_ctrain)
        error=np.mean((reg_l2.predict(X_ctest)-Y_ctest)**2)
        error_list.append(error)
        
    lamb2_list.append(lamb*0.05)
    error_l2.append(np.mean(np.array(error_list))) # mean error for different lamb

# Draw Graphs
fig = plt.figure(figsize=(13,9.5))
plt.subplots_adjust(top=0.5, bottom=0, left=0, right=1, hspace=0.3,wspace=0.25)
plt.subplot(121)
plt.plot(lamb2_list,error_l2, c='purple')
plt.title('Cross Validation Error Vs L2 Lambda', fontsize=18)
plt.xlabel('Lambda', fontsize=14)
plt.ylabel('Mean Square Error', fontsize=14)
plt.grid()

error_l1=[]
lamb1_list=[]
for lamb in range(1,11,1):
    # Iterate different lamb 
    reg_l1=linear_model.Lasso (alpha = lamb*0.0005, normalize=True)
    error_list=[]
    for train_index, test_index in kf.split(X_train):
        # for each lamb, perform 5 fold corss validation
        X_ctrain, X_ctest = X_train.iloc[train_index], X_train.iloc[test_index]
        Y_ctrain, Y_ctest = Y_train.iloc[train_index], Y_train.iloc[test_index]
               
        reg_l1.fit(X_ctrain,Y_ctrain)
        error=np.mean((reg_l1.predict(X_ctest)-Y_ctest)**2)
        error_list.append(error)
        
    lamb1_list.append(lamb*0.0005)
    error_l1.append(np.mean(np.array(error_list))) # mean error for different lamb
# Draw Graphs
plt.subplot(122)
plt.plot(lamb1_list,error_l1,c='purple')
plt.title('Cross Validation Error Vs L1 Lambda', fontsize=18)
plt.xlabel('Lambda', fontsize=14)
plt.ylabel('Mean Square Error', fontsize=14)
plt.grid()


#-------------------------------Fit the model------------------------------
reg_l1 = linear_model.Ridge (alpha = 4*.0005, normalize=True)
reg_l1.fit(X_train, Y_train)
param_l1 = pd.Series(reg_l1.coef_, index=X_train.columns)
error_train_l1=np.mean((reg_l1.predict(X_train)-Y_train)**2)
R2_train_l1=reg_l1.score(X_train,Y_train)

reg_l2 = linear_model.Ridge (alpha = 4*0.05, normalize=True)
reg_l2.fit(X_train, Y_train)
param_l2 = pd.Series(reg_l2.coef_, index=X_train.columns)
error_train_l2=np.mean((reg_l2.predict(X_train)-Y_train)**2)
R2_train_l2=reg_l2.score(X_train,Y_train)
    
error_test_l1=np.mean((reg_l1.predict(X_test)-Y_test)**2)
R2_test_l1=reg_l1.score(X_test,Y_test)
error_test_l2=np.mean((reg_l2.predict(X_test)-Y_test)**2)
R2_test_l2=reg_l2.score(X_test,Y_test)


