import matplotlib.pyplot as plt
import numpy as np

def select_sort(l):
    for i in range(len(l)):
        min = i
        for j in range(i+1,len(l)):
            if l[j] < l[min]:
                min = j
        l[i],l[min] = l[min],l[i]
        
    return l


rng = np.random.default_rng()

x = np.linspace(1,100,100)
y = rng.integers(1,101,100)

s_y = select_sort(y.copy())

plt.subplot(1,2,1)
plt.bar(x,y,width=1)

plt.subplot(1,2,2)
plt.bar(x,s_y,width=1)

plt.show()