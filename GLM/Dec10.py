from datetime import datetime, timedelta
import numpy as np
import math

day = 10
month = 12
year = 2020
weekday = 3


days = np.array([])
months = np.array([])
years = np.array([])
weekdays = np.array([])




while t.year >= 2000:
    t = t - timedelta(days=1)


while t.year >= 1900:
    t2 = t + timedelta(days=365*8+2)
    print(t)
    print(t.weekday())
    print(t2.weekday())
    if (t.weekday()==5 or t.weekday() == 6) and t2.weekday()==0:
        print(t)
        print(t2)
    t = t - timedelta(days=1)

print('hej')