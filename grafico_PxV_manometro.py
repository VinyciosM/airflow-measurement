import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from scipy import stats

#Gráfico referente à pressão no manômetro para diferentes tensões 

voltagem = np.asarray([2.5,3,3.5,4,4.5,5,5.5,6,6.5,7,7.5,8,8.5,9,9.5,10,10.5,11,11.5,12,12.5,13,13.5,14,14.5,15]) 
p1 = np.asarray([2.4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3.7,0,1.2,1.2,0])
p2 = np.asarray([14.6,19.5,14.6,14.6,19.5,19.5,19.5,19.5,24.4,19.5,24.4,29.3,29.3,29.3,34.1,34.1,34.1,39.0,39.0,39.0,39.0,43.9,48.8,48.8,48.8,48.8])

erro = [0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5] 



plt.errorbar(voltagem,p1, yerr=erro, fmt='o',markersize = 5,mfc = 'red',mec='black',ecolor='black',capsize=5,markeredgewidth=.8) 
plt.errorbar(voltagem,p2, yerr=erro, fmt='o',markersize = 5,mfc = 'green',mec='black',ecolor='black',capsize=5,markeredgewidth=.8) 

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

plt.plot(volt_n1,new_p1,color='blue',label = f'Pressão 1: a = ({38}$\pm${1})E-3; b = ({-0.6}$\pm${0.1})E-2')

plt.plot(volt_n2,new_p2,color='orange',label = f'Pressão 2: a = ({3.0}$\pm${0.1}); b = ({44}$\pm${12})E-1')
plt.legend()


plt.show()