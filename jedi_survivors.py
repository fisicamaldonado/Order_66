import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def create_table(data):
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
    top_5_jedi = data.nlargest(5, 'Force')

    names = top_5_jedi['Name']
    force = top_5_jedi['Force']

    plt.bar(names, force)
    plt.xlabel('Name')
    plt.ylabel('Force')
    plt.title('Top 5 powerful Jedi')
    plt.xticks(rotation=45)

    plt.show()


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

formatted_table = create_table(jedi_data)
print(formatted_table)

create_histogram(pd.DataFrame(jedi_data))
