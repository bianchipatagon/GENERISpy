import numpy as N
import matplotlib.pyplot as plt
from datetime import datetime
import pandas as pd
import seaborn as sns
from scipy.stats import spearmanr
from matplotlib.ticker import MultipleLocator
import matplotlib.colors as mcolors

costoT = pd.read_csv('/home/emi/Documents/GENERIS/GENERISpy/costoTEN.txt', header=0, delimiter=';', na_values='-99')
costoTGD = pd.read_csv('/home/emi/Documents/GENERIS/GENERISpy/costoTENGD.txt', header=0, delimiter=';', na_values='-99')

costoA = pd.read_csv('/home/emi/Documents/GENERIS/GENERISpy/costoALT.txt', header=0, delimiter=';', na_values='-99')
costoAGD = pd.read_csv('/home/emi/Documents/GENERIS/GENERISpy/costoALTGD.txt', header=0, delimiter=';', na_values='-99')

# --- Config ---
base_color = '#FBAA1B'   # single hue for all series
alpha_min  = 0.2
alpha_max  = 0.9
 
# --- Build per-layer colors with varying alpha ---
n = 4
alphas = N.linspace(alpha_min, alpha_max, n)
print(alphas)
r, g, b = mcolors.to_rgb(base_color)
colors = [(r, g, b, a) for a in alphas]
 
# --- Plot --- 
fig, ((ax1,ax2),(ax3,ax4)) = plt.subplots(2,2,figsize=(11, 5), sharey='row', sharex=True)

ax1.stackplot(costoT['ANIO'],costoT['GN']+costoT['HEAT'], costoT['CAP'], costoT['DEMANDA'], labels=['Combustible','Capital + O&M','Paneles GD'],  colors=colors)
ax1.plot(costoT['ANIO'],costoT['GN']+costoT['HEAT']+ costoT['CAP']+ costoT['DEMANDA'], color='#FBAA1B')
ax1.plot(costoT['ANIO'],costoT['GN']+costoT['HEAT']+ costoT['CAP'], color='#FBAA1B')
ax1.plot(costoT['ANIO'],costoT['GN']+costoT['HEAT'], color='#FBAA1B')
ax1.set_xlim(2023, 2050)
ax1.set_title('TEN', fontsize = 14, weight='bold')
ax1.yaxis.set_tick_params(labelsize=13)
ax1.xaxis.set_tick_params(labelsize=13)
# ~ ax1.set_ylabel('[MM U$D]', fontsize=12)

ax2.stackplot(costoA['ANIO'],costoA['GN'], costoA['CAP'], costoA['DEMANDA'], labels=['Combustible','Capital + O&M','Paneles GD'],  colors=colors)
ax2.plot(costoA['ANIO'],costoA['GN']+ costoA['CAP']+ costoA['DEMANDA'], color='#FBAA1B')
ax2.plot(costoA['ANIO'],costoA['GN']+ costoA['CAP'], color='#FBAA1B')
ax2.plot(costoA['ANIO'],costoA['GN'], color='#FBAA1B')
ax2.set_xlim(2023, 2050)
ax2.set_title('ALT', fontsize = 14, weight='bold')
ax2.xaxis.set_tick_params(labelsize=13)
ax2.legend(['Combustible','Capital + O&M','Paneles GD'], frameon=False,bbox_to_anchor=(1, 0.5), loc='center left', borderaxespad=0.,fontsize=14)

# ~ ax3.stackplot(costoTGD['ANIO'],costoTGD['GN']+costoTGD['HEAT'], costoTGD['CAP'], costoTGD['DEMANDA'], labels=['Combustible','Capital + O&M','Paneles GD'],  colors=colors)
ax3.fill_between(costoTGD['ANIO'], 0, costoTGD['DEMANDA'], color = '#FBAA1B', alpha = 0.66)
ax3.plot(costoTGD['ANIO'],costoTGD['DEMANDA'], color='#FBAA1B')
ax3.axhline(linewidth=1, color='black', label='_nolegend_')
ax3.stackplot(costoTGD['ANIO'],costoTGD['GN']+costoTGD['HEAT'], costoTGD['CAP'],  colors=colors)
ax3.plot(costoTGD['ANIO'],costoTGD['GN']+costoTGD['HEAT']+ costoTGD['CAP'], color='#FBAA1B')
ax3.plot(costoTGD['ANIO'],costoTGD['GN']+costoTGD['HEAT'], color='#FBAA1B')
ax3.set_xlim(2023, 2050)
ax3.set_title('(TEN-GD) - Ten', fontsize = 14, weight='bold')
ax3.yaxis.set_tick_params(labelsize=13)
ax3.xaxis.set_tick_params(labelsize=13)

ax4.fill_between(costoAGD['ANIO'], 0, costoAGD['DEMANDA'], color = '#FBAA1B', alpha = 0.66)
ax4.plot(costoAGD['ANIO'],costoAGD['DEMANDA'], color='#FBAA1B')
ax4.axhline(linewidth=1, color='black', label='_nolegend_')
ax4.stackplot(costoAGD['ANIO'],costoAGD['GN'], costoAGD['CAP'],  colors=colors)
ax4.plot(costoAGD['ANIO'],costoAGD['GN']+ costoAGD['CAP'], color='#FBAA1B')
ax4.plot(costoAGD['ANIO'],costoAGD['GN'], color='#FBAA1B')
ax4.set_xlim(2023, 2050)
ax4.set_title('(ALT-GD) - ALT', fontsize = 14, weight='bold')
ax4.yaxis.set_tick_params(labelsize=13)
ax4.xaxis.set_tick_params(labelsize=13)

fig.text(0.08, 0.5, '[MM U$D]', va='center' ,fontsize=13, rotation='vertical')  
fig.subplots_adjust(wspace=0.05)
plt.savefig('costo.svg', dpi=300, bbox_inches="tight")
