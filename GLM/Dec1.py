import numpy as np

q = np.loadtxt('input.txt')

for i in range(len(q)):
    for j in range(len(q)):
        if i != j and q[i] + q[j] == 2020:
            print('Found:')
            print(q[i])
            print(q[j])
            print(q[i]*q[j])

for i in range(len(q)):
    for j in range(len(q)):
        for k in range(len(q)):
            if i != j and j!=k and q[i] + q[j] + q[k] == 2020:
                print('Found:')
                print(q[i])
                print(q[j])
                print(q[k])
                print(q[i]*q[j]*q[k])


print('hej')