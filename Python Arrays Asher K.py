#import
import numpy as np
import pandas as pd
from numpy import random
#1 make array
array=random.randint(100, size=(5,5))
#2 print array
print(array)
#3 print 2nd row 3rd column
second_third=array[1][2]
print(second_third)
#4 print sum
def sum_array(arr):
    return np.sum(arr)
total_sum = sum_array(array)
print(total_sum)
#5 mean of each row
mean=np.mean(array,axis=1)
print(mean)
#6 get the max
df = pd.DataFrame(array)

print(df.max())
