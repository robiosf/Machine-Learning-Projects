# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 14:57:39 2020

@author: Zhizheng.Wang
"""

from sklearn import svm
from sklearn import datasets
import matplotlib.pyplot as plt

svc = svm.SVC(gamma=0.001, C=100)

digits = datasets.load_digits()
print(digits.DESCR)

digits.images[0]

plt.imshow(digits.images[0], cmap=plt.cm.gray_r, interpolation='nearest')

digits.target

digits.target.size

plt.subplot(321)
plt.imshow(digits.images[1791], cmap=plt.cm.gray_r, interpolation='nearest')
plt.subplot(322)
plt.imshow(digits.images[1792], cmap=plt.cm.gray_r, interpolation='nearest')
plt.subplot(323)
plt.imshow(digits.images[1793], cmap=plt.cm.gray_r, interpolation='nearest')
plt.subplot(324)
plt.imshow(digits.images[1794], cmap=plt.cm.gray_r, interpolation='nearest')
plt.subplot(325)
plt.imshow(digits.images[1795], cmap=plt.cm.gray_r, interpolation='nearest')
plt.subplot(326)
plt.imshow(digits.images[1796], cmap=plt.cm.gray_r, interpolation='nearest')

svc.fit(digits.data[1:1790], digits.target[1:1790])

svc.predict(digits.data[1791:1976])

digits.target[1791:1976]
