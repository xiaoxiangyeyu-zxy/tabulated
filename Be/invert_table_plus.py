import numpy as np
import math

name = 'Be'
temp_index = 21
den_index = 21

K = 11604.5221

lgdenmin = 16
lgdenmax = 26
dlgden = (lgdenmax-lgdenmin)/(den_index-1)

lgtempmin = np.log10(K/5)  # change
lgtempmax = 5 + np.log10(K/5)  # change
dlgtemp = (lgtempmax-lgtempmin)/(temp_index-1)

energy_index = 29
lgenergymin = 10.6
lgenergymax = 16.2
dlgenergy = (lgenergymax-lgenergymin)/(energy_index-1)

data = np.loadtxt("Be_21_21_den_temp.txt")

E = data[:, 0]
P = data[:, 1]

lgE = np.log10(E)
lgP = np.log10(P)

lgE = lgE.reshape((den_index, temp_index))
lgP = lgP.reshape((den_index, temp_index))

def gettp(i_den, lgenergy):
    lge_compare = lgE[i_den, :]
    lge_compare = (lge_compare - lgenergy).tolist()
    lge_index_1 = lge_compare.index(min(i for i in lge_compare if i > 0))
    lge_index_0 = lge_index_1-1
    delta_lge_1 = lgE[i_den, lge_index_1] - lgenergy
    delta_lge_0 = lgenergy - lgE[i_den, lge_index_0]
    delta_lge = lgE[i_den, lge_index_1]-lgE[i_den, lge_index_0]
    T_1 = lgtempmin + lge_index_1*dlgtemp
    T_0 = lgtempmin + lge_index_0*dlgtemp
    P_1 = lgP[i_den, lge_index_1]
    P_0 = lgP[i_den, lge_index_0]
    T_use = T_1*delta_lge_0/delta_lge + T_0*delta_lge_1/delta_lge
    P_use = P_1*delta_lge_0/delta_lge + P_0*delta_lge_1/delta_lge
    return T_use, P_use


min_lge = []
max_lge = []

for i in range(den_index):
    min_lge.append(min(lgE[i, :]))
    max_lge.append(max(lgE[i, :]))


# if max(min_lge) > lgenergymin:
#     print('warning!lgEmin is too small.')
#     sys.exit()
# if min(max_lge) < lgenergymax:
#     print('warning!lgEmax is too big.')
#     sys.exit()

data_new = [[]for i in range(den_index*energy_index)]
for i in range(den_index):
    for j in range(energy_index):
        index = i*energy_index+j
        lgenergy = j*dlgenergy + lgenergymin
        if lgenergy > max_lge[i] or lgenergy < min_lge[i]:
            T_print = -1
            P_print = -1
        else:
            T_print, P_print = gettp(i, lgenergy)
        data_new[index].append(T_print)
        data_new[index].append(P_print)

data_new = 10**np.array(data_new)
print(data_new)

with open(name+"_"+str(den_index)+"_"+str(energy_index)+"_den_energy_plus.txt", "w") as f:
    f.write('#'+' ')
    f.write(str(den_index)+' ')
    f.write(str(dlgden)+' ')
    f.write(str(10**lgdenmin)+'\n')
    f.write('#'+' ')
    f.write(str(energy_index)+' ')
    f.write(str(dlgenergy)+' ')
    f.write(str(10**lgenergymin) + '\n')
    np.savetxt(f, data_new)
f.close()
