import numpy as N
import matplotlib.pyplot as plt
from datetime import datetime
import pandas as pd
import seaborn as sns
from scipy.stats import spearmanr
from matplotlib.ticker import MultipleLocator
import matplotlib.patches as patches
import matplotlib.gridspec as gridspec

ad = pd.read_csv('/home/emi/Documents/GENERIS/GENERISpy/demanda.txt', header=0, delimiter=';', na_values='-999')

fig, (ax1,ax2) = plt.subplots(1,2,figsize=(6.5,3),sharex=True, sharey=True)

ax1.plot(ad['Anio'], ad['Ten'], color='#A1140B', label='TEN')
ax1.plot(ad['Anio'], ad['TenGD'], color='#A1140B', alpha=0.7, label='TEN-GD', linestyle = '--')
ax1.set_ylabel('demanda \n[10^3 GWh]', fontsize=13)
ax1.tick_params("x", rotation=90)
ax1.legend(frameon=False,bbox_to_anchor=(0.45, 0.9), borderaxespad=0.,fontsize=10)


ax2.plot(ad['Anio'], ad['Alt'], color='#207653', label='ALT')
ax2.plot(ad['Anio'], ad['AltGD'], color='#207653', alpha=0.7, label='ALT-GD', linestyle = '--')
# ~ ax1.legend( frameon=False,bbox_to_anchor=(2.8, 0.7), borderaxespad=0.,fontsize=10)
ax2.tick_params("x", rotation=90)
ax2.legend(frameon=False,bbox_to_anchor=(0.45, 0.9), borderaxespad=0.,fontsize=10)


ax2.set_xlim(2025, 2050)

# ~ axs[2].legend( frameon=False,bbox_to_anchor=(0.4, 0.7), borderaxespad=0.,fontsize=10)

fig.subplots_adjust(wspace=0.1)

plt.savefig('demand.svg', dpi=300, bbox_inches="tight")
