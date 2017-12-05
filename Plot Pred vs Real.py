# -*- coding: utf-8 -*-
"""
Created on Sun Dec 03 00:33:18 2017

@author: Shawn Z
"""

import matplotlib.pyplot as plt

def cutoutlier(arr):
    arr=np.array(arr)
    for i in range(len(arr)):
        if arr[i]>100:
            arr[i]=100
    return arr

fig = plt.figure(figsize=(11,9))
p=plt.scatter(Y_test,reg_l1.predict(X_test),s=0.5,c=cutoutlier(np.abs(reg_l1.predict(X_test)-Y_test)))
plt.xlim((1,150))
plt.ylim((1,150))
plt.plot([0,140],[0,140],c='m',linestyle='-.')
cbar=plt.colorbar(p)
cbar.set_label('absolute error', fontsize=16)
plt.xlabel('Real Vol', fontsize=16)
plt.ylabel('Predicted Vol', fontsize=16)
plt.title('Prediction vs Reality',fontsize=20)