#1
import numpy as np
values = list(map(int,input("12개 입력하세요").split()))
values = np.sort(values).reshape(3,4)
values_mean = values.mean(axis=1)
values_mean.reshape(3,1) * np.ones((3,4))
(values> values_mean).sum(axis = 1)

#2
arr_10 = np.random.random((10,10))

np.savetxt('data.csv',arr_10)
arr_10 = arr_10[::2,:] + arr_10[1::2,:]
arr_10 = arr_10[:,::2] + arr_10[:,1::2]
arr_sorted = np.sort(arr_10,axis = 1)
np.savetxt('sorted_data.csv',arr_sorted)