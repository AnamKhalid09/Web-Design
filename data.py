# import dependency
import pandas as pd

# Import cities.csv using pandas and convert into html file
df = pd.read_csv('Resources/cities.csv')
# Exporting html file to data.html
df.to_html('data.html', index=False)
table = df.to_html()
print(table)
