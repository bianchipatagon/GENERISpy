import numpy as N
import matplotlib.pyplot as plt
from datetime import datetime
import pandas as pd
import seaborn as sns
from scipy.stats import spearmanr
from matplotlib.ticker import MultipleLocator

emis = pd.read_csv('/home/emi/Documents/GENERIS/GENERISpy/emisiones.txt', header=0, delimiter=',', na_values='-99')
print(emis)

fig, ax = plt.subplots(1,1,figsize=(5, 3), sharey=True)

ax.bar(emis['año'], emis['TG'], color='#36495A')
ax.bar(emis['año'], emis['Motor'], bottom=emis['TG'], color='#6D6F70')
ax.bar(emis['año'], emis['CC'], bottom=emis['TG']+emis['Motor'], color='#A1140B')
ax.set_ylim(-800, 0)
# ~ ax.set_title('Estación seca \n (may-oct)', fontsize = 16)
ax.yaxis.set_tick_params(labelsize=12)
ax.xaxis.set_tick_params(labelsize=12, rotation=90)
ax.set_ylabel('m. ton. métricas \n CO$_2$ equiv.', fontsize=14)
ax.set_xlabel('años', fontsize=14)

# ~ ax2.bar(wet['hora'], wet['TG'], color='#36495A')
# ~ ax2.bar(wet['hora'], wet['TV'], bottom=wet['TG'], color='black')
# ~ ax2.bar(wet['hora'], wet['Motor'], bottom=wet['TG']+wet['TV'], color='#6D6F70')
# ~ ax2.bar(wet['hora'], wet['CC'], bottom=wet['TG']+wet['TV']+wet['Motor'], color='#A1140B')
# ~ ax2.bar(wet['hora'], wet['Solar'], bottom=wet['TG']+wet['TV']+wet['Motor']+wet['CC'], color='#FBAA1B')
# ~ ax2.set_title('Estación húmeda \n (nov-abr)', fontsize = 16)
# ~ ax2.xaxis.set_tick_params(labelsize=12, rotation=90)
# ~ ax2.set_xlabel('horas', fontsize=14)
ax.legend(["TG", "TV", "Motor", "CC", "Solar"], frameon=False,bbox_to_anchor=(.35, .35), borderaxespad=0.)

# ~ fig.subplots_adjust(wspace=0.2)
# ~ plt.legend(bbox_to_anchor=(.02, .02), loc='upper left', borderaxespad=0.)

plt.savefig('emisiones.svg', dpi=300, bbox_inches="tight")

