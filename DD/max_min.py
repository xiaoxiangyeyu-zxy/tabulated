import numpy as np
import math

data = np.loadtxt("DD_21_21_den_temp.txt")  # change

energy = data[:, 0]

min_e = []
max_e = []

temp_index = 21  # change
den_index = 21  # change

for i in range(den_index):
    min_e.append(min(energy[i*temp_index:(i+1)*temp_index]))
    max_e.append(max(energy[i * temp_index:(i + 1) * temp_index]))

print(min_e)
print(max_e)

print(max(min_e))
print(math.log10(max(min_e)))
print(np.argmax(min_e))
print(min(max_e))
print(math.log10(min(max_e)))
print(np.argmin(max_e))
