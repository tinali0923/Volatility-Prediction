# -*- coding: utf-8 -*-
"""
Created on Sun Dec 03 01:21:00 2017

@author: Shawn Z
"""

from sklearn import linear_model
from sklearn.preprocessing import StandardScaler

#-----------------------------------standardize features-------------------------------
scaler=StandardScaler()
scaler.fit(X_train)
X_train_st=scaler.transform(X_train)

#-----------------------------Huber no regularizer changing epsilon-----------------------------------
huber_error=[]
huber_lamb_list=[]
for lamb in range(40,60,1):
    # different lamb
    huber_reg=linear_model.SGDRegressor (loss='huber',epsilon=lamb )
    huber_error_list=[]
    for train_index, test_index in kf.split(X_train_st):
        # for each lamb, perform cross validation
        X_ctrain, X_ctest = X_train_st[train_index], X_train_st[test_index]
        Y_ctrain, Y_ctest = Y_train.iloc[train_index], Y_train.iloc[test_index]
               
        huber_reg.fit(X_ctrain,Y_ctrain)
        error=np.mean((huber_reg.predict(X_ctest)-Y_ctest)**2)
        huber_error_list.append(error)
    huber_lamb_list.append(lamb)
    huber_error.append(np.mean(np.array(huber_error_list)))
    
fig = plt.figure(figsize=(13,9.5))
plt.subplots_adjust(top=0.5, bottom=0, left=0, right=1, hspace=0.3,wspace=0.25)
plt.subplot(121)
plt.plot(huber_lamb_list, huber_error, c='purple')
plt.title('Cross Validation Error Vs Huber regression epsilon (no regularization)', fontsize=18)
plt.xlabel('epsilon', fontsize=14)
plt.ylabel('Mean Square Error', fontsize=14)
plt.grid()

#----------------------------Huber wit l2 regularizer changing lambda----------------------------------
l1error_l2=[]
l1lamb2_list=[]
for lamb in range(10):
    # different lamb
    l1reg_l2=linear_model.SGDRegressor (loss='huber', penalty='l2',epsilon=50, alpha=lamb*0.001 )
    l1error_list=[]
    for train_index, test_index in kf.split(X_train_st):
        # for each lamb, perform cross validation
        X_ctrain, X_ctest = X_train_st[train_index], X_train_st[test_index]
        Y_ctrain, Y_ctest = Y_train.iloc[train_index], Y_train.iloc[test_index]
               
        l1reg_l2.fit(X_ctrain,Y_ctrain)
        error=np.mean((l1reg_l2.predict(X_ctest)-Y_ctest)**2)
        l1error_list.append(error)
    l1lamb2_list.append(lamb*0.001)
    l1error_l2.append(np.mean(np.array(l1error_list)))
    
fig = plt.figure(figsize=(13,9.5))
plt.subplots_adjust(top=0.5, bottom=0, left=0, right=1, hspace=0.3,wspace=0.25)
plt.subplot(122)
plt.plot(l1lamb2_list,l1error_l2, c='purple')
plt.title('Cross Validation Error Vs Huber regression Lambda (l2 regularizer)', fontsize=18)
plt.xlabel('Lambda', fontsize=14)
plt.ylabel('Mean Square Error', fontsize=14)
plt.grid()


#-------------------------------Fit the model------------------------------
huber_reg = linear_model.SGDRegressor (loss='huber',epsilon=50, alpha=3*0.001 )
huber_reg.fit(X_train_st, Y_train)
param_huber = pd.Series(huber_reg.coef_, index=X_train.columns)
error_train_huber=np.mean((huber_reg.predict(X_train_st)-Y_train)**2)
R2_train_huber=huber_reg.score(X_train_st,Y_train)




