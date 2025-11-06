import numpy as N
import matplotlib.pyplot as plt
from datetime import datetime
import pandas as pd
import seaborn as sns
from scipy.stats import spearmanr
from matplotlib.ticker import MultipleLocator

powgen = pd.read_csv('/home/emi/Documents/GENERIS/python/PowGen.txt', header=0, delimiter=',', na_values='-99')
# ~ print(powgen)

dry = powgen.iloc[0:12]
wet = powgen.iloc[12:24]


fig, (ax1,ax2) = plt.subplots(1,2,figsize=(8, 3), sharey=True)
ax1.bar(dry['hora'], dry['TG'], color='#36495A')
ax1.bar(dry['hora'], dry['TV'], bottom=dry['TG'], color='black')
ax1.bar(dry['hora'], dry['Motor'], bottom=dry['TG']+dry['TV'], color='#6D6F70')
ax1.bar(dry['hora'], dry['CC'], bottom=dry['TG']+dry['TV']+dry['Motor'], color='#A1140B')
ax1.bar(dry['hora'], dry['Solar'], bottom=dry['TG']+dry['TV']+dry['Motor']+dry['CC'], color='#FBAA1B')
ax1.set_ylim(-650, 0)
ax1.set_title('Estación seca \n (may-oct)', fontsize = 16)
ax1.yaxis.set_tick_params(labelsize=12)
ax1.xaxis.set_tick_params(labelsize=12, rotation=90)
ax1.set_ylabel('[MW]', fontsize=14)
ax1.set_xlabel('horas', fontsize=14)

ax2.bar(wet['hora'], wet['TG'], color='#36495A')
ax2.bar(wet['hora'], wet['TV'], bottom=wet['TG'], color='black')
ax2.bar(wet['hora'], wet['Motor'], bottom=wet['TG']+wet['TV'], color='#6D6F70')
ax2.bar(wet['hora'], wet['CC'], bottom=wet['TG']+wet['TV']+wet['Motor'], color='#A1140B')
ax2.bar(wet['hora'], wet['Solar'], bottom=wet['TG']+wet['TV']+wet['Motor']+wet['CC'], color='#FBAA1B')
ax2.set_title('Estación húmeda \n (nov-abr)', fontsize = 16)
ax2.xaxis.set_tick_params(labelsize=12, rotation=90)
ax2.set_xlabel('horas', fontsize=14)
ax2.legend(["TG", "TV", "Motor", "CC", "Solar"], frameon=False,bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)

fig.subplots_adjust(wspace=0.2)
# ~ plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)

plt.savefig('Pow.svg', dpi=300, bbox_inches="tight")
