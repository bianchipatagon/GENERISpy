import numpy as N
import matplotlib.pyplot as plt
from datetime import datetime
import pandas as pd
import seaborn as sns
from scipy.stats import spearmanr
from matplotlib.ticker import MultipleLocator
import matplotlib.patches as patches
from labellines import labelLine, labelLines

porc = pd.read_csv('/home/emi/Documents/GENERIS/GENERISpy/porcentaje.txt', header=0, delimiter=',', na_values='-999')



fig, ax = plt.subplots(1,1,figsize=(4,2),sharex=True, sharey=True)

# ~ axs[0].set_title('Estación seca \n (nov-abr)', fontsize = 14)
ax.scatter(porc['capacidad'],porc['alt'],color='#A1150B',marker = 'D',s=60,label='alternativo')
# ~ ax.scatter(porc['capacidad'],porc['altMH'],color='#207653',marker = 'D',label='alternativo')
ax.scatter(porc['capacidad'],porc['tend'],color='#6D6F70',marker = 'D',s=60,label='tendencial')
ax.legend(bbox_to_anchor=(1.05, 0.5), loc=2, borderaxespad=0., fontsize=12).get_frame().set_edgecolor("white")

# ~ ax[0].plot(fu_dry['hora'],fu_dry['hidaj'],color='#207653',linewidth=2.5,label='propuesta')
ax.xaxis.set_tick_params(labelsize=12)
ax.yaxis.set_tick_params(labelsize=12)
labelLines(ax.get_lines(), zorder=2.5)
ax.set_ylabel('% vertido \n renovables', fontsize=14)
ax.set_xlim(100, 1100)
ax.set_ylim(0, 20)
ax.set_xticks([250,500,750,1000], ['250','500','750','1000'])

ax.set_xlabel('capacidad [MW]', fontsize=14)


fig.subplots_adjust(wspace=0.1)
plt.savefig('porc.svg', dpi=300, bbox_inches="tight")
