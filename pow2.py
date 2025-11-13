import numpy as N
import matplotlib.pyplot as plt
from datetime import datetime
import pandas as pd
import seaborn as sns
from scipy.stats import spearmanr
from matplotlib.ticker import MultipleLocator

pow30 = pd.read_csv('/home/emi/Documents/GENERIS/GENERISpy/PowGen30.txt', header=0, delimiter=',', na_values='-99')
pow40 = pd.read_csv('/home/emi/Documents/GENERIS/GENERISpy/PowGen40.txt', header=0, delimiter=',', na_values='-99')
pow50 = pd.read_csv('/home/emi/Documents/GENERIS/GENERISpy/PowGen50.txt', header=0, delimiter=',', na_values='-99')

# ~ print(powgen)

dry30 = pow30.iloc[0:12]
wet30 = pow30.iloc[12:24]

dry40 = pow40.iloc[0:12]
wet40 = pow40.iloc[12:24]

dry50 = pow50.iloc[0:12]
wet50 = pow50.iloc[12:24]
print(dry50)


fig, ((ax1,ax2),(ax3,ax4),(ax5,ax6)) = plt.subplots(3,2,figsize=(7,8),sharey=True, sharex=True)

################### 2030
##positivos
ax1.bar(dry30['hora'], dry30['TG'], color='#36495A')
ax1.bar(dry30['hora'], dry30['Motor'], bottom=dry30['TG'], color='#6D6F70')
ax1.bar(dry30['hora'], dry30['Solar'], bottom=dry30['TG']+dry30['Motor'], color='#FBAA1B')
ax1.bar(dry30['hora'], dry30['Eolica'], bottom=dry30['TG']+dry30['Motor']+dry30['Solar'], color='#8FC73E')
ax1.bar(dry30['hora'], dry30['Hidro'], bottom=dry30['TG']+dry30['Motor']+dry30['Solar']+dry30['Eolica'], color='#207653')
ax1.axhline(linewidth=1, color='black')

##negativos
ax1.bar(dry30['hora'], dry30['TGn'], color='#36495A')
ax1.bar(dry30['hora'], dry30['Motorn'], bottom=dry30['TGn'], color='#6D6F70')
ax1.bar(dry30['hora'], dry30['CCn'], bottom=dry30['TGn']+dry30['Motorn'], color='#A1140B')
ax1.bar(dry30['hora'], dry30['Solarn'], bottom=dry30['TGn']+dry30['Motorn']+dry30['CCn'], color='#FBAA1B')
ax1.bar(dry30['hora'], dry30['Eolican'], bottom=dry30['TGn']+dry30['Motorn']+dry30['CCn']+dry30['Solarn'], color='#8FC73E')
ax1.bar(dry30['hora'], dry30['Hidron'], bottom=dry30['TGn']+dry30['Motorn']+dry30['CCn']+dry30['Solarn']+dry30['Eolican'], color='#207653')
ax1.set_ylim(-650, 200)
ax1.set_title('Estación seca \n (may-oct)', fontsize = 16)
ax1.yaxis.set_tick_params(labelsize=12)
ax1.xaxis.set_tick_params(labelsize=12, rotation=90)
ax1.text(9,-600,'2030',fontsize=12,weight='bold')


##positivos
ax2.bar(wet30['hora'], wet30['TG'], color='#36495A')
ax2.bar(wet30['hora'], wet30['Motor'], bottom=wet30['TG'], color='#6D6F70')
ax2.bar(wet30['hora'], wet30['Solar'], bottom=wet30['TG']+wet30['Motor'], color='#FBAA1B')
ax2.bar(wet30['hora'], wet30['Eolica'], bottom=wet30['TG']+wet30['Motor']+wet30['Solar'], color='#8FC73E')
ax2.bar(wet30['hora'], wet30['Hidro'], bottom=wet30['TG']+wet30['Motor']+wet30['Solar']+wet30['Eolica'], color='#207653')
ax2.axhline(linewidth=1, color='black')

##negativos
ax1.bar(wet30['hora'], wet30['TGn'], color='#36495A')
ax1.bar(wet30['hora'], wet30['Motorn'], bottom=wet30['TGn'], color='#6D6F70')
ax1.bar(wet30['hora'], wet30['CCn'], bottom=wet30['TGn']+wet30['Motorn'], color='#A1140B')
ax1.bar(wet30['hora'], wet30['Solarn'], bottom=wet30['TGn']+wet30['Motorn']+wet30['CCn'], color='#FBAA1B')
ax1.bar(wet30['hora'], wet30['Eolican'], bottom=wet30['TGn']+wet30['Motorn']+wet30['CCn']+wet30['Solarn'], color='#8FC73E')
ax1.bar(wet30['hora'], wet30['Hidron'], bottom=wet30['TGn']+wet30['Motorn']+wet30['CCn']+wet30['Solarn']+wet30['Eolican'], color='#207653')

ax2.set_title('Estación húmeda \n (nov-abr)', fontsize = 16)
ax2.xaxis.set_tick_params(labelsize=12, rotation=90)
ax2.text(9,-600,'2030',fontsize=12,weight='bold')

# ~ ax2.legend(["TG", "TV", "Motor", "CC", "Solar", "Eolica", "Hidro"], frameon=False,bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)

################### 2040

##positivos
ax3.bar(dry40['hora'], dry40['TG'], color='#36495A')
ax3.bar(dry40['hora'], dry40['CC'], bottom=dry40['TG'], color='#A1140B')
ax3.bar(dry40['hora'], dry40['Solar'], bottom=dry40['TG']+dry40['CC'], color='#FBAA1B')
ax3.bar(dry40['hora'], dry40['Eolica'], bottom=dry40['TG']+dry40['CC']+dry40['Solar'], color='#8FC73E')
ax3.axhline(linewidth=1, color='black')

##negativos
ax3.bar(dry40['hora'], dry40['TGn'], color='#36495A')
ax3.bar(dry40['hora'], dry40['TVn'], bottom=dry40['TGn'], color='black')
ax3.bar(dry40['hora'], dry40['Motorn'], bottom=dry40['TGn']+dry40['TVn'], color='#6D6F70')
ax3.bar(dry40['hora'], dry40['CCn'], bottom=dry40['TGn']+dry40['TVn']+dry40['Motorn'], color='#A1140B')
ax3.bar(dry40['hora'], dry40['Solarn'], bottom=dry40['TGn']+dry40['TVn']+dry40['Motorn']+dry40['CCn'], color='#FBAA1B')
ax3.bar(dry40['hora'], dry40['Eolican'], bottom=dry40['TGn']+dry40['TVn']+dry40['Motorn']+dry40['CCn']+dry40['Solarn'], color='#8FC73E')
ax3.bar(dry40['hora'], dry40['Hidron'], bottom=dry40['TGn']+dry40['TVn']+dry40['Motorn']+dry40['CCn']+dry40['Solarn']+dry40['Eolican'], color='#207653')
ax3.set_ylim(-650, 200)
# ~ ax3.set_title('Estación seca \n (may-oct)', fontsize = 16)
ax3.yaxis.set_tick_params(labelsize=12)
ax3.xaxis.set_tick_params(labelsize=12, rotation=90)
ax3.set_ylabel('[MW]', fontsize=14)
ax3.text(9,-600,'2040',fontsize=12,weight='bold')

##negativos
ax4.bar(wet40['hora'], wet40['TGn'], color='#36495A')
ax4.bar(wet40['hora'], wet40['TVn'], bottom=wet40['TGn'], color='black')
ax4.bar(wet40['hora'], wet40['Motorn'], bottom=wet40['TGn']+wet40['TVn'], color='#6D6F70')
ax4.bar(wet40['hora'], wet40['CCn'], bottom=wet40['TGn']+wet40['TVn']+wet40['Motorn'], color='#A1140B')
ax4.bar(wet40['hora'], wet40['Solarn'], bottom=wet40['TGn']+wet40['TVn']+wet40['Motorn']+wet40['CCn'], color='#FBAA1B')
ax4.bar(wet40['hora'], wet40['Eolican'], bottom=wet40['TGn']+wet40['TVn']+wet40['Motorn']+wet40['CCn']+wet40['Solarn'], color='#8FC73E')
ax4.bar(wet40['hora'], wet40['Hidron'], bottom=wet40['TGn']+wet40['TVn']+wet40['Motorn']+wet40['CCn']+wet40['Solarn']+wet40['Eolican'], color='#207653')

##positivos
ax4.bar(wet40['hora'], wet40['TG'], color='#36495A')
ax4.bar(wet40['hora'], wet40['CC'], bottom=wet40['TG'], color='#A1140B')
ax4.bar(wet40['hora'], wet40['Solar'], bottom=wet40['TG']+wet40['CC'], color='#FBAA1B')
ax4.bar(wet40['hora'], wet40['Eolica'], bottom=wet40['TG']+wet40['CC']+wet40['Solar'], color='#8FC73E')
ax4.axhline(linewidth=1, color='black', label='_nolegend_')


# ~ ax4.set_title('Estación húmeda \n (nov-abr)', fontsize = 16)
ax4.xaxis.set_tick_params(labelsize=12, rotation=90)
ax4.text(9,-600,'2040',fontsize=12,weight='bold')
ax4.legend(["TG", "TV", "Motor", "CC", "Solar", "Eolica", "Hidro"], frameon=False,bbox_to_anchor=(1.05, 2), loc='upper left', borderaxespad=0.)

################### 2050
ax5.bar(dry50['hora'], dry50['TG'], color='#36495A')
ax5.bar(dry50['hora'], dry50['TV'], bottom=dry50['TG'], color='black')
ax5.bar(dry50['hora'], dry50['Motor'], bottom=dry50['TG']+dry50['TV'], color='#6D6F70')
ax5.bar(dry50['hora'], dry50['CC'], bottom=dry50['TG']+dry50['TV']+dry50['Motor'], color='#A1140B')
ax5.bar(dry50['hora'], dry50['Solar'], bottom=dry50['TG']+dry50['TV']+dry50['Motor']+dry50['CC'], color='#FBAA1B')
ax5.set_ylim(-650, 200)
# ~ ax5.set_title('Estación seca \n (may-oct)', fontsize = 16)
ax5.yaxis.set_tick_params(labelsize=12)
ax5.xaxis.set_tick_params(labelsize=12, rotation=90)
ax5.set_xlabel('horas', fontsize=14)
ax5.text(9,-600,'2050',fontsize=12,weight='bold')
ax5.axhline(linewidth=1, color='black')

ax6.bar(wet50['hora'], wet50['TG'], color='#36495A')
ax6.bar(wet50['hora'], wet50['TV'], bottom=wet50['TG'], color='black')
ax6.bar(wet50['hora'], wet50['Motor'], bottom=wet50['TG']+wet50['TV'], color='#6D6F70')
ax6.bar(wet50['hora'], wet50['CC'], bottom=wet50['TG']+wet50['TV']+wet50['Motor'], color='#A1140B')
ax6.bar(wet50['hora'], wet50['Solar'], bottom=wet50['TG']+wet50['TV']+wet50['Motor']+wet50['CC'], color='#FBAA1B')
# ~ ax6.set_title('Estación húmeda \n (nov-abr)', fontsize = 16)
ax6.xaxis.set_tick_params(labelsize=12, rotation=90)
ax6.set_xlabel('horas', fontsize=14)
# ~ ax6.legend(["TG", "TV", "Motor", "CC", "Solar"], frameon=False,bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)
ax6.text(9,-600,'2050',fontsize=12,weight='bold')
ax6.axhline(linewidth=1, color='black')

fig.subplots_adjust(wspace=0.1, hspace=0.1)
# ~ plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)

plt.savefig('Pow2.svg', dpi=300, bbox_inches="tight")
