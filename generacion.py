import matplotlib.pyplot as plt
import numpy as np
from matplotlib.gridspec import GridSpec
import pandas as pd

potencia = pd.read_csv('/home/emi/Documents/GENERIS/GENERISpy/generacion.txt', header=0, delimiter=';', na_values='-999')
print(potencia)

colors = ['#A1140B', '#FBAA1B','#8FC73E','#207653','#FBAA1B']
labels = ['Fosil','Solar','Eólica','Hidro', 'Solar Dist']
hatch_patterns = ['', '', '', '', '/']

fig = plt.figure(figsize=(24, 12))
gs = GridSpec(1,5, figure=fig, width_ratios=[1,1.39,1.39,1.4,1.39])

ax1 = fig.add_subplot(gs[0, 0])
ax1.pie(potencia['2025'], colors=colors,autopct='%1.1f%%', startangle=90, radius=1.3,wedgeprops=dict(width=0.98, edgecolor='white'),labeldistance=1.1,textprops=dict(color="black", fontsize=16), hatch=hatch_patterns)
ax1.set_title('2025 (11430 GWh)', fontsize=24, fontweight='bold')

ax2 = fig.add_subplot(gs[0, 1])
ax2.pie(potencia['T2050'], colors=colors,autopct='%1.1f%%', startangle=90, radius=1.3,wedgeprops=dict(width=0.98, edgecolor='white'),labeldistance=1.1,textprops=dict(color="black", fontsize=16), hatch=hatch_patterns)
ax2.set_title('Escenario Tendencial \n 2050 (22410 GWh)', fontsize=24, fontweight='bold')

ax3 = fig.add_subplot(gs[0, 2])
ax3.pie(potencia['T2050GD'], colors=colors,autopct='%1.1f%%', startangle=90, radius=1.3,wedgeprops=dict(width=0.98, edgecolor='white'),labeldistance=1.1,textprops=dict(color="black", fontsize=16), hatch=hatch_patterns)
ax3.set_title('Escenario Tendencial \n +Distribuida \n 2050 (20610 GWh)', fontsize=24, fontweight='bold')

ax4 = fig.add_subplot(gs[0, 3])
ax4.pie(potencia['A2050'], colors=colors,autopct='%1.1f%%', startangle=90, radius=1.3,wedgeprops=dict(width=0.98, edgecolor='white'),labeldistance=1.1,textprops=dict(color="black", fontsize=16), hatch=hatch_patterns)
ax4.set_title('Escenario Alternativo \n 2050 (22256 GWh)', fontsize=24, fontweight='bold')

ax5 = fig.add_subplot(gs[0, 4])
ax5.pie(potencia['A2050GD'], colors=colors,autopct='%1.1f%%', startangle=90, radius=1.3,wedgeprops=dict(width=0.98, edgecolor='white'),labeldistance=1.1,textprops=dict(color="black", fontsize=16), hatch=hatch_patterns)
ax5.set_title('Escenario Alternativo \n +Distribuida \n 2050 (22122 GWh)', fontsize=24, fontweight='bold')
ax5.legend(labels,  loc="center left", bbox_to_anchor=(1, 0, 0.5, 1), fontsize=16, frameon=False)

plt.savefig('GENERACION.svg', dpi=300, bbox_inches="tight")
