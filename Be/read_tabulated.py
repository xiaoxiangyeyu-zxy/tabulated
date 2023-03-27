import numpy as np
import math

name = "Be"  # change
temp_index = 21  # change
den_index = 21  # change

K = 11604.5221
joule2erg = 1.0e7
number_one_line = 4
number_len = 12
head_line = 4 + int(math.ceil(temp_index/number_one_line)) + int(math.ceil(den_index/number_one_line))  # not need
one_piece = int(math.ceil(temp_index*den_index/number_one_line))  # columns of one piece of data

press_ion = []
press_ele = []
energy_ion = []
energy_ele = []


def str_float(data):
    a1 = float(data[0:number_len])
    a2 = float(data[number_len:2*number_len])
    a3 = float(data[2*number_len:3*number_len])
    a4 = float(data[3 * number_len:4 * number_len])
    return a1, a2, a3, a4


def appendthem(a, a1, a2, a3, a4):
    a.append(a1)
    a.append(a2)
    a.append(a3)
    a.append(a4)
    return a


f = open("Be-006-imx.cn4", encoding='utf-8')  # change
# skip the headlines
for i in range(head_line):
    next(f)

for i in range(2*one_piece):
    next(f)

for i in range(one_piece):
    if i != one_piece - 1:
        line = f.readline()
        p1, p2, p3, p4 = str_float(line)
        press_ion = appendthem(press_ion, joule2erg*p1, joule2erg*p2, joule2erg*p3, joule2erg*p4)
    else:
        line = f.readline()
        p1 = float(line[0:number_len])
        press_ion.append(p1*joule2erg)

for i in range(one_piece):
    if i != one_piece - 1:
        line = f.readline()
        p1, p2, p3, p4 = str_float(line)
        press_ele = appendthem(press_ele, joule2erg*p1, joule2erg*p2, joule2erg*p3, joule2erg*p4)
    else:
        line = f.readline()
        p1 = float(line[0:number_len])
        press_ele.append(p1*joule2erg)

for i in range(2*one_piece):
    next(f)

for i in range(one_piece):
    if i != one_piece - 1:
        line = f.readline()
        p1, p2, p3, p4 = str_float(line)
        energy_ion = appendthem(energy_ion, joule2erg*p1, joule2erg*p2, joule2erg*p3, joule2erg*p4)
    else:
        line = f.readline()
        p1 = float(line[0:number_len])
        energy_ion.append(p1*joule2erg)

for i in range(one_piece):
    if i != one_piece - 1:
        line = f.readline()
        p1, p2, p3, p4 = str_float(line)
        energy_ele = appendthem(energy_ele, joule2erg*p1, joule2erg*p2, joule2erg*p3, joule2erg*p4)
    else:
        line = f.readline()
        p1 = float(line[0:number_len])
        energy_ele.append(p1*joule2erg)

f.close()

# print(press_ion)
# print(press_ele)
# print(energy_ion)
# print(energy_ele)

press_tot = np.array(press_ele)+np.array(press_ion)
energy_tot = np.array(energy_ele)+np.array(energy_ion)

press_tot = press_tot.reshape((-1, 1))
energy_tot = energy_tot.reshape((-1, 1))

pout = np.hstack((energy_tot, press_tot))
print(pout)

np.savetxt(name+"_"+str(den_index)+"_"+str(temp_index)+"_den_temp.txt", pout)
