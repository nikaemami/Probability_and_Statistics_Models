#!/usr/bin/env python
# coding: utf-8

# In[13]:


import numpy as np
def estimation(n):
    in_circle=0
    for i in range (n):
        x=np.random.uniform(0,2)
        y=np.random.uniform(0,2)
        if((((x-1)**2+(y-1)**2)**(0.5))<1):
            in_circle+=1
    return (float(in_circle/n))

def repeats (n):
    estimate=4*(estimation(n))
    print("\nn=",n)
    print("Pi =",estimate)
    print("accuracy =",(np.abs(float((np.pi - estimate)/(np.pi)))))
    
r1=repeats(100)
r2=repeats(1000)
r3=repeats(10000)
r4=repeats(100000)

