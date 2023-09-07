import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from scipy import stats


voltagem = np.asarray([3.00,4.00,5.00,6.00,7.00,8.00,9.00,10.00,11.00,12.00,13.00,14.00,15.00,16.00,17.00,18.00,19.00,20.00,21.00])
p1 = np.asarray([321.36,322.02,321.69,321.36,321.02,321.02,320.53,319.69,319.02,319.02,318.69,318.02,318.02,317.86,317.69,317.36,317.02,317.02,316.69])
p2 = np.asarray([321.06,321.72,321.72,321.72,321.39,322.06,322.06,321.72,321.72,321.72,321.72,321.39,321.06,321.06,321.06,321.06,321.06,321.06,320.72])

erro1 = [0.49,0.43,0.43,0.52,0.51,0.81,0.58,0.56,0.47,0.47,0.41,0.37,0.39,0.40,0.39,0.43,0.40,0.92,0.37] 
erro2 = [0.38,0.37,0.36,0.40,1.54,0.43,0.53,0.44,0.41,0.37,0.37,0.41,0.39,0.40,0.41,0.41,0.43,0.43,2.02]


plt.errorbar(voltagem,p1, yerr=erro1, fmt='o',markersize = 5,mfc = 'red',mec='black',ecolor='black',capsize=5,markeredgewidth=.8) 
plt.errorbar(voltagem,p2, yerr=erro2, fmt='o',markersize = 5,mfc = 'green',mec='black',ecolor='black',capsize=5,markeredgewidth=.8) 

plt.title('Pressão vs Voltagem',fontsize=14)

plt.xlabel('Tensão (V)', fontsize = 12)

plt.ylabel('Pressão (Pa)',fontsize=12)

plt.grid(axis='both',color='0.92')

c1 = np.polyfit(voltagem,p1,1)
c2 = np.polyfit(voltagem,p2,1)

f1 = np.poly1d(c1) 
f2 = np.poly1d(c2) 

volt_n1 = np.linspace(voltagem[0],voltagem[-1],50)
new_p1= f1(volt_n1) 

volt_n2 = np.linspace(voltagem[0],voltagem[-1],50)
new_p2= f2(volt_n2) 

a1, b1, r_value1, p_value1, std_err1 = stats.linregress(voltagem, p1)
a2, b2, r_value2, p_value2, std_err2 = stats.linregress(voltagem, p2)

plt.plot(volt_n1,new_p1,color='blue',label = f'Pressão 1 (a = {round(a1,5)}; b = {round(b1,5)})')

plt.plot(volt_n2,new_p2,color='orange',label = f'Pressão 2 (a = {round(a2,5)}; b = {round(b2,5)})')
plt.legend()


plt.show()
