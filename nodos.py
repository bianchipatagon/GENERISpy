import numpy as N
import matplotlib.pyplot as plt
from datetime import datetime
import pandas as pd
import seaborn as sns
from scipy.stats import spearmanr
from matplotlib.ticker import MultipleLocator
import matplotlib.patches as patches

ALT = pd.read_csv('/home/emi/Documents/GENERIS/GENERISpy/nodosALT.txt', header=0, delimiter=';', na_values='-999',index_col='hora')
ALTGD = pd.read_csv('/home/emi/Documents/GENERIS/GENERISpy/nodosALT-GD.txt', header=0, delimiter=';', na_values='-999',index_col='hora')
# ~ ALTGDM = pd.read_csv('/home/emi/Documents/GENERIS/GENERISpy/nodosALT-GD-M.txt', header=0, delimiter=';', na_values='-999',index_col='hora')
ALTGDM = pd.read_csv('/home/emi/Documents/GENERIS/GENERISpy/nodosALT-GD-M-2.txt', header=0, delimiter=';', na_values='-999',index_col='hora')

print(ALT)

# ~ ALT = pd.DataFrame(N.array(ALT).reshape(6, 4, -1).mean(axis=1),columns=ALT.columns)
# ~ print(ALT)

# ~ fig, axs = plt.subplots(3,3,figsize=(16,8),sharex=True, sharey=True)
fig, axs = plt.subplots(3,3,figsize=(16,8), sharex=True)

#################### ALT ###############################
################### 2030
NetoC30 = ALT['expoC30']+ALT['impoC30']
axs[0,0].set_title('2030', fontsize = 16, weight = 'bold')
##positivos
axs[0,0].plot(ALT.index, NetoC30, color='darkorange', linewidth=2)
axs[0,0].bar(ALT.index, ALT['expoC30'], color='#FBAA1B', alpha=0.8)
axs[0,0].bar(ALT.index, ALT['expoN30'], bottom=ALT['expoC30'], color='#207653', alpha=0.8)
axs[0,0].bar(ALT.index, ALT['expoO30'], bottom=ALT['expoC30']+ALT['expoN30'], color='#8FC73E', alpha=0.8)
axs[0,0].bar(ALT.index, ALT['expoS30'], bottom=ALT['expoC30']+ALT['expoN30']+ALT['expoO30'], color='#A1140B', alpha=0.7)
axs[0,0].set_ylim(-700, 700)
axs[0,0].set_xticks(range(0, len(ALT.index), 2))
axs[0,0].set_xticklabels(ALT.index[::2])
# ~ axs[0,0].axvline(x=11.5, color='black', linewidth=1, linestyle='--', label='_nolegend_')
axs[0,0].axhline(linewidth=1, color='black', label='_nolegend_')
axs[0,0].xaxis.set_tick_params(labelsize=12, rotation=90)
# ~ axs[0,0].set_xlim(-0.5, 23.5)
axs[0,0].text(-5, -600,'Imports', rotation='vertical',fontsize = 14)
axs[0,0].text(-5, 100,'Exports', rotation='vertical',fontsize = 14)

##negativos
axs[0,0].bar(ALT.index, ALT['impoC30'], color='#FBAA1B', alpha=0.8)
axs[0,0].bar(ALT.index, ALT['impoN30'], bottom=ALT['impoC30'], color='#207653', alpha=0.8)
axs[0,0].bar(ALT.index, ALT['impoO30'], bottom=ALT['impoC30']+ALT['impoN30'], color='#8FC73E', alpha=0.8)
axs[0,0].bar(ALT.index, ALT['impoS30'], bottom=ALT['impoC30']+ALT['impoN30']+ALT['impoO30'], color='#A1140B', alpha=0.7)

################### 2040
NetoC40 = ALT['expoC40']+ALT['impoC40']
axs[0,1].set_title('2040', fontsize = 16, weight = 'bold')
##positivos
axs[0,1].plot(ALT.index, NetoC40, color='darkorange', linewidth=2)
axs[0,1].bar(ALT.index, ALT['expoC40'], color='#FBAA1B', alpha=0.8)
axs[0,1].bar(ALT.index, ALT['expoN40'], bottom=ALT['expoC40'], color='#207653', alpha=0.8)
axs[0,1].bar(ALT.index, ALT['expoO40'], bottom=ALT['expoC40']+ALT['expoN40'], color='#8FC73E', alpha=0.8)
axs[0,1].bar(ALT.index, ALT['expoS40'], bottom=ALT['expoC40']+ALT['expoN40']+ALT['expoO40'], color='#A1140B', alpha=0.7)
axs[0,1].set_ylim(-700, 700)
axs[0,1].set_xticks(range(0, len(ALT.index), 2))
axs[0,1].set_xticklabels(ALT.index[::2])
# ~ axs[0,1].axvline(x=11.5, color='black', linewidth=1, linestyle='--', label='_nolegend_')
axs[0,1].axhline(linewidth=1, color='black', label='_nolegend_')
axs[0,1].xaxis.set_tick_params(labelsize=12, rotation=90)
# ~ axs[0,1].set_xlim(-0.5, 23.5)


##negativos
axs[0,1].bar(ALT.index, ALT['impoC40'], color='#FBAA1B', alpha=0.8)
axs[0,1].bar(ALT.index, ALT['impoN40'], bottom=ALT['impoC40'], color='#207653', alpha=0.8)
axs[0,1].bar(ALT.index, ALT['impoO40'], bottom=ALT['impoC40']+ALT['impoN40'], color='#8FC73E', alpha=0.8)
axs[0,1].bar(ALT.index, ALT['impoS40'], bottom=ALT['impoC40']+ALT['impoN40']+ALT['impoO40'], color='#A1140B', alpha=0.7)

################### 2050
NetoC50 = ALT['expoC50']+ALT['impoC50']
axs[0,2].set_title('2050', fontsize = 16, weight = 'bold')

##positivos
axs[0,2].plot(ALT.index, NetoC50, color='darkorange', linewidth=2)
axs[0,2].bar(ALT.index, ALT['expoC50'], color='#FBAA1B', alpha=0.8)
axs[0,2].bar(ALT.index, ALT['expoN50'], bottom=ALT['expoC50'], color='#207653', alpha=0.8)
axs[0,2].bar(ALT.index, ALT['expoO50'], bottom=ALT['expoC50']+ALT['expoN50'], color='#8FC73E', alpha=0.8)
axs[0,2].bar(ALT.index, ALT['expoS50'], bottom=ALT['expoC50']+ALT['expoN50']+ALT['expoO50'], color='#A1150B', alpha=0.7)
axs[0,2].set_ylim(-700, 700)
axs[0,2].set_xticks(range(0, len(ALT.index), 2))
axs[0,2].set_xticklabels(ALT.index[::2])
# ~ axs[0,2].axvline(x=11.5, color='black', linewidth=1, linestyle='--', label='_nolegend_')
axs[0,2].axhline(linewidth=1, color='black', label='_nolegend_')
axs[0,2].xaxis.set_tick_params(labelsize=12, rotation=90)
# ~ axs[0,2].set_xlim(-0.5, 23.5)


##negativos
axs[0,2].bar(ALT.index, ALT['impoC50'], color='#FBAA1B', alpha=0.8)
axs[0,2].bar(ALT.index, ALT['impoN50'], bottom=ALT['impoC50'], color='#207653', alpha=0.8)
axs[0,2].bar(ALT.index, ALT['impoO50'], bottom=ALT['impoC50']+ALT['impoN50'], color='#8FC73E', alpha=0.8)
axs[0,2].bar(ALT.index, ALT['impoS50'], bottom=ALT['impoC50']+ALT['impoN50']+ALT['impoO50'], color='#A1150B', alpha=0.7)

#################### ALT-GD ###############################
################### 2030
NetoC30 = ALTGD['expoC30']+ALTGD['impoC30']
axs[1,0].set_ylabel('[MW]', fontsize=14,labelpad=20)
##positivos
axs[1,0].plot(ALTGD.index, NetoC30, color='darkorange', linewidth=2)
axs[1,0].bar(ALTGD.index, ALTGD['expoC30'], color='#FBAA1B', alpha=0.8)
axs[1,0].bar(ALTGD.index, ALTGD['expoN30'], bottom=ALTGD['expoC30'], color='#207653', alpha=0.8)
axs[1,0].bar(ALTGD.index, ALTGD['expoO30'], bottom=ALTGD['expoC30']+ALTGD['expoN30'], color='#8FC73E', alpha=0.8)
axs[1,0].bar(ALTGD.index, ALTGD['expoS30'], bottom=ALTGD['expoC30']+ALTGD['expoN30']+ALTGD['expoO30'], color='#A1140B', alpha=0.7)
axs[1,0].set_ylim(-700, 700)
axs[1,0].set_xticks(range(0, len(ALTGD.index), 2))
axs[1,0].set_xticklabels(ALTGD.index[::2])
axs[1,0].axvline(x=11.5, color='black', linewidth=1, linestyle='--', label='_nolegend_')
axs[1,0].axhline(linewidth=1, color='black', label='_nolegend_')
axs[1,0].xaxis.set_tick_params(labelsize=12, rotation=90)
axs[1,0].set_xlim(-0.5, 23.5)
axs[1,0].text(-5, -600,'Imports', rotation='vertical',fontsize = 14)
axs[1,0].text(-5, 100,'Exports', rotation='vertical',fontsize = 14)

##negativos
axs[1,0].bar(ALTGD.index, ALTGD['impoC30'], color='#FBAA1B', alpha=0.8)
axs[1,0].bar(ALTGD.index, ALTGD['impoN30'], bottom=ALTGD['impoC30'], color='#207653', alpha=0.8)
axs[1,0].bar(ALTGD.index, ALTGD['impoO30'], bottom=ALTGD['impoC30']+ALTGD['impoN30'], color='#8FC73E', alpha=0.8)
axs[1,0].bar(ALTGD.index, ALTGD['impoS30'], bottom=ALTGD['impoC30']+ALTGD['impoN30']+ALTGD['impoO30'], color='#A1140B', alpha=0.7)

################### 2040
NetoC40 = ALTGD['expoC40']+ALTGD['impoC40']
##positivos
axs[1,1].plot(ALTGD.index, NetoC40, color='darkorange', linewidth=2)
axs[1,1].bar(ALTGD.index, ALTGD['expoC40'], color='#FBAA1B', alpha=0.8)
axs[1,1].bar(ALTGD.index, ALTGD['expoN40'], bottom=ALTGD['expoC40'], color='#207653', alpha=0.8)
axs[1,1].bar(ALTGD.index, ALTGD['expoO40'], bottom=ALTGD['expoC40']+ALTGD['expoN40'], color='#8FC73E', alpha=0.8)
axs[1,1].bar(ALTGD.index, ALTGD['expoS40'], bottom=ALTGD['expoC40']+ALTGD['expoN40']+ALTGD['expoO40'], color='#A1140B', alpha=0.7)
axs[1,1].set_ylim(-700, 700)
axs[1,1].set_xticks(range(0, len(ALTGD.index), 2))
axs[1,1].set_xticklabels(ALTGD.index[::2])
axs[1,1].axvline(x=11.5, color='black', linewidth=1, linestyle='--', label='_nolegend_')
axs[1,1].axhline(linewidth=1, color='black', label='_nolegend_')
axs[1,1].xaxis.set_tick_params(labelsize=12, rotation=90)
axs[1,1].set_xlim(-0.5, 23.5)


##negativos
axs[1,1].bar(ALTGD.index, ALTGD['impoC40'], color='#FBAA1B', alpha=0.8)
axs[1,1].bar(ALTGD.index, ALTGD['impoN40'], bottom=ALTGD['impoC40'], color='#207653', alpha=0.8)
axs[1,1].bar(ALTGD.index, ALTGD['impoO40'], bottom=ALTGD['impoC40']+ALTGD['impoN40'], color='#8FC73E', alpha=0.8)
axs[1,1].bar(ALTGD.index, ALTGD['impoS40'], bottom=ALTGD['impoC40']+ALTGD['impoN40']+ALTGD['impoO40'], color='#A1140B', alpha=0.7)

################### 2050
NetoC50 = ALTGD['expoC50']+ALTGD['impoC50']
##positivos
axs[1,2].plot(ALTGD.index, NetoC50, color='darkorange', linewidth=2)
axs[1,2].bar(ALTGD.index, ALTGD['expoC50'], color='#FBAA1B', alpha=0.8)
axs[1,2].bar(ALTGD.index, ALTGD['expoN50'], bottom=ALTGD['expoC50'], color='#207653', alpha=0.8)
axs[1,2].bar(ALTGD.index, ALTGD['expoO50'], bottom=ALTGD['expoC50']+ALTGD['expoN50'], color='#8FC73E', alpha=0.8)
axs[1,2].bar(ALTGD.index, ALTGD['expoS50'], bottom=ALTGD['expoC50']+ALTGD['expoN50']+ALTGD['expoO50'], color='#A1150B', alpha=0.7)
axs[1,2].set_ylim(-700, 700)
axs[1,2].set_xticks(range(0, len(ALTGD.index), 2))
axs[1,2].set_xticklabels(ALTGD.index[::2])
axs[1,2].axvline(x=11.5, color='black', linewidth=1, linestyle='--', label='_nolegend_')
axs[1,2].axhline(linewidth=1, color='black', label='_nolegend_')
axs[1,2].xaxis.set_tick_params(labelsize=12, rotation=90)
axs[1,2].set_xlim(-0.5, 23.5)


##negativos
axs[1,2].bar(ALTGD.index, ALTGD['impoC50'], color='#FBAA1B', alpha=0.8)
axs[1,2].bar(ALTGD.index, ALTGD['impoN50'], bottom=ALTGD['impoC50'], color='#207653', alpha=0.8)
axs[1,2].bar(ALTGD.index, ALTGD['impoO50'], bottom=ALTGD['impoC50']+ALTGD['impoN50'], color='#8FC73E', alpha=0.8)
axs[1,2].bar(ALTGD.index, ALTGD['impoS50'], bottom=ALTGD['impoC50']+ALTGD['impoN50']+ALTGD['impoO50'], color='#A1150B', alpha=0.7)

#################### ALT-GD-M ###############################

################### 2030
NetoC30 = ALTGDM['expoC30']+ALTGDM['impoC30']
##positivos
axs[2,0].plot(ALTGDM.index, NetoC30, color='darkorange', linewidth=2)
axs[2,0].bar(ALTGDM.index, ALTGDM['expoC30'], color='#FBAA1B', alpha=0.8)
axs[2,0].bar(ALTGDM.index, ALTGDM['expoN30'], bottom=ALTGDM['expoC30'], color='#207653', alpha=0.8)
axs[2,0].bar(ALTGDM.index, ALTGDM['expoO30'], bottom=ALTGDM['expoC30']+ALTGDM['expoN30'], color='#8FC73E', alpha=0.8)
axs[2,0].bar(ALTGDM.index, ALTGDM['expoS30'], bottom=ALTGDM['expoC30']+ALTGDM['expoN30']+ALTGDM['expoO30'], color='#A1140B', alpha=0.7)
axs[2,0].set_ylim(-700, 700)
axs[2,0].set_xticks(range(0, len(ALTGDM.index), 2))
axs[2,0].set_xticklabels(ALTGDM.index[::2])
axs[2,0].axvline(x=11.5, color='black', linewidth=1, linestyle='--', label='_nolegend_')
axs[2,0].axhline(linewidth=1, color='black', label='_nolegend_')
axs[2,0].xaxis.set_tick_params(labelsize=12, rotation=90)
axs[2,0].set_xlim(-0.5, 23.5)
axs[2,0].text(-5, -600,'Imports', rotation='vertical',fontsize = 14)
axs[2,0].text(-5, 100,'Exports', rotation='vertical',fontsize = 14)

##negativos
axs[2,0].bar(ALTGDM.index, ALTGDM['impoC30'], color='#FBAA1B', alpha=0.8)
axs[2,0].bar(ALTGDM.index, ALTGDM['impoN30'], bottom=ALTGDM['impoC30'], color='#207653', alpha=0.8)
axs[2,0].bar(ALTGDM.index, ALTGDM['impoO30'], bottom=ALTGDM['impoC30']+ALTGDM['impoN30'], color='#8FC73E', alpha=0.8)
axs[2,0].bar(ALTGDM.index, ALTGDM['impoS30'], bottom=ALTGDM['impoC30']+ALTGDM['impoN30']+ALTGDM['impoO30'], color='#A1140B', alpha=0.7)

################### 2040
NetoC40 = ALTGDM['expoC40']+ALTGDM['impoC40']
##positivos
axs[2,1].plot(ALTGDM.index, NetoC40, color='darkorange', linewidth=2)
axs[2,1].bar(ALTGDM.index, ALTGDM['expoC40'], color='#FBAA1B', alpha=0.8)
axs[2,1].bar(ALTGDM.index, ALTGDM['expoN40'], bottom=ALTGDM['expoC40'], color='#207653', alpha=0.8)
axs[2,1].bar(ALTGDM.index, ALTGDM['expoO40'], bottom=ALTGDM['expoC40']+ALTGDM['expoN40'], color='#8FC73E', alpha=0.8)
axs[2,1].bar(ALTGDM.index, ALTGDM['expoS40'], bottom=ALTGDM['expoC40']+ALTGDM['expoN40']+ALTGDM['expoO40'], color='#A1140B', alpha=0.7)
axs[2,1].set_xticks(range(0, len(ALTGDM.index), 2))
axs[2,1].set_xticklabels(ALTGDM.index[::2])
axs[2,1].axvline(x=11.5, color='black', linewidth=1, linestyle='--', label='_nolegend_')
axs[2,1].axhline(linewidth=1, color='black', label='_nolegend_')
axs[2,1].xaxis.set_tick_params(labelsize=12, rotation=90)
axs[2,1].set_xlim(-0.5, 23.5)
# ~ axs[2,1].legend(["Centro", "Norte","Oriente","Sur"], frameon=False,bbox_to_anchor=(1.05, 2), loc='upper left', borderaxespad=0.,fontsize=14)

##negativos
axs[2,1].bar(ALTGDM.index, ALTGDM['impoC40'], color='#FBAA1B', alpha=0.8)
axs[2,1].bar(ALTGDM.index, ALTGDM['impoN40'], bottom=ALTGDM['impoC40'], color='#207653', alpha=0.8)
axs[2,1].bar(ALTGDM.index, ALTGDM['impoO40'], bottom=ALTGDM['impoC40']+ALTGDM['impoN40'], color='#8FC73E', alpha=0.8)
axs[2,1].bar(ALTGDM.index, ALTGDM['impoS40'], bottom=ALTGDM['impoC40']+ALTGDM['impoN40']+ALTGDM['impoO40'], color='#A1140B', alpha=0.7)

################### 2050
NetoC50 = ALTGDM['expoC50']+ALTGDM['impoC50']
##positivos
axs[2,2].plot(ALTGDM.index, NetoC50, color='darkorange', linewidth=2)
axs[2,2].bar(ALTGDM.index, ALTGDM['expoC50'], color='#FBAA1B', alpha=0.8)
axs[2,2].bar(ALTGDM.index, ALTGDM['expoN50'], bottom=ALTGDM['expoC50'], color='#207653', alpha=0.8)
axs[2,2].bar(ALTGDM.index, ALTGDM['expoO50'], bottom=ALTGDM['expoC50']+ALTGDM['expoN50'], color='#8FC73E', alpha=0.8)
axs[2,2].bar(ALTGDM.index, ALTGDM['expoS50'], bottom=ALTGDM['expoC50']+ALTGDM['expoN50']+ALTGDM['expoO50'], color='#A1150B', alpha=0.7)
axs[2,2].set_xticks(range(0, len(ALTGDM.index), 2))
axs[2,2].set_xticklabels(ALTGDM.index[::2])
axs[2,2].axvline(x=11.5, color='black', linewidth=1, linestyle='--', label='_nolegend_')
axs[2,2].axhline(linewidth=1, color='black', label='_nolegend_')
axs[2,2].xaxis.set_tick_params(labelsize=12, rotation=90)
axs[2,2].set_xlim(-0.5, 23.5)
axs[2,2].legend(["Neto Centro", "Centro", "Norte","Oriente","Sur"], frameon=False,bbox_to_anchor=(1.1, 2), loc='upper left', borderaxespad=0.,fontsize=14)

##negativos
axs[2,2].bar(ALTGDM.index, ALTGDM['impoC50'], color='#FBAA1B', alpha=0.8)
axs[2,2].bar(ALTGDM.index, ALTGDM['impoN50'], bottom=ALTGDM['impoC50'], color='#207653', alpha=0.8)
axs[2,2].bar(ALTGDM.index, ALTGDM['impoO50'], bottom=ALTGDM['impoC50']+ALTGDM['impoN50'], color='#8FC73E', alpha=0.8)
axs[2,2].bar(ALTGDM.index, ALTGDM['impoS50'], bottom=ALTGDM['impoC50']+ALTGDM['impoN50']+ALTGDM['impoO50'], color='#A1150B', alpha=0.7)

fig.subplots_adjust(wspace=0.1, hspace=0.1)
# ~ plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)
# ~ fig.text(.24, 0.97, 'Escenario Tendencial', va='center' ,fontsize=16, weight='bold')  
# ~ fig.text(.6, 0.97, 'Escenario Alternativo', va='center' ,fontsize=16, weight='bold')  
fig.text(0.91, 0.75, 'ALT', va='center' ,fontsize=16, weight='bold', rotation='vertical')  
fig.text(0.91, 0.49, 'ALT-GD', va='center' ,fontsize=16, weight='bold', rotation='vertical')  
fig.text(0.91, 0.23, 'ALT-GD-M', va='center' ,fontsize=16, weight='bold', rotation='vertical')  

plt.savefig('transmision2.jpg', dpi=300, bbox_inches="tight")
