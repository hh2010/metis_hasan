import pandas as pd

# Read the file into a DataFrame
df = pd.read_csv('football.csv')

# Create 'Diff' column, sort it, and output
df['Diff'] = abs(df['Goals'] - df['Goals Allowed'])
df.sort_values(by=['Diff'], inplace=True)
print df.iloc[0]
