from data.api_call import *

df = get_dataframe()

print(df.gravite.value_counts())

# Filter the DataFrame for each type of "gravite"
gravite_blesse_leger = df[df['gravite'] == 'Blessé léger']
gravite_hospitalises = df[df['gravite'] == 'Hospitalisés']
gravite_tues = df[df['gravite'] == 'Tués']

# Output the filtered DataFrames
print("Accidents with 'Blessé léger' gravite:")
print(gravite_blesse_leger)

print("\nAccidents with 'Hospitalisés' gravite:")
print(gravite_hospitalises)

print("\nAccidents with 'Tués' gravite:")
print(gravite_tues)