import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.colors as mcolors
import numpy as N
from matplotlib.gridspec import GridSpec


ins = pd.read_csv('/home/emi/Documents/GENERIS/GENERISpy/inst.txt', header=0, delimiter=';', na_values='-999')

cat1 = 'Norte','Centro','Oriente','Sur'
counts1 = ins['EolicaT']
counts2 = ins['SolarT']
counts3 = ins['HidroT']

counts4 = ins['EolicaA']
counts5 = ins['SolarA']
counts6 = ins['HidroA']

hatch1 = ['', '/', '', '.']

# --- Dorados ---
base_color1 = '#FBAA1B'   # single hue for all series
alpha_min  = 0.2
alpha_max  = 0.9
 
# --- Build per-layer colors with varying alpha ---
n = 4
alphas = N.linspace(alpha_min, alpha_max, n)
print(alphas)
r, g, b = mcolors.to_rgb(base_color1)
colors1 = [(r, g, b, a) for a in alphas]

# --- Verde Claro ---
base_color2 = '#8FC73E'   # single hue for all series
alpha_min  = 0.2
alpha_max  = 0.9
 
# --- Build per-layer colors with varying alpha ---
n = 4
alphas = N.linspace(alpha_min, alpha_max, n)
print(alphas)
r, g, b = mcolors.to_rgb(base_color2)
colors2 = [(r, g, b, a) for a in alphas]

# --- Verde Oscuro ---
base_color3 = '#207653'   # single hue for all series
alpha_min  = 0.2
alpha_max  = 0.9
 
# --- Build per-layer colors with varying alpha ---
n = 4
alphas = N.linspace(alpha_min, alpha_max, n)
print(alphas)
r, g, b = mcolors.to_rgb(base_color3)
colors3 = [(r, g, b, a) for a in alphas]

fig,((ax1,ax2, ax3),(ax4, ax5, ax6)) = plt.subplots(2,3,figsize=(12,6), sharey=True)
# ~ fig = plt.figure(figsize=(16, 8))

# ~ gs = GridSpec(2,3, figure=fig, width_ratios=[1,1.3,1.9,3.5,6, 7.7])

ax1.set_title('Eolica', fontsize=16, fontweight='bold')
ax1.pie(counts1, labels = cat1, autopct='%1.1f%%',colors=colors2,wedgeprops=dict(width=0.98, edgecolor='white'),hatch=hatch1)
ax1.legend(cat1,  loc="lower left", bbox_to_anchor=(1, 0, 0.5, 1), fontsize=13, frameon=False)

ax2.set_title('TEN \n Solar', fontsize=16, fontweight='bold')
ax2.pie(counts2, labels = cat1, autopct='%1.1f%%',colors=colors1,wedgeprops=dict(width=0.98, edgecolor='white'),hatch=hatch1)
ax2.legend(cat1,  loc="lower left", bbox_to_anchor=(1, 0, 0.5, 1), fontsize=13, frameon=False)

ax3.set_title('Hidro', fontsize=16, fontweight='bold')
ax3.pie(counts3, labels = cat1, autopct='%1.1f%%',colors=colors3,wedgeprops=dict(width=0.98, edgecolor='white'),hatch=hatch1)
ax3.legend(cat1,  loc="lower left", bbox_to_anchor=(1, 0, 0.5, 1), fontsize=13, frameon=False)

# ~ ax4.set_title('Eolica', fontsize=16, fontweight='bold')
ax4.pie(counts4, labels = cat1, autopct='%1.1f%%',colors=colors2,wedgeprops=dict(width=0.98, edgecolor='white'),hatch=hatch1)
# ~ ax4.legend(cat1,  loc="center left", bbox_to_anchor=(1, 0, 0.5, 1), fontsize=13, frameon=False)

ax5.set_title('ALT', fontsize=16, fontweight='bold')
ax5.pie(counts5, labels = cat1, autopct='%1.1f%%',colors=colors1,wedgeprops=dict(width=0.98, edgecolor='white'),hatch=hatch1)
# ~ ax5.legend(cat1,  loc="center left", bbox_to_anchor=(1, 0, 0.5, 1), fontsize=13, frameon=False)

# ~ ax6.set_title('Hidro', fontsize=16, fontweight='bold')
ax6.pie(counts6, labels = cat1, autopct='%1.1f%%',colors=colors3,wedgeprops=dict(width=0.98, edgecolor='white'),hatch=hatch1)
# ~ ax6.legend(cat1,  loc="center left", bbox_to_anchor=(1, 0, 0.5, 1), fontsize=13, frameon=False)

fig.subplots_adjust(wspace=0.02)
fig.subplots_adjust(hspace=0.02)

plt.savefig('inst.svg',dpi=300, bbox_inches="tight")
