import numpy as N
import matplotlib.pyplot as plt
from datetime import datetime
import pandas as pd
import seaborn as sns
from scipy.stats import spearmanr
from matplotlib.ticker import MultipleLocator
import matplotlib.patches as patches

ALTGDM = pd.read_csv('/home/emi/Documents/GENERIS/GENERISpy/nodosALT-GD-M.txt', header=0, delimiter=';', na_values='-999')

fig, axs = plt.subplots(3,3,figsize=(16,8),sharex=True, sharey=True)

#################### ALT-GD-M ###############################
axs[0,0].set_title('2030', fontsize = 16, weight = 'bold')
axs[0,0].set_ylim(-450, 450)

axs[0,1].set_title('2040', fontsize = 16, weight = 'bold')
axs[1,0].set_ylabel('[MW]', fontsize=14)

axs[0,2].set_title('2050', fontsize = 16, weight = 'bold')


#################### ALT-GD-M ###############################

################### 2030
NetoC30 = ALTGDM['expoC30']+ALTGDM['impoC30']
NetoN30 = ALTGDM['expoN30']+ALTGDM['impoN30']
NetoO30 = ALTGDM['expoO30']+ALTGDM['impoO30']
NetoS30 = ALTGDM['expoS30']+ALTGDM['impoS30']

##positivos
bars = axs[2,0].bar(ALTGDM['hora'], ALTGDM['expoC30'], color='#FBAA1B')
axs[2,0].bar_label(bars, label_type='center', color='white', fontsize=9, rotation='vertical')
axs[2,0].bar(ALTGDM['hora'], ALTGDM['expoN30'], bottom=ALTGDM['expoC30'], color='#207653')
axs[2,0].bar(ALTGDM['hora'], ALTGDM['expoO30'], bottom=ALTGDM['expoC30']+ALTGDM['expoN30'], color='#8FC73E')
axs[2,0].bar(ALTGDM['hora'], ALTGDM['expoS30'], bottom=ALTGDM['expoC30']+ALTGDM['expoN30']+ALTGDM['expoO30'], color='#A1140B')
axs[2,0].set_ylim(-700, 700)
axs[2,0].set_xticks(range(0, len(ALTGDM['hora']), 2))
axs[2,0].set_xticklabels(ALTGDM['hora'][::2])
axs[2,0].axvline(x=11.5, color='black', linewidth=1, linestyle='--', label='_nolegend_')
axs[2,0].axhline(linewidth=1, color='black', label='_nolegend_')
axs[2,0].xaxis.set_tick_params(labelsize=12, rotation=90)
axs[2,0].set_xlim(-0.5, 23.5)
axs[2,0].text(-5, -600,'Imports', rotation='vertical',fontsize = 14)
axs[2,0].text(-5, 100,'Exports', rotation='vertical',fontsize = 14)

##negativos
bars = axs[2,0].bar(ALTGDM['hora'], ALTGDM['impoC30'], color='#FBAA1B')
axs[2,0].bar_label(bars, label_type='center', color='white', fontsize=9, rotation='vertical')
axs[2,0].bar(ALTGDM['hora'], ALTGDM['impoN30'], bottom=ALTGDM['impoC30'], color='#207653')
axs[2,0].bar(ALTGDM['hora'], ALTGDM['impoO30'], bottom=ALTGDM['impoC30']+ALTGDM['impoN30'], color='#8FC73E')
axs[2,0].bar(ALTGDM['hora'], ALTGDM['impoS30'], bottom=ALTGDM['impoC30']+ALTGDM['impoN30']+ALTGDM['impoO30'], color='#A1140B')

################### 2040
##positivos
axs[2,1].bar(ALTGDM['hora'], ALTGDM['expoC40'], color='#FBAA1B')
axs[2,1].bar(ALTGDM['hora'], ALTGDM['expoN40'], bottom=ALTGDM['expoC40'], color='#207653')
axs[2,1].bar(ALTGDM['hora'], ALTGDM['expoO40'], bottom=ALTGDM['expoC40']+ALTGDM['expoN40'], color='#8FC73E')
axs[2,1].bar(ALTGDM['hora'], ALTGDM['expoS40'], bottom=ALTGDM['expoC40']+ALTGDM['expoN40']+ALTGDM['expoO40'], color='#A1140B')
axs[2,1].set_xticks(range(0, len(ALTGDM['hora']), 2))
axs[2,1].set_xticklabels(ALTGDM['hora'][::2])
axs[2,1].axvline(x=11.5, color='black', linewidth=1, linestyle='--', label='_nolegend_')
axs[2,1].axhline(linewidth=1, color='black', label='_nolegend_')
axs[2,1].xaxis.set_tick_params(labelsize=12, rotation=90)
axs[2,1].set_xlim(-0.5, 23.5)
# ~ axs[2,1].legend(["Centro", "Norte","Oriente","Sur"], frameon=False,bbox_to_anchor=(1.05, 2), loc='upper left', borderaxespad=0.,fontsize=14)

##negativos
axs[2,1].bar(ALTGDM['hora'], ALTGDM['impoC40'], color='#FBAA1B')
axs[2,1].bar(ALTGDM['hora'], ALTGDM['impoN40'], bottom=ALTGDM['impoC40'], color='#207653')
axs[2,1].bar(ALTGDM['hora'], ALTGDM['impoO40'], bottom=ALTGDM['impoC40']+ALTGDM['impoN40'], color='#8FC73E')
axs[2,1].bar(ALTGDM['hora'], ALTGDM['impoS40'], bottom=ALTGDM['impoC40']+ALTGDM['impoN40']+ALTGDM['impoO40'], color='#A1140B')

################### 2050
##positivos
axs[2,2].bar(ALTGDM['hora'], ALTGDM['expoC50'], color='#FBAA1B')
axs[2,2].bar(ALTGDM['hora'], ALTGDM['expoN50'], bottom=ALTGDM['expoC50'], color='#207653')
axs[2,2].bar(ALTGDM['hora'], ALTGDM['expoO50'], bottom=ALTGDM['expoC50']+ALTGDM['expoN50'], color='#8FC73E')
axs[2,2].bar(ALTGDM['hora'], ALTGDM['expoS50'], bottom=ALTGDM['expoC50']+ALTGDM['expoN50']+ALTGDM['expoO50'], color='#A1150B')
axs[2,2].set_xticks(range(0, len(ALTGDM['hora']), 2))
axs[2,2].set_xticklabels(ALTGDM['hora'][::2])
axs[2,2].axvline(x=11.5, color='black', linewidth=1, linestyle='--', label='_nolegend_')
axs[2,2].axhline(linewidth=1, color='black', label='_nolegend_')
axs[2,2].xaxis.set_tick_params(labelsize=12, rotation=90)
axs[2,2].set_xlim(-0.5, 23.5)
axs[2,2].legend(["Centro", "Norte","Oriente","Sur"], frameon=False,bbox_to_anchor=(1.1, 2), loc='upper left', borderaxespad=0.,fontsize=14)

##negativos
axs[2,2].bar(ALTGDM['hora'], ALTGDM['impoC50'], color='#FBAA1B')
axs[2,2].bar(ALTGDM['hora'], ALTGDM['impoN50'], bottom=ALTGDM['impoC50'], color='#207653')
axs[2,2].bar(ALTGDM['hora'], ALTGDM['impoO50'], bottom=ALTGDM['impoC50']+ALTGDM['impoN50'], color='#8FC73E')
axs[2,2].bar(ALTGDM['hora'], ALTGDM['impoS50'], bottom=ALTGDM['impoC50']+ALTGDM['impoN50']+ALTGDM['impoO50'], color='#A1150B')

fig.subplots_adjust(wspace=0.1, hspace=0.1)
# ~ plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)
# ~ fig.text(.24, 0.97, 'Escenario Tendencial', va='center' ,fontsize=16, weight='bold')  
# ~ fig.text(.6, 0.97, 'Escenario Alternativo', va='center' ,fontsize=16, weight='bold')  
fig.text(0.91, 0.75, 'ALT', va='center' ,fontsize=16, weight='bold', rotation='vertical')  
fig.text(0.91, 0.49, 'ALT-GD', va='center' ,fontsize=16, weight='bold', rotation='vertical')  
fig.text(0.91, 0.23, 'ALT-GD-M', va='center' ,fontsize=16, weight='bold', rotation='vertical')  

plt.savefig('transmision.jpg', dpi=300, bbox_inches="tight")
