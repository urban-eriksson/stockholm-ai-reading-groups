import math


N = 100

exit_flag = False
while not exit_flag: 

    total_glue = 2020

    for k in range(N, 0, -1):
        A = 625*(1 + 1/k**2 + 1/(k+1)**2)
        s = math.sqrt(A)
        glue_used = 0.15*4*s
        total_glue -= glue_used

    if total_glue < 0:
        exit_flag = True
    else:
        N += 1

    print(total_glue)


print(N-1)
