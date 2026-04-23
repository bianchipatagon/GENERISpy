import numpy as N
import matplotlib.pyplot as plt
from datetime import datetime
import pandas as pd
import seaborn as sns
from scipy.stats import spearmanr
from matplotlib.ticker import MultipleLocator
import matplotlib.patches as patches

ALT = pd.read_csv('/home/emi/Documents/GENERIS/GENERISpy/inputALT.txt', header=0, delimiter=';', na_values='-999',index_col='anio')
ALTGD = pd.read_csv('/home/emi/Documents/GENERIS/GENERISpy/inputALTGD.txt', header=0, delimiter=';', na_values='-999',index_col='anio')
ALTGDM = pd.read_csv('/home/emi/Documents/GENERIS/GENERISpy/inputALTGDM.txt', header=0, delimiter=';', na_values='-999',index_col='anio')

print(ALT)
fig, axs = plt.subplots(1,4,figsize=(16,3), sharey='row', sharex=True)
'''
#################### ALT ###############################
################### NORTE
axs[0,0].set_title('Norte', fontsize = 16, weight = 'bold')
axs[0,0].bar(ALT.index, ALT['FosilN'], color='#A1140B', alpha=0.8)
axs[0,0].bar(ALT.index, ALT['HidroN'], bottom=ALT['FosilN'], color='#207653', alpha=0.8)
axs[0,0].bar(ALT.index, ALT['SolarN'], bottom=ALT['FosilN']+ALT['HidroN'], color='#FBAA1B', alpha=0.8)
axs[0,0].bar(ALT.index, ALT['EolicoN'], bottom=ALT['FosilN']+ALT['HidroN']+ALT['SolarN'], color='#8FC73E', alpha=0.8)
axs[0,0].xaxis.set_tick_params(labelsize=12, rotation=90)
axs[0,0].set_xlim(2022.5, 2050.5)
axs[0,0].yaxis.set_tick_params(labelsize=12)

################### CENTRO
axs[0,1].set_title('Centro', fontsize = 16, weight = 'bold')
axs[0,1].bar(ALT.index, ALT['FosilC'], color='#A1140B', alpha=0.8)
axs[0,1].bar(ALT.index, ALT['HidroC'], bottom=ALT['FosilC'], color='#207653', alpha=0.8)
axs[0,1].bar(ALT.index, ALT['SolarC'], bottom=ALT['FosilC']+ALT['HidroC'], color='#FBAA1B', alpha=0.8)
axs[0,1].bar(ALT.index, ALT['EolicoC'], bottom=ALT['FosilC']+ALT['HidroC']+ALT['SolarC'], color='#8FC73E', alpha=0.8)
axs[0,1].xaxis.set_tick_params(labelsize=12, rotation=90)
axs[0,1].set_xlim(2022.5, 2050.5)

################### ORIENTE
axs[0,2].set_title('Oriente', fontsize = 16, weight = 'bold')
axs[0,2].bar(ALT.index, ALT['FosilO'], color='#A1140B', alpha=0.8)
axs[0,2].bar(ALT.index, ALT['HidroO'], bottom=ALT['FosilO'], color='#207653', alpha=0.8)
axs[0,2].bar(ALT.index, ALT['SolarO'], bottom=ALT['FosilO']+ALT['HidroO'], color='#FBAA1B', alpha=0.8)
axs[0,2].bar(ALT.index, ALT['EolicoO'], bottom=ALT['FosilO']+ALT['HidroO']+ALT['SolarO'], color='#8FC73E', alpha=0.8)
axs[0,2].xaxis.set_tick_params(labelsize=12, rotation=90)
axs[0,2].set_xlim(2022.5, 2050.5)

################### SUR
axs[0,3].set_title('Sur', fontsize = 16, weight = 'bold')
axs[0,3].bar(ALT.index, ALT['FosilS'], color='#A1140B', alpha=0.8)
axs[0,3].bar(ALT.index, ALT['HidroS'], bottom=ALT['FosilS'], color='#207653', alpha=0.8)
axs[0,3].bar(ALT.index, ALT['SolarS'], bottom=ALT['FosilS']+ALT['HidroS'], color='#FBAA1B', alpha=0.8)
axs[0,3].bar(ALT.index, ALT['EolicoS'], bottom=ALT['FosilS']+ALT['HidroS']+ALT['SolarS'], color='#8FC73E', alpha=0.8)
axs[0,3].xaxis.set_tick_params(labelsize=12, rotation=90)
axs[0,3].set_xlim(2022.5, 2050.5)
axs[0,3].legend(["Fósil", "Hidro","Solar","Eólica"], frameon=False,bbox_to_anchor=(1.2, 0.5), loc='center left', borderaxespad=0.,fontsize=14)

#################### ALTGD ###############################
################### NORTE
cols = ['FosilN', 'HidroN', 'SolarN', 'EolicoN']
colors = ['#A1140B', '#207653', '#FBAA1B', '#8FC73E']

# Separate positive and negative parts
pos_data = ALTGD[cols].clip(lower=0)  # keep only positive values
neg_data = ALTGD[cols].clip(upper=0)  # keep only negative values

pos_bottoms = N.zeros(len(ALTGD))
neg_bottoms = N.zeros(len(ALTGD))

for col, color in zip(cols, colors):
    # Plot positive part
    axs[1,0].bar(ALTGD.index, pos_data[col], bottom=pos_bottoms,
                 color=color, alpha=0.8)
    pos_bottoms += pos_data[col].values

    # Plot negative part
    axs[1,0].bar(ALTGD.index, neg_data[col], bottom=neg_bottoms,
                 color=color, alpha=0.8)
    neg_bottoms += neg_data[col].values
axs[1,0].xaxis.set_tick_params(labelsize=12, rotation=90)
axs[1,0].set_xlim(2022.5, 2050.5)
axs[1,0].axhline(linewidth=1, color='black', label='_nolegend_')
# ~ axs[1,0].set_ylabel('[GWh]', fontsize=14)
axs[1,0].set_ylim(-1500, 1500)
axs[1,0].yaxis.set_tick_params(labelsize=12)

################### CENTRO
cols = ['FosilC', 'HidroC', 'SolarC', 'EolicoC']
colors = ['#A1140B', '#207653', '#FBAA1B', '#8FC73E']

# Separate positive and negative parts
pos_data = ALTGD[cols].clip(lower=0)  # keep only positive values
neg_data = ALTGD[cols].clip(upper=0)  # keep only negative values

pos_bottoms = N.zeros(len(ALTGD))
neg_bottoms = N.zeros(len(ALTGD))

for col, color in zip(cols, colors):
    # Plot positive part
    axs[1,1].bar(ALTGD.index, pos_data[col], bottom=pos_bottoms,
                 color=color, alpha=0.8)
    pos_bottoms += pos_data[col].values

    # Plot negative part
    axs[1,1].bar(ALTGD.index, neg_data[col], bottom=neg_bottoms,
                 color=color, alpha=0.8)
    neg_bottoms += neg_data[col].values
axs[1,1].xaxis.set_tick_params(labelsize=12, rotation=90)
axs[1,1].set_xlim(2022.5, 2050.5)
axs[1,1].axhline(linewidth=1, color='black', label='_nolegend_')

################### ORIENTE
cols = ['FosilO', 'HidroO', 'SolarO', 'EolicoO']
colors = ['#A1140B', '#207653', '#FBAA1B', '#8FC73E']

# Separate positive and negative parts
pos_data = ALTGD[cols].clip(lower=0)  # keep only positive values
neg_data = ALTGD[cols].clip(upper=0)  # keep only negative values

pos_bottoms = N.zeros(len(ALTGD))
neg_bottoms = N.zeros(len(ALTGD))

for col, color in zip(cols, colors):
    # Plot positive part
    axs[1,2].bar(ALTGD.index, pos_data[col], bottom=pos_bottoms,
                 color=color, alpha=0.8)
    pos_bottoms += pos_data[col].values

    # Plot negative part
    axs[1,2].bar(ALTGD.index, neg_data[col], bottom=neg_bottoms,
                 color=color, alpha=0.8)
    neg_bottoms += neg_data[col].values
axs[1,2].xaxis.set_tick_params(labelsize=12, rotation=90)
axs[1,2].set_xlim(2022.5, 2050.5)
axs[1,2].axhline(linewidth=1, color='black', label='_nolegend_')

################### SUR
cols = ['FosilS', 'HidroS', 'SolarS', 'EolicoS']
colors = ['#A1140B', '#207653', '#FBAA1B', '#8FC73E']

# Separate positive and negative parts
pos_data = ALTGD[cols].clip(lower=0)  # keep only positive values
neg_data = ALTGD[cols].clip(upper=0)  # keep only negative values

pos_bottoms = N.zeros(len(ALTGD))
neg_bottoms = N.zeros(len(ALTGD))

for col, color in zip(cols, colors):
    # Plot positive part
    axs[1,3].bar(ALTGD.index, pos_data[col], bottom=pos_bottoms,
                 color=color, alpha=0.8)
    pos_bottoms += pos_data[col].values

    # Plot negative part
    axs[1,3].bar(ALTGD.index, neg_data[col], bottom=neg_bottoms,
                 color=color, alpha=0.8)
    neg_bottoms += neg_data[col].values
axs[1,3].xaxis.set_tick_params(labelsize=12, rotation=90)
axs[1,3].set_xlim(2022.5, 2050.5)
axs[1,3].axhline(linewidth=1, color='black', label='_nolegend_')
'''
#################### ALTGDM ###############################
################### NORTE
cols = ['FosilN', 'HidroN', 'SolarN', 'EolicoN']
colors = ['#A1140B', '#207653', '#FBAA1B', '#8FC73E']

# Separate positive and negative parts
pos_data = ALTGDM[cols].clip(lower=0)  # keep only positive values
neg_data = ALTGDM[cols].clip(upper=0)  # keep only negative values

pos_bottoms = N.zeros(len(ALTGDM))
neg_bottoms = N.zeros(len(ALTGDM))

for col, color in zip(cols, colors):
    # Plot positive part
    axs[0].bar(ALTGDM.index, pos_data[col], bottom=pos_bottoms,
                 color=color, alpha=0.8)
    pos_bottoms += pos_data[col].values

    # Plot negative part
    axs[0].bar(ALTGDM.index, neg_data[col], bottom=neg_bottoms,
                 color=color, alpha=0.8)
    neg_bottoms += neg_data[col].values
    
axs[0].set_title('Norte', fontsize = 16, weight = 'bold')
axs[0].xaxis.set_tick_params(labelsize=12, rotation=90)
axs[0].set_xlim(2022.5, 2050.5)
axs[0].axhline(linewidth=1, color='black', label='_nolegend_')
axs[0].set_ylim(-1500, 1500)
axs[0].yaxis.set_tick_params(labelsize=12)

################### CENTRO
cols = ['FosilC', 'HidroC', 'SolarC', 'EolicoC']
colors = ['#A1140B', '#207653', '#FBAA1B', '#8FC73E']

# Separate positive and negative parts
pos_data = ALTGDM[cols].clip(lower=0)  # keep only positive values
neg_data = ALTGDM[cols].clip(upper=0)  # keep only negative values

pos_bottoms = N.zeros(len(ALTGDM))
neg_bottoms = N.zeros(len(ALTGDM))

for col, color in zip(cols, colors):
    # Plot positive part
    axs[1].bar(ALTGDM.index, pos_data[col], bottom=pos_bottoms,
                 color=color, alpha=0.8)
    pos_bottoms += pos_data[col].values

    # Plot negative part
    axs[1].bar(ALTGDM.index, neg_data[col], bottom=neg_bottoms,
                 color=color, alpha=0.8)
    neg_bottoms += neg_data[col].values
    
axs[1].set_title('Centro', fontsize = 16, weight = 'bold')
axs[1].xaxis.set_tick_params(labelsize=12, rotation=90)
axs[1].set_xlim(2022.5, 2050.5)
axs[1].axhline(linewidth=1, color='black', label='_nolegend_')

################### ORIENTE
cols = ['FosilO', 'HidroO', 'SolarO', 'EolicoO']
colors = ['#A1140B', '#207653', '#FBAA1B', '#8FC73E']

# Separate positive and negative parts
pos_data = ALTGDM[cols].clip(lower=0)  # keep only positive values
neg_data = ALTGDM[cols].clip(upper=0)  # keep only negative values

pos_bottoms = N.zeros(len(ALTGDM))
neg_bottoms = N.zeros(len(ALTGDM))

for col, color in zip(cols, colors):
    # Plot positive part
    axs[2].bar(ALTGDM.index, pos_data[col], bottom=pos_bottoms,
                 color=color, alpha=0.8)
    pos_bottoms += pos_data[col].values

    # Plot negative part
    axs[2].bar(ALTGDM.index, neg_data[col], bottom=neg_bottoms,
                 color=color, alpha=0.8)
    neg_bottoms += neg_data[col].values
    
axs[2].set_title('Oriente', fontsize = 16, weight = 'bold')
axs[2].xaxis.set_tick_params(labelsize=12, rotation=90)
axs[2].set_xlim(2022.5, 2050.5)
axs[2].axhline(linewidth=1, color='black', label='_nolegend_')

################### SUR
cols = ['FosilS', 'HidroS', 'SolarS', 'EolicoS']
colors = ['#A1140B', '#207653', '#FBAA1B', '#8FC73E']

# Separate positive and negative parts
pos_data = ALTGDM[cols].clip(lower=0)  # keep only positive values
neg_data = ALTGDM[cols].clip(upper=0)  # keep only negative values

pos_bottoms = N.zeros(len(ALTGDM))
neg_bottoms = N.zeros(len(ALTGDM))

for col, color in zip(cols, colors):
    # Plot positive part
    axs[3].bar(ALTGDM.index, pos_data[col], bottom=pos_bottoms,
                 color=color, alpha=0.8)
    pos_bottoms += pos_data[col].values

    # Plot negative part
    axs[3].bar(ALTGDM.index, neg_data[col], bottom=neg_bottoms,
                 color=color, alpha=0.8)
    neg_bottoms += neg_data[col].values
   
axs[3].set_title('Sur', fontsize = 16, weight = 'bold')
axs[3].xaxis.set_tick_params(labelsize=12, rotation=90)
axs[3].set_xlim(2022.5, 2050.5)
axs[3].axhline(linewidth=1, color='black', label='_nolegend_')

fig.subplots_adjust(wspace=0.1, hspace=0.1)
# ~ plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)
# ~ fig.text(.24, 0.97, 'Escenario Tendencial', va='center' ,fontsize=16, weight='bold')  
# ~ fig.text(.6, 0.97, 'Escenario Alternativo', va='center' ,fontsize=16, weight='bold')  
# ~ fig.text(0.91, 0.69, 'ALT', va='center' ,fontsize=16, weight='bold', rotation='vertical')  
# ~ fig.text(0.91, 0.3, 'ALTGD - ALT', va='center' ,fontsize=16, weight='bold', rotation='vertical')  
fig.text(0.91, 0.5, 'ALTGDM - ALT', va='center' ,fontsize=16, weight='bold', rotation='vertical')  
fig.text(0.08, 0.5, '[GWh]', va='center' ,fontsize=14, rotation='vertical')  

plt.savefig('inputALTGDM.jpg', dpi=300, bbox_inches="tight")
