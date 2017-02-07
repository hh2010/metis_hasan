# Import the libraries we need
import pandas as pd

# Use this function to strip white text using converters arg in pd.read_csv
def strip(text):
    try:
        return text.strip()
    except:
        return text

# Read the file into a DataFrame
csv_input = 'faculty.csv'
df = pd.read_csv(csv_input, header=1, names=["name", "degree",
"title", "email"], converters = {'name' : strip,
                                 'degree' : strip,
                                 'title' : strip,
                                 'email' : strip})

# First clean up some columns in DataFrame
deg = df['degree'].values.tolist()
title = df['title'].values.tolist()

# Clean up degree_list
# There must be a cleaner way to do this
deg_map = {'Ph': 'Ph.D.', 'Sc': 'Sc.D.', 'M.': 'MS', '0': 'NA'}
new_deg = [i.split() for i in deg]

for i in range(len(new_deg)):
    for j in new_deg[i]:
        for a,b in deg_map.items():
            if a in j: new_deg[i][new_deg[i].index(j)] = b

new_deg = map(lambda x: ", ".join(x), new_deg)

# Clean up title
title_map = {'Assis': 'Assistant Professor', 'Assoc': 'Associate Professor',
'Prof': 'Professor'}
new_title = map(lambda x: x, title)

for i in range(len(title)):
    new_title[i] = [b for a, b in title_map.iteritems() if a in new_title[i]]

map(lambda x: ", ".join(x), new_title)

# Put clean data in new DataFrame
df2 = df.copy(deep=True)
df2['title'] = new_title
df2['degree'] = new_deg
