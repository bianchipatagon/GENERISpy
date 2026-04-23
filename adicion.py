import numpy as N
import matplotlib.pyplot as plt
from datetime import datetime
import pandas as pd
import seaborn as sns
from scipy.stats import spearmanr
from matplotlib.ticker import MultipleLocator
import matplotlib.patches as patches

ad = pd.read_csv('/home/emi/Documents/GENERIS/GENERISpy/adiciones.txt', header=0, delimiter=',', na_values='-999')

fig, axs = plt.subplots(1,3,figsize=(12,2),sharex=True, sharey=True)

axs[0].set_title('Tend', fontsize = 13, weight='bold')
axs[0].bar(ad['Anio'], ad['SolarT'], color='#FBAA1B')
axs[0].bar(ad['Anio'], ad['EolicaT'], bottom=ad['Solar'], color='#8FC73E')
axs[0].bar(ad['Anio'], ad['HidroT'], bottom=ad['Solar']+ad['Eolica'], color='#207653')
axs[0].legend(["Solar","Eólica","Hidro"], frameon=False,bbox_to_anchor=(0.9, 0.9), borderaxespad=0.,fontsize=10)
axs[0].set_xlim(2023, 2050)
axs[0].set_ylabel('[MW]', fontsize=12)

axs[1].set_title('Alt', fontsize = 13, weight='bold')
axs[1].bar(ad['Anio'], ad['Solar'], color='#FBAA1B')
axs[1].bar(ad['Anio'], ad['Eolica'], bottom=ad['Solar'], color='#8FC73E')
axs[1].bar(ad['Anio'], ad['Hidro'], bottom=ad['Solar']+ad['Eolica'], color='#207653')

axs[2].set_title('Solar dist.', fontsize = 13, weight='bold')
axs[2].plot(ad['Anio'], ad['cien'], color='#FBAA1B')
axs[2].plot(ad['Anio'], ad['mil'], color='#FBAA1B')
axs[2].fill_between(ad['Anio'], 0, ad['mil'], alpha=0.5, color='#FBAA1B', label='1000 MW')
axs[2].fill_between(ad['Anio'], 0, ad['cien'], alpha=0.8, color='#FBAA1B', label='100 MW')
axs[2].legend( frameon=False,bbox_to_anchor=(0.4, 0.7), borderaxespad=0.,fontsize=10)

fig.subplots_adjust(wspace=0.1)

plt.savefig('ad.svg', dpi=300, bbox_inches="tight")
