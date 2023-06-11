"""
order_66 is a project that showcases a list of Jedi who survived Order 66.
We use numpy, pandas and matplotlib libraries.
It provides a formatted table of the Jedi survivors and a histogram of the top 5 most powerful Jedi.
"""

import numpy as np #used to create an array for the dataset.
import pandas as pd #the standard for tables.
import matplotlib.pyplot as plt #to create a histogram.


def create_table(data):
    '''
    Creates a table using pandas from the data loaded from the array, jedi_data.
    '''
    jedi_table = pd.DataFrame(data)
    table_string = jedi_table.to_string(index=False)

    title = "Jedi Survivors - Order 66"
    formatted_title = f"\033[1;34m{title.center(len(table_string.splitlines()[0]))}\033[0m\n\n"
    formatted_table = formatted_title

    header_line = table_string.splitlines()[0]
    separator_line = "-" * len(header_line)

    formatted_table += header_line + "\n"  # Header line
    formatted_table += separator_line + "\n"  # Separator line

    formatted_table += "\n".join(table_string.splitlines()[1:])

    return formatted_table


def create_histogram(data):
    '''
    Creates a histogram using matplotlib, from the jedi_data array.
    '''
    top_5_jedi = data.nlargest(5, 'Force')
    #Extracting top 5 jedi survivors.
    names = top_5_jedi['Name']
    force = top_5_jedi['Force']
    #Defining title and labels for the histogram.
    x_label = 'Name'
    y_label = 'Force'
    histogram_title = 'Top 5 powerful Jedi'
    plt.bar(names, force)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(histogram_title)
    plt.xticks(rotation=45) #rotating names in the x axis.

    plt.show()

#dataset of jedi survivors
jedi_data = np.array([
    # (id, Name, age, Force)
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

order66_table = create_table(jedi_data)
print(order66_table)

create_histogram(pd.DataFrame(jedi_data))
