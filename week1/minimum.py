

'''
Function to find a minimum
'''

import numpy as np
from datetime import datetime

# Make array of data
arr=np.random.random((100))


# method 1
t1=datetime.now()

minN=10000  # a big number
for i in arr:
  if(i<minN):
    minN=i
t2=datetime.now()

# method 2
tt1=datetime.now()
fastMin=np.min(arr)
tt2=datetime.now()

print("Min is",minN,"in",t2-t1)
print("compared to",fastMin,"in",tt2-tt1)


