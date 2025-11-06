import matplotlib.pyplot as plt
import numpy as np
from matplotlib.gridspec import GridSpec

# # # #  año 2025
inner_labels = ['Norte', 'Centro', 'Oriente', 'Sur', 'Pando']
inner_sizes_1 = [630.8, 1746.7,1463,643.6,66.2]
inner_colors = ['lightgrey', 'lightgrey', 'lightgrey','lightgrey','lightgrey']
outer_labels = ['TG','TV','Motor','Solar','Solar Dist.','Hidro',
'TG','CC','Solar','Solar Dist.','Eolica','Hidro',
'TG','TV','CC','Solar','Solar Dist.','Eolica' ,
'TG','CC','Solar','Solar Dist.','Hidro',
'Motor','Solar Dist.']
'''
TG  #36495A
TV Black
motor #6D6F70
CC #A1140B 
solar  #FBAA1B
Eolico #8FC73E
Hidro #207653
'''
outer_sizes_1 = [50.3,15,37.8,120,12,395.7,
419.8,480,100,8.4,27,711.5,
235,84.3,736,20,18.7,369,
36.2,508.5,66.4,4.600 ,27.9,
65.8,0.4]

outer_colors = ['#36495A','black','#6D6F70','#FBAA1B','#FBAA1B','#207653',
'#36495A','#A1140B' ,'#FBAA1B','#FBAA1B','#8FC73E','#207653',
'#36495A','black','#A1140B','#FBAA1B','#FBAA1B','#8FC73E', 
'#36495A','#A1140B','#FBAA1B','#FBAA1B','#207653',
'#6D6F70','#FBAA1B']

hatch_patterns = ['', '', '', '', '.', '',
'', '', '', '.', '', '',
'', '', '', '', '.', '',
'', '', '', '.', '', 
'','.']

# # # #  año 2050
inner_labels = ['Norte', 'Centro', 'Oriente', 'Sur', 'Pando']
inner_sizes_2 = [1050.6, 2127.9,2008.8,747.4,75.8]
inner_colors = ['lightgrey', 'lightgrey', 'lightgrey','lightgrey','lightgrey']
outer_labels = ['TG','TV','Motor','Solar','Solar Dist.','Hidro',
'TG','CC','Solar','Solar Dist.','Eolica','Hidro',
'TG','TV','CC','Solar','Solar Dist.','Eolica' ,
'TG','CC','Solar','Solar Dist.','Hidro',
'Motor','Solar Dist.']
'''
TG  #36495A
TV Black
motor #6D6F70
CC #A1140B 
solar  #FBAA1B
Eolico #8FC73E
Hidro #207653
'''
outer_sizes_2 = [87.6,15,37.8,120,275.5,514.7,
419.8,480,298,191.6,27,711.5,
371,84.3,736,20,428.5,369,
38,508.5,66.4,106.5,27.9,
65.8,10]

outer_colors = ['#36495A','black','#6D6F70','#FBAA1B','#FBAA1B','#207653',
'#36495A','#A1140B' ,'#FBAA1B','#FBAA1B','#8FC73E','#207653',
'#36495A','black','#A1140B','#FBAA1B','#FBAA1B','#8FC73E', 
'#36495A','#A1140B','#FBAA1B','#FBAA1B','#207653',
'#6D6F70','#FBAA1B']

hatch_patterns = ['', '', '', '', '/', '',
'', '', '', '/', '', '',
'', '', '', '', '/', '',
'', '', '', '/', '', 
'','/']

# ~ fig, (ax1,ax2) = plt.subplots(1,2,figsize=(20, 15))
fig = plt.figure(figsize=(20, 12))
gs = GridSpec(1, 2, figure=fig, width_ratios=[1,1.149])

# Plot outer pie (larger radius)
ax1 = fig.add_subplot(gs[0, 0])

ax1.pie(outer_sizes_1, labels=outer_labels, colors=outer_colors,
       autopct='%1.1f%%', startangle=90, radius=1.3,
       wedgeprops=dict(width=0.4, edgecolor='white'),labeldistance=1.1,textprops=dict(color="black", fontsize=16), hatch=hatch_patterns)

# Plot inner pie (smaller radius)
ax1.pie(inner_sizes_1, labels=inner_labels, colors=inner_colors,
       autopct='%1.1f%%', startangle=90, radius=0.9,
       wedgeprops=dict(width=0.8, edgecolor='white'),  labeldistance=0.5,textprops=dict(color="w", fontsize=16))
       

# Plot outer pie (larger radius)
ax2 = fig.add_subplot(gs[0, 1])

ax2.pie(outer_sizes_2, labels=outer_labels, colors=outer_colors,
       autopct='%1.1f%%', startangle=90, radius=1.3,
       wedgeprops=dict(width=0.4, edgecolor='white'),labeldistance=1.1,textprops=dict(color="black", fontsize=16), hatch=hatch_patterns)

# Plot inner pie (smaller radius)
ax2.pie(inner_sizes_2, labels=inner_labels, colors=inner_colors,
       autopct='%1.1f%%', startangle=90, radius=0.9,
       wedgeprops=dict(width=0.8, edgecolor='white'),  labeldistance=0.5,textprops=dict(color="w", fontsize=16))

ax2.legend( outer_labels, title="Tecnología",  loc="center left", bbox_to_anchor=(1, 0, 0.5, 1), fontsize=16)
# Add a circle at the center to make it look like a donut
# ~ centre_circle = plt.Circle((0, 0), 0.5, fc='white')
# ~ fig.gca().add_artist(centre_circle)

# Equal aspect ratio ensures circular pie
# ~ ax2.axis('equal')

# ~ ax1.axis('equal')
ax1.set_title('Escenario Tendencial \n 2025 (4550 MW)', fontsize=24, fontweight='bold')
ax2.set_title('Escenario Tendencial \n 2050 (6010 MW)', fontsize=24, fontweight='bold')
plt.tight_layout()
plt.savefig('torta.svg', dpi=300, bbox_inches="tight")
