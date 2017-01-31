import numpy as np
import matplotlib.pyplot as plt

nums = [2, 7, 1, 5, 10] # 5 numbers
can = [x/10.0 for x in range(101)] # 100 numbers

fig = plt.figure()

ys = []
xs = []
for i in can:
    new = 0
    for j in nums:
        new += (j - i)**2
    ys.append(new)
    xs.append(i)

plt.plot(xs, ys)

fig.savefig('foo.png')
