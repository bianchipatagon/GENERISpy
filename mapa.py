import cartopy.crs as ccrs
from cartopy.mpl.ticker import LongitudeFormatter, LatitudeFormatter
import matplotlib.pyplot as plt
import cartopy.feature as cfeature
from cartopy.feature import ShapelyFeature
from cartopy.io.shapereader import Reader
from matplotlib.offsetbox import AnnotationBbox, OffsetImage
from shapely.geometry.polygon import LinearRing
from matplotlib.patches import Rectangle
import pandas as pd
import geopandas as gpd

Bolivia = gpd.read_file('/home/emi/Documents/GENERIS/mapa/shapes/Mapa de limites departamentales de Bolivia/limites/limites_departamentales.shp')
print(Bolivia)
Sur = Bolivia.iloc[[1, 5, 7]]
Sur = Sur.dissolve()
Norte = Bolivia.iloc[[0, 8]]
Norte = Norte.dissolve()
Centro = Bolivia.iloc[[2, 6]]
Centro = Centro.dissolve()
Oriente = Bolivia.iloc[[4]]
Pando = Bolivia.iloc[[3]]

#centro, norte, oriente, sur, pando
lats = [-17.48, -16.51, -17.88,-19.3,-11.03]
lons = [-66.16,-68.13,-63.17, -65.25,-66.03]

lat1, lat2, lat3, lat4, lat5 = -17.38, -16.51, -17.78,-19.3,-11.03
lon1, lon2, lon3, lon4, lon5 = -66.16,-68.13,-63.17, -65.25,-66.03
lat6 = -17.54
lat7 = -17.94

# Method 1: Define colors for specific provinces by name
province_colors = {
    'Chuquisaca': 'salmon',  # Red
    'Tarija': 'salmon',  # Teal
    'Potosi': 'salmon',  # Blue
    'Oruro': 'slategrey',  # Light Salmon
    'Cochabamba': 'slategrey',  # Mint
    'La Paz': 'khaki',  # Teal
    'Beni': 'khaki',  # Blue
    'Santa Cruz': 'palevioletred',  # Light Salmon
    'Pando': 'lightgreen',  # Mint
}

province_column = 'nom_dep'

# Map colors to each province (use default color for unmapped provinces)
# ~ Bolivia['color'] = Bolivia[province_column].map(province_colors)

# Create the plot
fig, ax = plt.subplots( 1,1, figsize=(10, 10))
# ~ fig = plt.figure(figsize=(10, 10))
# ~ ax = fig.add_subplot(1, 1, 1, projection=ccrs.PlateCarree())
ax.plot(lons, lats, 'o', color='red', ms="14", zorder=1000)
# ~ ax.add_feature(cfeature.BORDERS, edgecolor='ivory')

ax.plot([lon1, lon2], [lat1, lat2], color='black', linewidth=3.9, label = 'L1 - 390 MW') #centro-norte
ax.plot([lon1, lon4], [lat1, lat4], color='black', linewidth=1.65, label = 'L3 - 165 MW') #centro-sur
ax.plot([lon1, lon3], [lat1, lat3], color='black', linewidth=2.6, label = 'L2 - 260 MW') #centro-oriente
ax.plot([lon2, lon5], [lat2, lat5], color='black', linewidth=0, label = 'L4') #norte-pando
ax.plot([lon2, lon3], [lat2, lat3], color='black', linewidth=0.35, label = 'L5 - 35 MW') #oriente-norte
ax.plot([lon1, lon3], [lat6, lat7], color='black', linewidth=5, label = 'L6 - 500 MW') #oriente-norte
ax.tick_params(axis='both', labelsize=24)
ax.set_yticks([-10, -14, -18, -22])
ax.set_xticks([-68, -64, -60])
plt.legend(loc='upper right', fontsize = 15,frameon=False) 

# ~ Bolivia.plot(ax=ax, color=Bolivia['color'], linewidth=0, alpha=0.7,edgecolor='ivory')
Sur.plot(ax=ax, color='salmon', linewidth=5, alpha=0.7,edgecolor='grey')
Norte.plot(ax=ax, color='khaki', linewidth=5, alpha=0.7,edgecolor='grey')
Centro.plot(ax=ax, color='slategrey', linewidth=5, alpha=0.7,edgecolor='grey')
Oriente.plot(ax=ax, color='palevioletred', linewidth=5, alpha=0.7,edgecolor='grey')
Pando.plot(ax=ax, color='lightgreen', linewidth=5, alpha=0.7,edgecolor='grey')

plt.savefig('mapas.png', dpi=600, bbox_inches="tight")

plt.show()
