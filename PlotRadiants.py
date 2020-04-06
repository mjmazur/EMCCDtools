import numpy as np
import pandas as pd

filename='orbit.txt'


f=open(filename)
lines=f.readlines()

time = lines[1]
ra = lines[5]
dec = lines[6]
vel = lines[7]

value_array = np.empty((0,8))

values = str(time.split()[1]) + ' ' + str(time.split()[2]) + ' ' + str(ra.split()[1]) + ' ' + str(ra.split()[3]) + ' ' + str(dec.split()[1]) + ' ' + str(dec.split()[3]) + ' ' + str(vel.split()[1]) + ' ' + str(vel.split()[3])
value_array = np.vstack((value_array, values.split()))
value_array = np.vstack((value_array, values.split()))

print(value_array[1][1])