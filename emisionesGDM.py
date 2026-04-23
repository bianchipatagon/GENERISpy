import numpy as N
import matplotlib.pyplot as plt
from datetime import datetime
import pandas as pd
import seaborn as sns
from scipy.stats import spearmanr
from matplotlib.ticker import MultipleLocator

emis = pd.read_csv('/home/emi/Documents/GENERIS/GENERISpy/emisionesGDM.txt', header=0, delimiter=',', na_values='-99')
print(emis)

fig, ax = plt.subplots(1,1,figsize=(5, 3), sharey=True)

ax.bar(emis['anio'], emis['altgdm'], color='#A1140B')
ax.set_ylim(-800, 0)
ax.yaxis.set_tick_params(labelsize=16)
ax.xaxis.set_tick_params(labelsize=16, rotation=90)
ax.set_ylabel('10^3 CO$_2$e', fontsize=16)
ax.set_xticks([2025,2030,2035,2040,2045,2050], ['2025','2030','2035','2040','2045','2050'])
ax.set_title('Alt c/manejo', fontsize=16, fontweight='bold')
ax.set_xlim(2022.5, 2050.5)

# ~ ax2.bar(emis['anio'], emis['alt'], color='#A1140B')
# ~ ax2.set_ylim(-1000, 0)
# ~ ax2.yaxis.set_tick_params(labelsize=16)
# ~ ax2.xaxis.set_tick_params(labelsize=16, rotation=90)
# ~ ax2.set_xticks([2025,2030,2035,2040,2045,2050], ['2025','2030','2035','2040','2045','2050'])
# ~ ax2.set_title('Alt', fontsize=16, fontweight='bold')
# ~ ax2.set_xlim(2022.5, 2050.5)

# ~ fig.subplots_adjust(wspace=0.2)
# ~ plt.legend(bbox_to_anchor=(.02, .02), loc='upper left', borderaxespad=0.)
fig.subplots_adjust(hspace=0.1,wspace=0.05)

plt.savefig('emisionesGDM.svg', dpi=300, bbox_inches="tight")

