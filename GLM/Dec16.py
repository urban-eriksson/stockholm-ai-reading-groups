import numpy as np

frac = 0.82
N = 10000000
res = []


for i in range(N):
    person1 = np.random.uniform()
    person2 = np.random.uniform()

    if person1 <= frac and person2 <= frac:
        infec = np.random.uniform() < 0.025
    elif person1 <= frac and person2 > frac:
        infec = np.random.uniform() < 0.5
    elif person1 > frac and person2 <= frac:
        infec = np.random.uniform() < 0.05
    elif person1 > frac and person2 > frac:
        infec = True
    else:
        print('hej')

    res.append(infec)
        
print(np.sum(res)/N)

