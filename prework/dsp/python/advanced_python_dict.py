# Import pandas and the cleaned up DataFrame
import pandas
from advanced_python_clean import df2

# Pull the columns into lists
names = list(df2['name'])
degrees = list(df2['degree'])
title = list(df2['title'])
email = list(df2['email'])

# Split names column into first and last name
splitnames = [i.split() for i in names]
firstnames = [i[0] for i in splitnames]
lastnames = [i[-1] for i in splitnames]

# Check that all lists match in length
len(names) == len(degrees) == len(title) == len(email) == len(lastnames)

# Create the dictionary and print out 3 key, value pairs for Question #7
professor_dict = { x: [i, j, k] for x, i, j, k in
                                        zip(lastnames, degrees, title, email)}

print {k: professor_dict[k] for k in professor_dict.keys()[:3]}

# Create the dictionary and print out 3 key, value pairs for Question #8
professor_dict2 = {(x, y) : [i, j, k] for x, y, i, j, k in
                             zip(lastnames, firstnames, degrees, title, email)}

print {k: professor_dict2[k] for k in professor_dict2.keys()[:3]}

# Print in alphabetical order by last name for Question #9
for x in sorted(professor_dict2):
    print x, professor_dict2[x]
