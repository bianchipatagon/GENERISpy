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
ALTGDM = pd.read_csv('/home/emi/Documents/GENERIS/GENERISpy/nodosALT-GD-M.txt', header=0, delimiter=';', na_values='-999',index_col='hora')

ALT = -ALT
ALTGD = -ALTGD
ALTGDM = -ALTGDM

RESTA1 = ALTGD-ALT
RESTA2 = ALTGDM-ALT

print(RESTA1)

fig, axs = plt.subplots(2,3,figsize=(16,6), sharey='row', sharex=True)

#################### ALT ###############################
################### 2030
axs[0,0].set_title('2030', fontsize = 16, weight = 'bold')
##positivos
axs[0,0].bar(ALT.index, ALT['impoC30'], color='#FBAA1B', alpha=0.8)
axs[0,0].bar(ALT.index, ALT['impoN30'], bottom=ALT['impoC30'], color='#207653', alpha=0.8)
axs[0,0].bar(ALT.index, ALT['impoO30'], bottom=ALT['impoC30']+ALT['impoN30'], color='#8FC73E', alpha=0.8)
axs[0,0].bar(ALT.index, ALT['impoS30'], bottom=ALT['impoC30']+ALT['impoN30']+ALT['impoO30'], color='#A1140B', alpha=0.8)
axs[0,0].set_ylim(0, 700)
axs[0,0].set_xticks(range(0, len(ALT.index), 2))
axs[0,0].set_xticklabels(ALT.index[::2])
axs[0,0].axvline(x=11.5, color='black', linewidth=1, linestyle='--', label='_nolegend_')
axs[0,0].axhline(linewidth=1, color='black', label='_nolegend_')
axs[0,0].xaxis.set_tick_params(labelsize=12, rotation=90)
axs[0,0].yaxis.set_tick_params(labelsize=12)


################### 2040
axs[0,1].set_title('importaciones \n 2040', fontsize = 16, weight = 'bold')
##positivos
axs[0,1].bar(ALT.index, ALT['impoC40'], color='#FBAA1B', alpha=0.8)
axs[0,1].bar(ALT.index, ALT['impoN40'], bottom=ALT['impoC40'], color='#207653', alpha=0.8)
axs[0,1].bar(ALT.index, ALT['impoO40'], bottom=ALT['impoC40']+ALT['impoN40'], color='#8FC73E', alpha=0.8)
axs[0,1].bar(ALT.index, ALT['impoS40'], bottom=ALT['impoC40']+ALT['impoN40']+ALT['impoO40'], color='#A1140B', alpha=0.8)
axs[0,1].set_ylim(0, 700)
axs[0,1].set_xticks(range(0, len(ALT.index), 2))
axs[0,1].set_xticklabels(ALT.index[::2])
axs[0,1].axvline(x=11.5, color='black', linewidth=1, linestyle='--', label='_nolegend_')
axs[0,1].axhline(linewidth=1, color='black', label='_nolegend_')
axs[0,1].xaxis.set_tick_params(labelsize=12, rotation=90)
# ~ axs[0,1].set_xlim(-0.5, 23.5)


################### 2050
axs[0,2].set_title('2050', fontsize = 16, weight = 'bold')

##positivos
axs[0,2].bar(ALT.index, ALT['impoC50'], color='#FBAA1B', alpha=0.8)
axs[0,2].bar(ALT.index, ALT['impoN50'], bottom=ALT['impoC50'], color='#207653', alpha=0.8)
axs[0,2].bar(ALT.index, ALT['impoO50'], bottom=ALT['impoC50']+ALT['impoN50'], color='#8FC73E', alpha=0.8)
axs[0,2].bar(ALT.index, ALT['impoS50'], bottom=ALT['impoC50']+ALT['impoN50']+ALT['impoO50'], color='#A1150B', alpha=0.8)
axs[0,2].set_ylim(0, 700)
axs[0,2].set_xticks(range(0, len(ALT.index), 2))
axs[0,2].set_xticklabels(ALT.index[::2])
axs[0,2].axvline(x=11.5, color='black', linewidth=1, linestyle='--', label='_nolegend_')
axs[0,2].axhline(linewidth=1, color='black', label='_nolegend_')
axs[0,2].xaxis.set_tick_params(labelsize=12, rotation=90)
axs[0,2].legend(["Centro", "Norte","Oriente","Sur"], frameon=False,bbox_to_anchor=(1.1, 0.5), loc='center left', borderaxespad=0.,fontsize=14)

# ~ axs[0,2].set_xlim(-0.5, 23.5)


#################### ALT-GD ###############################
################### 2030
# ~ axs[1,0].set_ylabel('[MW]', fontsize=14)
##positivos
cols = ['impoC30', 'impoN30', 'impoO30', 'impoS30']
colors = ['#FBAA1B', '#207653', '#8FC73E', '#A1150B']

# Separate positive and negative parts
pos_data = RESTA1[cols].clip(lower=0)  # keep only positive values
neg_data = RESTA1[cols].clip(upper=0)  # keep only negative values

pos_bottoms = N.zeros(len(RESTA1))
neg_bottoms = N.zeros(len(RESTA1))

for col, color in zip(cols, colors):
    # Plot positive part
    axs[1,0].bar(RESTA1.index, pos_data[col], bottom=pos_bottoms,
                 color=color, alpha=0.8)
    pos_bottoms += pos_data[col].values

    # Plot negative part
    axs[1,0].bar(RESTA1.index, neg_data[col], bottom=neg_bottoms,
                 color=color, alpha=0.8)
    neg_bottoms += neg_data[col].values

axs[1,0].set_ylim(-400,400)
axs[1,0].set_xticks(range(0, len(RESTA1.index), 2))
axs[1,0].set_xticklabels(RESTA1.index[::2])
axs[1,0].axvline(x=11.5, color='black', linewidth=1, linestyle='--', label='_nolegend_')
axs[1,0].axhline(linewidth=1, color='black', label='_nolegend_')
axs[1,0].xaxis.set_tick_params(labelsize=12, rotation=90)
axs[1,0].set_xlim(-0.5, 23.5)
axs[1,0].yaxis.set_tick_params(labelsize=12)

################### 2040
##positivos
cols = ['impoC40', 'impoN40', 'impoO40', 'impoS40']
colors = ['#FBAA1B', '#207653', '#8FC73E', '#A1150B']

# Separate positive and negative parts
pos_data = RESTA1[cols].clip(lower=0)  # keep only positive values
neg_data = RESTA1[cols].clip(upper=0)  # keep only negative values

pos_bottoms = N.zeros(len(RESTA1))
neg_bottoms = N.zeros(len(RESTA1))

for col, color in zip(cols, colors):
    # Plot positive part
    axs[1,1].bar(RESTA1.index, pos_data[col], bottom=pos_bottoms,
                 color=color, alpha=0.8)
    pos_bottoms += pos_data[col].values

    # Plot negative part
    axs[1,1].bar(RESTA1.index, neg_data[col], bottom=neg_bottoms,
                 color=color, alpha=0.8)
    neg_bottoms += neg_data[col].values

axs[1,1].set_ylim(-400,400)
axs[1,1].set_xticks(range(0, len(RESTA1.index), 2))
axs[1,1].set_xticklabels(RESTA1.index[::2])
axs[1,1].axvline(x=11.5, color='black', linewidth=1, linestyle='--', label='_nolegend_')
axs[1,1].axhline(linewidth=1, color='black', label='_nolegend_')
axs[1,1].xaxis.set_tick_params(labelsize=12, rotation=90)
axs[1,1].set_xlim(-0.5, 23.5)


################### 2050
##positivos

cols = ['impoC50', 'impoN50', 'impoO50', 'impoS50']
colors = ['#FBAA1B', '#207653', '#8FC73E', '#A1150B']

# Separate positive and negative parts
pos_data = RESTA1[cols].clip(lower=0)  # keep only positive values
neg_data = RESTA1[cols].clip(upper=0)  # keep only negative values

pos_bottoms = N.zeros(len(RESTA1))
neg_bottoms = N.zeros(len(RESTA1))

for col, color in zip(cols, colors):
    # Plot positive part
    axs[1,2].bar(RESTA1.index, pos_data[col], bottom=pos_bottoms,
                 color=color, alpha=0.8)
    pos_bottoms += pos_data[col].values

    # Plot negative part
    axs[1,2].bar(RESTA1.index, neg_data[col], bottom=neg_bottoms,
                 color=color, alpha=0.8)
    neg_bottoms += neg_data[col].values

axs[1,2].set_ylim(-400,400)
axs[1,2].set_xticks(range(0, len(RESTA1.index), 2))
axs[1,2].set_xticklabels(RESTA1.index[::2])
axs[1,2].axvline(x=11.5, color='black', linewidth=1, linestyle='--', label='_nolegend_')
axs[1,2].axhline(linewidth=1, color='black', label='_nolegend_')
axs[1,2].xaxis.set_tick_params(labelsize=12, rotation=90)
axs[1,2].set_xlim(-0.5, 23.5)

'''
#################### ALT-GD-M ###############################

################### 2030
##positivos
cols = ['impoC30', 'impoN30', 'impoO30', 'impoS30']
colors = ['#FBAA1B', '#207653', '#8FC73E', '#A1150B']

# Separate positive and negative parts
pos_data = RESTA2[cols].clip(lower=0)  # keep only positive values
neg_data = RESTA2[cols].clip(upper=0)  # keep only negative values

pos_bottoms = N.zeros(len(RESTA2))
neg_bottoms = N.zeros(len(RESTA2))

for col, color in zip(cols, colors):
    # Plot positive part
    axs[2,0].bar(RESTA2.index, pos_data[col], bottom=pos_bottoms,
                 color=color, alpha=0.8)
    pos_bottoms += pos_data[col].values

    # Plot negative part
    axs[2,0].bar(RESTA2.index, neg_data[col], bottom=neg_bottoms,
                 color=color, alpha=0.8)
    neg_bottoms += neg_data[col].values

axs[2,0].set_ylim(-400, 400)
axs[2,0].set_xticks(range(0, len(RESTA2.index), 2))
axs[2,0].set_xticklabels(RESTA2.index[::2])
axs[2,0].axvline(x=11.5, color='black', linewidth=1, linestyle='--', label='_nolegend_')
axs[2,0].axhline(linewidth=1, color='black', label='_nolegend_')
axs[2,0].xaxis.set_tick_params(labelsize=12, rotation=90)
axs[2,0].set_xlim(-0.5, 23.5)
axs[2,0].yaxis.set_tick_params(labelsize=12)


################### 2040
##positivos
cols = ['impoC40', 'impoN40', 'impoO40', 'impoS40']
colors = ['#FBAA1B', '#207653', '#8FC73E', '#A1150B']

# Separate positive and negative parts
pos_data = RESTA2[cols].clip(lower=0)  # keep only positive values
neg_data = RESTA2[cols].clip(upper=0)  # keep only negative values

pos_bottoms = N.zeros(len(RESTA2))
neg_bottoms = N.zeros(len(RESTA2))

for col, color in zip(cols, colors):
    # Plot positive part
    axs[2,1].bar(RESTA2.index, pos_data[col], bottom=pos_bottoms,
                 color=color, alpha=0.8)
    pos_bottoms += pos_data[col].values

    # Plot negative part
    axs[2,1].bar(RESTA2.index, neg_data[col], bottom=neg_bottoms,
                 color=color, alpha=0.8)
    neg_bottoms += neg_data[col].values

axs[2,1].set_xticks(range(0, len(RESTA2.index), 2))
axs[2,1].set_xticklabels(RESTA2.index[::2])
axs[2,1].axvline(x=11.5, color='black', linewidth=1, linestyle='--', label='_nolegend_')
axs[2,1].axhline(linewidth=1, color='black', label='_nolegend_')
axs[2,1].xaxis.set_tick_params(labelsize=12, rotation=90)
axs[2,1].set_xlim(-0.5, 23.5)
# ~ axs[2,1].legend(["Centro", "Norte","Oriente","Sur"], frameon=False,bbox_to_anchor=(1.05, 2), loc='upper left', borderaxespad=0.,fontsize=14)



################### 2050
##positivos
cols = ['impoC50', 'impoN50', 'impoO50', 'impoS50']
colors = ['#FBAA1B', '#207653', '#8FC73E', '#A1150B']

# Separate positive and negative parts
pos_data = RESTA2[cols].clip(lower=0)  # keep only positive values
neg_data = RESTA2[cols].clip(upper=0)  # keep only negative values

pos_bottoms = N.zeros(len(RESTA2))
neg_bottoms = N.zeros(len(RESTA2))

for col, color in zip(cols, colors):
    # Plot positive part
    axs[2,2].bar(RESTA2.index, pos_data[col], bottom=pos_bottoms,
                 color=color, alpha=0.8)
    pos_bottoms += pos_data[col].values

    # Plot negative part
    axs[2,2].bar(RESTA2.index, neg_data[col], bottom=neg_bottoms,
                 color=color, alpha=0.8)
    neg_bottoms += neg_data[col].values

axs[2,2].set_xticks(range(0, len(RESTA2.index), 2))
axs[2,2].set_xticklabels(RESTA2.index[::2])
axs[2,2].axvline(x=11.5, color='black', linewidth=1, linestyle='--', label='_nolegend_')
axs[2,2].axhline(linewidth=1, color='black', label='_nolegend_')
axs[2,2].xaxis.set_tick_params(labelsize=12, rotation=90)
axs[2,2].set_xlim(-0.5, 23.5)
'''


fig.subplots_adjust(wspace=0.1, hspace=0.1)
# ~ plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)
# ~ fig.text(.24, 0.97, 'Escenario Tendencial', va='center' ,fontsize=16, weight='bold')  
# ~ fig.text(.6, 0.97, 'Escenario Alternativo', va='center' ,fontsize=16, weight='bold')  
fig.text(0.91, 0.69, 'ALT', va='center' ,fontsize=16, weight='bold', rotation='vertical')  
fig.text(0.91, 0.3, 'ALTGD - ALT', va='center' ,fontsize=16, weight='bold', rotation='vertical')  
# ~ fig.text(0.91, 0.23, 'ALTGDM - ALT', va='center' ,fontsize=16, weight='bold', rotation='vertical')  
fig.text(0.08, 0.5, '[MW]', va='center' ,fontsize=14, rotation='vertical')  

plt.savefig('impoALT.jpg', dpi=300, bbox_inches="tight")
