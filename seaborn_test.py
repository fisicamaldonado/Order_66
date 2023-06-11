"""
This file is created to explore some nice features of the seaborn library.
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

jedi_data = np.array([
    (1, 'Cal Kestis', 22, 82),
    (2, 'Cere Junda', 40, 78),
    (3, 'Ahsoka Tano', 32, 88),
    (4, 'Naq Med', 44, 70),
    (5, 'Kanan Jarrus', 35, 82),
    (6, 'Jocasta Nu', 70, 80),
    (7, 'Prosset Dibbs', 36, 81),
    (8, 'Bil Valen', 40, 78),
    (9, 'Masana Tide', 29, 82),
    (10, 'Quinlan Vos', 45, 91),
    (11, 'Luminara Unduli', 42, 86),
    (12, 'Grogu', 50, 85),
    (13, 'Obi-Wan Kenobi', 38, 95),
    (14, 'Yoda', 900, 100)],
    dtype=[('id', int), ('Name', 'U15'), ('age', int), ('Force', int)]
)

# Convert the jedi_data array into a DataFrame
df = pd.DataFrame(jedi_data)

# Set the Seaborn style to darkgrid
sns.set_style('darkgrid')

# Customize the color palette
custom_palette = sns.color_palette("dark")
sns.set_palette(custom_palette)

# Plot the histogram
plt.figure(figsize=(8, 6))
n, bins, patches = plt.hist(df['Force'], bins=12, facecolor='#2ab0ff', edgecolor='#e0e0e0', linewidth=0.5, alpha=0.7)

# Changing properties of each bin
n = n.astype('int') # n should be integer, otherwise it wouldn't work properly

# Accessing each bin, changing color according to height
for i in range(len(patches)):
    patches[i].set_facecolor(plt.cm.viridis(n[i]/max(n)))

plt.xlabel('Force', fontfamily='Arial', fontsize=14)
plt.ylabel('Count', fontfamily='Arial',fontsize=14)
plt.title('Distribution of Force among Jedi survivors', fontfamily='Arial', fontweight='bold',fontsize=16)
plt.show()
