import numpy as np


res = []

for j in range(10000):
    sp1 = 5
    counter1 = 0
    while sp1 != 0 and counter1 < 1000 :
        if np.random.randint(0,3) == 2:
            sp1 += 1
        else:
            sp1 -= 1
        counter1 += 1


    sp2 = -5
    counter2 = 0
    while sp2 != 0 and counter2 < 1000:
        if np.random.randint(0,3) == 2:
            sp2 += 1
        else:
            sp2 -= 1
        counter2 += 1

    if sp1 == 0 and sp2 == 0:
        res.append(counter1 < counter2)
        print(str(len(res)) + ',' + str(np.sum(res)) + ',' + str(np.sum(res)/len(res)))


print('hej')