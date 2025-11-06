import matplotlib.pyplot as plt
import numpy as np


inner_labels = ['Norte', 'Centro', 'Oriente', 'Sur', 'Pando']
inner_sizes = [618.80,1738.30,1344.30 ,639.00,65.8]
inner_colors = ['lightgrey', 'lightgrey', 'lightgrey','lightgrey','lightgrey']
hatch_patterns = ['/', '\\', '|', '-', '.']
outer_labels = ['TG','TV','Motor','Solar','Hidro',
'TG','CC','Solar','Eolica','Hidro',
'TG','TV','CC','Solar','Eolica','Hidro' ,
'TG','Motor','CC','Solar','Hidro',
'Motor']
'''
TG  #36495A
TV Black
motor #6D6F70
CC #A1140B 
solar  #FBAA1B
Eolico #8FC73E
Hidro #207653
'''
outer_sizes = [50.30,15.00,37.80,120.00,395.70,419.80,480.00,100.00,27.00,711.50,235.00,84.30,736.00,20.00,269.00,0.00,36.2,0,508.5,66.4,27.9,65.8]
outer_colors = ['#36495A','black','#6D6F70','#FBAA1B','#207653',
'#36495A','#A1140B' ,'#FBAA1B','#8FC73E','#207653',
'#36495A','black','#A1140B','#FBAA1B','#8FC73E', '#207653',
'#36495A','#6D6F70','#A1140B','#FBAA1B','#207653',
'#6D6F70']

fig, ax = plt.subplots(figsize=(10, 8))

# Plot outer pie (larger radius)
ax.pie(outer_sizes, labels=outer_labels, colors=outer_colors,
       autopct='%1.1f%%', startangle=90, radius=1.3,
       wedgeprops=dict(width=0.4, edgecolor='white'),labeldistance=1.1,textprops=dict(color="black", fontsize=16))

# Plot inner pie (smaller radius)
ax.pie(inner_sizes, labels=inner_labels, colors=inner_colors,
       autopct='%1.1f%%', startangle=90, radius=0.9,
       wedgeprops=dict(width=0.8, edgecolor='white'),  labeldistance=0.5,textprops=dict(color="w", fontsize=16), hatch=hatch_patterns)

ax.legend( outer_labels, title="Tecnología",  loc="center left", bbox_to_anchor=(1, 0, 0.5, 1), fontsize=16)
# Add a circle at the center to make it look like a donut
# ~ centre_circle = plt.Circle((0, 0), 0.5, fc='white')
# ~ fig.gca().add_artist(centre_circle)

# Equal aspect ratio ensures circular pie
ax.axis('equal')
plt.title('Alternativo 2025', fontsize=16, fontweight='bold')
plt.tight_layout()
plt.savefig('torta.svg', dpi=300, bbox_inches="tight")
