import numpy as np
import math

data = np.loadtxt("Al_25_21_den_temp.txt")

energy = data[:, 0]

min_e = []
max_e = []

temp_index = 21
den_index = 25

for i in range(den_index):
    min_e.append(min(energy[i*temp_index:(i+1)*temp_index]))
    max_e.append(max(energy[i * temp_index:(i + 1) * temp_index]))

print(min_e)
print(max_e)

print(math.log10(min(min_e)))
print(math.log10(max(min_e)))

print(math.log10(min(max_e)))
print(math.log10(max(max_e)))
