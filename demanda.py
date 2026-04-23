import matplotlib.pyplot as plt

cat1 = 'GN','GLP','Diesel','Jet Fuel','Gasolina','Elec','Biomasa'
counts1 = [ 21.2,6.1 ,  26.0,  1.3,  22.2 ,  10.4, 8.9]
colors1 = ['#FBAA1B','#FBAA1B', '#A1140B','#A1140B','#A1140B','#36495A','#207653']
hatch1 = ['', '/', '', '.', '/', '', '']

cat2 = 'Norte', 'Centro', 'Oriente', 'Sur', 'Pando'
counts2 = [  2278.7, 2167.6, 4128.6 ,1730.4, 78.4 ]
colors2 = ['#FBAA1B','#8FC73E', '#207653','#A1140B','#36495A']

cat3 = 'Residencial', 'Transporte', 'Industria', 'Comercial y Publico', 'Agro Pesca y Mineria', 'Construccion'
counts3 = [   3918.2 ,38.1 ,2503.8 ,2414.5 ,1171.4 ,337.7 ]
colors3 = ['#36495A','#207653', '#FBAA1B','#8FC73E','#A1140B', '#6D6F70']


fig,ax = plt.subplots(1,3,figsize=(16,4), sharey=True)
ax[0].set_title('Combustible', fontsize=16, fontweight='bold')
ax[0].pie(counts1, labels = cat1, autopct='%1.1f%%',colors=colors1,hatch=hatch1,wedgeprops=dict(width=0.98, edgecolor='white'))
ax[0].legend(cat1,  loc="center left", bbox_to_anchor=(1, 0, 0.5, 1), fontsize=13, frameon=False)

# ~ ax.pie(sizes. labels=labels. autopct='%1.1f%%')
# ~ ax.set_title('% generación Suiza 2023'. fontsize = 16)
ax[1].set_title('Región', fontsize=16, fontweight='bold')
ax[1].pie(counts2, labels = cat2, autopct='%1.1f%%',colors=colors2,wedgeprops=dict(width=0.98, edgecolor='white'))
ax[1].legend(cat2,  loc="center left", bbox_to_anchor=(1, 0, 0.5, 1), fontsize=13, frameon=False)

ax[2].set_title('Sector', fontsize=16, fontweight='bold')
ax[2].pie(counts3, labels = cat3, autopct='%1.1f%%',colors=colors3,wedgeprops=dict(width=0.98, edgecolor='white'))
ax[2].legend(cat3,  loc="center left", bbox_to_anchor=(1, 0, 0.5, 1), fontsize=13, frameon=False)


fig.subplots_adjust(wspace=0.1)

plt.savefig('demanda.svg',dpi=300, bbox_inches="tight")
