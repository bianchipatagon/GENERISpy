import numpy as N
import matplotlib.pyplot as plt
from datetime import datetime
import pandas as pd
import seaborn as sns
from scipy.stats import spearmanr
from matplotlib.ticker import MultipleLocator
import matplotlib.patches as patches

alt30 = pd.read_csv('/home/emi/Documents/GENERIS/GENERISpy/MH30.txt', header=0, delimiter=';', na_values='-999', index_col=0)
alt40 = pd.read_csv('/home/emi/Documents/GENERIS/GENERISpy/MH40.txt', header=0, delimiter=';', na_values='-999', index_col=0)
alt50 = pd.read_csv('/home/emi/Documents/GENERIS/GENERISpy/MH50.txt', header=0, delimiter=';', na_values='-999', index_col=0)

adry30 = alt30.iloc[0:12]
awet30 = alt30.iloc[12:24]

adry40 = alt40.iloc[0:12]
awet40 = alt40.iloc[12:24]

adry50 = alt50.iloc[0:12]
awet50 = alt50.iloc[12:24]
print(adry50)
print(awet50)
fig, axs = plt.subplots(3,2,figsize=(8,8),sharex=True, sharey=True)

#################### ALTERNATIVO ###############################

################### 2030 seco

cols = ['Fosil', 'Solar', 'Eolica', 'Hidro']
colors = ['#A1140B', '#FBAA1B', '#8FC73E', '#207653']

# Separate positive and negative parts
pos_data = adry30[cols].clip(lower=0)  # keep only positive values
neg_data = adry30[cols].clip(upper=0)  # keep only negative values

pos_bottoms = N.zeros(len(adry30))
neg_bottoms = N.zeros(len(adry30))

for col, color in zip(cols, colors):
    # Plot positive part
    axs[0,0].bar(adry30.index, pos_data[col], bottom=pos_bottoms,
                 color=color, alpha=0.8)
    pos_bottoms += pos_data[col].values

    # Plot negative part
    axs[0,0].bar(adry30.index, neg_data[col], bottom=neg_bottoms,
                 color=color, alpha=0.8)
    neg_bottoms += neg_data[col].values

axs[0,0].axhline(linewidth=1, color='black')
axs[0,0].set_ylim(-750, 300)
axs[0,0].set_title('Estación seca \n (may-oct)', fontsize = 16)
axs[0,0].yaxis.set_tick_params(labelsize=12)
axs[0,0].xaxis.set_tick_params(labelsize=12, rotation=90)
axs[0,0].text(1,200,'2030',fontsize=12,weight='bold')

################### 2030 humedo

cols = ['Fosil', 'Solar', 'Eolica', 'Hidro']
colors = ['#A1140B', '#FBAA1B', '#8FC73E', '#207653']

# Separate positive and negative parts
pos_data = awet30[cols].clip(lower=0)  # keep only positive values
neg_data = awet30[cols].clip(upper=0)  # keep only negative values

pos_bottoms = N.zeros(len(awet30))
neg_bottoms = N.zeros(len(awet30))

for col, color in zip(cols, colors):
    # Plot positive part
    axs[0,1].bar(awet30.index, pos_data[col], bottom=pos_bottoms,
                 color=color, alpha=0.8)
    pos_bottoms += pos_data[col].values

    # Plot negative part
    axs[0,1].bar(awet30.index, neg_data[col], bottom=neg_bottoms,
                 color=color, alpha=0.8)
    neg_bottoms += neg_data[col].values

axs[0,1].axhline(linewidth=1, color='black')
axs[0,1].set_ylim(-750, 300)
axs[0,1].set_title('Estación húmeda \n (nov-abr)', fontsize = 16)
axs[0,1].yaxis.set_tick_params(labelsize=12)
axs[0,1].xaxis.set_tick_params(labelsize=12, rotation=90)
axs[0,1].text(1,200,'2030',fontsize=12,weight='bold')

################### 2040 seco

cols = ['Fosil', 'Solar', 'Eolica', 'Hidro']
colors = ['#A1140B', '#FBAA1B', '#8FC73E', '#207653']

# Separate positive and negative parts
pos_data = adry40[cols].clip(lower=0)  # keep only positive values
neg_data = adry40[cols].clip(upper=0)  # keep only negative values

pos_bottoms = N.zeros(len(adry40))
neg_bottoms = N.zeros(len(adry40))

for col, color in zip(cols, colors):
    # Plot positive part
    axs[1,0].bar(adry40.index, pos_data[col], bottom=pos_bottoms,
                 color=color, alpha=0.8)
    pos_bottoms += pos_data[col].values

    # Plot negative part
    axs[1,0].bar(adry40.index, neg_data[col], bottom=neg_bottoms,
                 color=color, alpha=0.8)
    neg_bottoms += neg_data[col].values

axs[1,0].axhline(linewidth=1, color='black')
axs[1,0].set_ylim(-750, 300)
axs[1,0].yaxis.set_tick_params(labelsize=12)
axs[1,0].xaxis.set_tick_params(labelsize=12, rotation=90)
axs[1,0].text(1,200,'2040',fontsize=12,weight='bold')
axs[1,0].set_ylabel('[MW]', fontsize=14)

################### 2040 humedo

cols = ['Fosil', 'Solar', 'Eolica', 'Hidro']
colors = ['#A1140B', '#FBAA1B', '#8FC73E', '#207653']

# Separate positive and negative parts
pos_data = awet40[cols].clip(lower=0)  # keep only positive values
neg_data = awet40[cols].clip(upper=0)  # keep only negative values

pos_bottoms = N.zeros(len(awet40))
neg_bottoms = N.zeros(len(awet40))

for col, color in zip(cols, colors):
    # Plot positive part
    axs[1,1].bar(awet40.index, pos_data[col], bottom=pos_bottoms,
                 color=color, alpha=0.8)
    pos_bottoms += pos_data[col].values

    # Plot negative part
    axs[1,1].bar(awet40.index, neg_data[col], bottom=neg_bottoms,
                 color=color, alpha=0.8)
    neg_bottoms += neg_data[col].values

axs[1,1].axhline(linewidth=1, color='black')
axs[1,1].set_ylim(-300, 300)
axs[1,1].yaxis.set_tick_params(labelsize=12)
axs[1,1].xaxis.set_tick_params(labelsize=12, rotation=90)
axs[1,1].text(1,200,'2040',fontsize=12,weight='bold')

################### 2050 seco

cols = ['Fosil', 'Solar', 'Eolica', 'Hidro']
colors = ['#A1140B', '#FBAA1B', '#8FC73E', '#207653']

# Separate positive and negative parts
pos_data = adry50[cols].clip(lower=0)  # keep only positive values
neg_data = adry50[cols].clip(upper=0)  # keep only negative values

pos_bottoms = N.zeros(len(adry50))
neg_bottoms = N.zeros(len(adry50))

for col, color in zip(cols, colors):
    # Plot positive part
    axs[2,0].bar(adry50.index, pos_data[col], bottom=pos_bottoms,
                 color=color, alpha=0.8)
    pos_bottoms += pos_data[col].values

    # Plot negative part
    axs[2,0].bar(adry50.index, neg_data[col], bottom=neg_bottoms,
                 color=color, alpha=0.8)
    neg_bottoms += neg_data[col].values

axs[2,0].axhline(linewidth=1, color='black')
axs[2,0].set_ylim(-300, 300)
axs[2,0].yaxis.set_tick_params(labelsize=12)
axs[2,0].xaxis.set_tick_params(labelsize=12, rotation=90)
axs[2,0].text(1,200,'2050',fontsize=12,weight='bold')
axs[2,0].set_xlabel('horas', fontsize=14)

################### 2050 humedo

cols = ['Fosil', 'Solar', 'Eolica', 'Hidro']
colors = ['#A1140B', '#FBAA1B', '#8FC73E', '#207653']

# Separate positive and negative parts
pos_data = awet50[cols].clip(lower=0)  # keep only positive values
neg_data = awet50[cols].clip(upper=0)  # keep only negative values

pos_bottoms = N.zeros(len(awet50))
neg_bottoms = N.zeros(len(awet50))

for col, color in zip(cols, colors):
    # Plot positive part
    axs[2,1].bar(awet50.index, pos_data[col], bottom=pos_bottoms,
                 color=color, alpha=0.8)
    pos_bottoms += pos_data[col].values

    # Plot negative part
    axs[2,1].bar(awet50.index, neg_data[col], bottom=neg_bottoms,
                 color=color, alpha=0.8)
    neg_bottoms += neg_data[col].values

axs[2,1].axhline(linewidth=1, color='black')
axs[2,1].set_ylim(-300, 300)
axs[2,1].yaxis.set_tick_params(labelsize=12)
axs[2,1].xaxis.set_tick_params(labelsize=12, rotation=90)
axs[2,1].text(1,200,'2050',fontsize=12,weight='bold')
axs[2,1].set_xlabel('horas', fontsize=14)

'''

'''
fig.subplots_adjust(wspace=0.1, hspace=0.1)
# ~ plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)
# ~ fig.text(.24, 0.97, 'Escenario Tendencial', va='center' ,fontsize=16, weight='bold')  
fig.text(.42, 0.97, '(ALT-M) - ALT', va='center' ,fontsize=16, weight='bold')  

plt.savefig('PowPOST.svg', dpi=300, bbox_inches="tight")
