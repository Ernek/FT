import sys
import numpy as np
from scipy.constants import c 
from scipy.fftpack import fft
import math
# Number of sample points
fin = open("output_tcf_col11_t10000", 'r')
lines = fin.readlines()

#print(len(lines))
Ncol = int(2)
#Ncol = int(sys.argv[1])
#tcf_duration = int(sys.argv[2])
col_value = []

for i, line in enumerate(lines):
    line_split = line.split()
    #print(line_split[1])
    col_value.append(line_split[Ncol-1])
#print(len(col_value))
#print(col_value[0], col_value[1])
fin.close()

col_array = np.array(col_value)

new_array = np.zeros(len(col_array))
for j in range(len(col_array)):
    g = float(col_array[j])*math.sqrt(1-j/len(col_array))
    new_array[j] = g

fout2 = open('ft_out2', 'w')
for i in range(len(new_array)):
    fout2.write(f'{i}' + '    ' + f'{new_array[i]}' + '\n' )
fout2.close()
#print(new_array[0], new_array[1])

N = len(col_value)
# sample spacing
T = 1.0   # T in fs
print(c)
x = np.linspace(0.0, N*T, N)
y = col_array

print(np.shape(x),np.shape(y))
#y = np.sin(50.0 * 2.0*np.pi*x) + 0.5*np.sin(80.0 * 2.0*np.pi*x)
yf = fft(y)
#xf = np.linspace(0.0, 1.0/(2.0*T), N//2)
#xinv = np.linspace(0.0, 1.0/T, N//2)
xf = np.linspace(0.0, 1.0/(2.0*T), N//2)
print(1e-15)
xfc = xf*(1.0/(c*100*1e-15)) 
print(xf, xfc)
print(np.shape(xf), np.shape(xfc))
print(yf[0], yf[1], yf[2], yf[3], yf[4])

fout = open('ft_out', 'w')
for i in range(len(xfc)):
    yvalue = 2.0/N * abs(yf[i])
    fout.write(f'{xfc[i]}' + '    ' + f'{yvalue}' + '\n' )
fout.close()


y3 = new_array
yf3 = fft(y3)
#xf = np.linspace(0.0, 1.0/(2.0*T), N//2)
#xinv = np.linspace(0.0, 1.0/T, N//2)
xf3 = np.linspace(0.0, 1.0/(2.0*T), N//2)
xfc3 = xf3*(1.0/(c*100*1e-15)) 
#print(xf, xfc)
#print(np.shape(xf), np.shape(xfc))

fout3 = open('ft_out3', 'w')
for i in range(len(xfc3)):
    yvalue3 = 2.0/N * abs(yf3[i])
    fout3.write(f'{xfc3[i]}' + '    ' + f'{yvalue3}' + '\n' )
fout3.close()



import matplotlib.pyplot as plt
#plt.plot(x,y)
#plt.show()
plt.plot(xfc, 2.0/N * np.abs(yf[0:N//2]))
plt.grid()
#plt.plot(xfc, np.abs(yf[0:N//2]))
plt.show()