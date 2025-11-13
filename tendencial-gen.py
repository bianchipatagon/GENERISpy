import matplotlib.pyplot as plt
import numpy as np
from matplotlib.gridspec import GridSpec

# # # #  año 2025 sin dist
inner_labels = ['Norte', 'Centro', 'Oriente', 'Sur', 'Pando']
inner_sizes_1 = [2124.5,2731.3,4542.7,1903.9,82.1]
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
outer_sizes_1 = [9.6,15.6,67.0,209.9,0.5,1821.8,
0.0,255.7,51.3,0.4,75.1,2348.9,
0.0,246.0,2983.3,41.8,0.8,1270.7,
0.0,1629.9,138.8,0.2,135.0,
82,0]

outer_colors = ['#36495A','black','#6D6F70','#FBAA1B','#FBAA1B','#207653',
'#36495A','#A1140B' ,'#FBAA1B','#FBAA1B','#8FC73E','#207653',
'#36495A','black','#A1140B','#FBAA1B','#FBAA1B','#8FC73E', 
'#36495A','#A1140B','#FBAA1B','#FBAA1B','#207653',
'#6D6F70','#FBAA1B']

# # # #  año 2050 sin dist
inner_labels = ['Norte', 'Centro', 'Oriente', 'Sur', 'Pando']
inner_sizes_2 = [3135.5,6894.5,8371.3,3502.8,145.9]
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
outer_sizes_2 = [72.8,43.8,276.9,250.8,49,2491.3,
683.2,2544.3,622.7,36.3,88.9,2955.3,
2299.6,246.0,4513.2,41.8,68.4,1270.7,
145.8,3083.2,138.8,20.9,135.0,
145.9,1.4]

outer_colors = ['#36495A','black','#6D6F70','#FBAA1B','#FBAA1B','#207653',
'#36495A','#A1140B' ,'#FBAA1B','#FBAA1B','#8FC73E','#207653',
'#36495A','black','#A1140B','#FBAA1B','#FBAA1B','#8FC73E', 
'#36495A','#A1140B','#FBAA1B','#FBAA1B','#207653',
'#6D6F70','#FBAA1B']

# # # #  año 2050 sin dist
inner_labels = ['Norte', 'Centro', 'Oriente', 'Sur', 'Pando']
inner_sizes_3 = [3536.1,6471.0,8442.0,3499.4,146.1]
inner_colors = ['lightgrey', 'lightgrey', 'lightgrey','lightgrey','lightgrey']
outer_labels_3 = ['TG','TV','Motor','Solar','Solar Dist.','Hidro',
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
outer_sizes_3 = [69.3,34.4,221.8,228.0,491.4,2491.3,
623.7,1944.0,497.3,361.9,88.9,2955.3,
1706.7,228.8,4510.8,41.8,683.2,1270.7,
128.0,2878.6,138.8,210.5,135.0,
132.1,13.9]

outer_colors_3 = ['#36495A','black','#6D6F70','#FBAA1B','#FBAA1B','#207653',
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
fig = plt.figure(figsize=(24, 12))
gs = GridSpec(1, 3, figure=fig, width_ratios=[1,1.393,1.393])

# 2025 sin dist
ax1 = fig.add_subplot(gs[0, 0])
ax1.pie(outer_sizes_1, labels=outer_labels, colors=outer_colors,
       autopct='%1.1f%%', startangle=90, radius=1.3,
       wedgeprops=dict(width=0.4, edgecolor='white'),labeldistance=1.1,textprops=dict(color="black", fontsize=16), hatch=hatch_patterns)
ax1.pie(inner_sizes_1, labels=inner_labels, colors=inner_colors,
       autopct='%1.1f%%', startangle=90, radius=0.9,
       wedgeprops=dict(width=0.8, edgecolor='white'),  labeldistance=0.5,textprops=dict(color="w", fontsize=16))
       
# 2050 sin dist
ax2 = fig.add_subplot(gs[0, 1])
ax2.pie(outer_sizes_2, labels=outer_labels, colors=outer_colors,
       autopct='%1.1f%%', startangle=90, radius=1.3,
       wedgeprops=dict(width=0.4, edgecolor='white'),labeldistance=1.1,textprops=dict(color="black", fontsize=16), hatch=hatch_patterns)
ax2.pie(inner_sizes_2, labels=inner_labels, colors=inner_colors,
       autopct='%1.1f%%', startangle=90, radius=0.9,
       wedgeprops=dict(width=0.8, edgecolor='white'),  labeldistance=0.5,textprops=dict(color="w", fontsize=16))

# 2050 con dist
ax3 = fig.add_subplot(gs[0, 2])
ax3.pie(outer_sizes_3, labels=outer_labels_3, colors=outer_colors_3,
       autopct='%1.1f%%', startangle=90, radius=1.3,
       wedgeprops=dict(width=0.4, edgecolor='white'),labeldistance=1.1,textprops=dict(color="black", fontsize=16), hatch=hatch_patterns)
ax3.pie(inner_sizes_3, labels=inner_labels, colors=inner_colors,
       autopct='%1.1f%%', startangle=90, radius=0.9,
       wedgeprops=dict(width=0.8, edgecolor='white'),  labeldistance=0.5,textprops=dict(color="w", fontsize=16))
ax3.legend( outer_labels_3, title="Tecnología",  loc="center left", bbox_to_anchor=(1, 0, 0.5, 1), fontsize=16)
# Add a circle at the center to make it look like a donut
# ~ centre_circle = plt.Circle((0, 0), 0.5, fc='white')
# ~ fig.gca().add_artist(centre_circle)

# Equal aspect ratio ensures circular pie
# ~ ax2.axis('equal')

# ~ ax1.axis('equal')
ax1.set_title('Escenario Tendencial \n 2025 (11384 GWh)', fontsize=24, fontweight='bold')
ax2.set_title('Escenario Tendencial \n 2050 (22225 GWh)', fontsize=24, fontweight='bold')
ax3.set_title('Escenario Tendencial \n +Distribuida \n 2050 (22094 GWh)', fontsize=24, fontweight='bold')

plt.tight_layout()
plt.savefig('tendencialGen.svg', dpi=300, bbox_inches="tight")
