import sys
import numpy as np
from scipy.constants import c 
from scipy.fftpack import fft
# Number of sample points
fin = open("output_tcf_col11_t10000", 'r')
lines = fin.readlines()

print(len(lines))
Ncol = int(2)
#Ncol = int(sys.argv[1])
#tcf_duration = int(sys.argv[2])
col_value = []

for i, line in enumerate(lines):
    line_split = line.split()
    #print(line_split[1])
    col_value.append(line_split[Ncol-1])
print(len(col_value))
print(col_value[0], col_value[1])
print(c)
fin.close()

col_array = np.array(col_value)


N = len(col_value)
# sample spacing
T = 1.0
x = np.linspace(0.0, N*T, N)
y = col_array
#y = np.sin(50.0 * 2.0*np.pi*x) + 0.5*np.sin(80.0 * 2.0*np.pi*x)
yf = fft(y)
xf = np.linspace(0.0, 1.0/(2.0*T), N//2)
xfc = xf*(1.0/(c*100*10E-15)) 

#fout = open('ft_out', 'w')
#for i in range(len(xfc)):
#    fout.write(f'{i}' + '    ' + f'{xfc[i]}' + '\n' )
#fout.close()

import matplotlib.pyplot as plt
plt.plot(xfc, 2.0/N * np.abs(yf[0:N//2]))
plt.grid()
plt.show()