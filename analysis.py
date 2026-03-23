import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("databreachproject.csv.zip")

# CLEANING
# Fix column names (remove spaces)
df.columns = df.columns.str.strip()

# Remove first garbage row
df = df.iloc[1:]

# Drop unnecessary columns
df = df.drop(columns=[
    'alternative name',
    'story',
    'interesting story',
    'Unnamed: 11',
    '1st source link',
    '2nd source link',
    'ID'
], errors='ignore')

# Fill missing values
df.fillna("Unknown", inplace=True)

# Convert numeric columns
df['records lost'] = pd.to_numeric(df['records lost'], errors='coerce')
df['year'] = pd.to_numeric(df['year'], errors='coerce')

# ANALYSIS
print("\nTop Attack Methods:\n")
print(df['method'].value_counts().head(10))

print("\nTop Sectors:\n")
print(df['sector'].value_counts().head(10))

print("\nData Sensitivity:\n")
print(df['data sensitivity'].value_counts())

print("\nYear-wise Breaches:\n")
print(df['year'].value_counts().sort_index())

# VISUALIZATION
# Attack methods
plt.figure()
sns.countplot(y='method', data=df, order=df['method'].value_counts().iloc[:10].index)
plt.title("Top Cyber Attack Methods")
plt.savefig("attack_methods.png")
plt.show()

# Sectors
plt.figure()
sns.countplot(y='sector', data=df, order=df['sector'].value_counts().iloc[:10].index)
plt.title("Most Targeted Sectors")
plt.savefig("sectors.png")
plt.show()

# Year trend
plt.figure()
sns.countplot(x='year', data=df)
plt.xticks(rotation=45)
plt.title("Cyber Breaches Over Years")
plt.savefig("year_trend.png")
plt.show()