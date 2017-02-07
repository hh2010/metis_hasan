# Import pandas, regex, and cleaned DataFrame
import pandas as pd
import re
from advanced_python_clean import df2

# Calculate Number of Degrees for Question #1
deg_list = ["Ph.D.", "MD", "MPH", "B.S.", "MS", "JD", "MA", 'Sc.D.']

for i in deg_list:
    print (i, sum(1 for j in df2['degree'] if i in j))

# Calculate Number of Titles for Question #2
a = sum(1 for i in df2['title'] if "Associate" in i)
b = sum(1 for i in df2['title'] if "Assistant" in i)
c = sum(1 for i in df2['title'])

# The output below is working in interpreter but not console
print "Professor", c - b - a, '\n', "Assistant Professor", a, \
'\n', "Associate Professor", b

# Put all e-mail addresses in a list for Question #3
print "\n".join(sorted(list(df2['email'])))

# Find unique email domains for Question #4
domain_set = set()
for i in sorted(list(df2['email'])):
    domain_set.add(re.search("@[\w.]+", i).group())

for i in domain_set: print i
