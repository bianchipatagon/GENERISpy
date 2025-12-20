import numpy as N
import matplotlib.pyplot as plt
from datetime import datetime
import pandas as pd
import seaborn as sns
from scipy.stats import spearmanr
from matplotlib.ticker import MultipleLocator

emis = pd.read_csv('/home/emi/Documents/GENERIS/GENERISpy/ahorro.txt', header=0, delimiter=',', na_values='-99')
print(emis)

fig, (ax1,ax2) = plt.subplots(1,2,figsize=(9, 3), sharey=True)

ax1.bar(emis['año'], emis['tend'], color='#A1140B')
ax1.set_ylim(-1000, 0)
ax1.yaxis.set_tick_params(labelsize=16)
ax1.xaxis.set_tick_params(labelsize=16, rotation=90)
ax1.set_ylabel('10^3 BEP', fontsize=16)
ax1.set_xticks([2025,2030,2035,2040,2045,2050], ['2025','2030','2035','2040','2045','2050'])
ax1.set_title('Escenario Tendencial', fontsize=16, fontweight='bold')

ax2.bar(emis['año'], emis['alt'], color='#A1140B')
ax2.set_ylim(-1000, 0)
ax2.yaxis.set_tick_params(labelsize=16)
ax2.xaxis.set_tick_params(labelsize=16, rotation=90)
ax2.set_xticks([2025,2030,2035,2040,2045,2050], ['2025','2030','2035','2040','2045','2050'])
ax2.set_title('Escenario Alternativo', fontsize=16, fontweight='bold')

# ~ fig.subplots_adjust(wspace=0.2)
# ~ plt.legend(bbox_to_anchor=(.02, .02), loc='upper left', borderaxespad=0.)
fig.subplots_adjust(hspace=0.1,wspace=0.05)

plt.savefig('ahorro.svg', dpi=300, bbox_inches="tight")

