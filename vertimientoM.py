import numpy as N
import matplotlib.pyplot as plt
from datetime import datetime
import pandas as pd
import seaborn as sns
from scipy.stats import spearmanr
from matplotlib.ticker import MultipleLocator
import matplotlib.patches as patches

ad = pd.read_csv('/home/emi/Documents/GENERIS/GENERISpy/vertimientoM2.txt', header=0, delimiter=';', na_values='-999')
dif = pd.read_csv('/home/emi/Documents/GENERIS/GENERISpy/vertimientoDIF.txt', header=0, delimiter=';', na_values='-999')

print(ad)
# ~ fig, (ax1,ax2) = plt.subplots(2,1,figsize=(7,4),sharex=True)
fig, (ax1, ax2) = plt.subplots(2, 1,figsize=(7,4),sharex=True,gridspec_kw={'height_ratios': [3, 1]} )

ax1.set_ylim(0, 4300)
ax1.set_xlim(2022.5, 2050.5)
ax1.bar(ad['anio'], ad['Solar'], color='#FBAA1B')
ax1.bar(ad['anio'], ad['Eolica'], bottom=ad['Solar'], color='#8FC73E')
ax1.bar(ad['anio'], ad['Hidro'], bottom=ad['Solar']+ad['Eolica'], color='#207653')
# ~ ax1.set_ylabel('[GWh]', fontsize=12)
# ~ ax2.set_yticks([0, 500, 1000, 1500, 2000, 2500, 3000, 3500, 4000])   
ax1.legend(["Solar","Eólica","Hidro"], frameon=False,bbox_to_anchor=(0.2, 0.9), borderaxespad=0.,fontsize=10)

ax3 = ax1.twinx()
ax3.plot(ad['anio'], ad['Porc'],'.', color = 'black', markersize = 10)
ax3.set_ylabel('% renovables', fontsize=12)

ax2.bar(dif['anio'], dif['dif'], color='#6D6F70')
ax2.legend(["reducción \nvertimiento"], frameon=False,bbox_to_anchor=(0.235, 0.9), borderaxespad=0.,fontsize=10)

fig.subplots_adjust(wspace=0.1)
fig.text(0.0045, 0.5, '[GWh]', va='center' ,fontsize=14, rotation='vertical')  

plt.savefig('vertM.svg', dpi=300, bbox_inches="tight")
