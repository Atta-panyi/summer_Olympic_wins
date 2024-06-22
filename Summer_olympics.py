import pandas as pd
import matplotlib.pyplot as plt

# data
df = pd.read_csv("summer.csv")
# Understanding the data
print(df.head(3))
print(df.tail(5))
print(df.shape)
print(df.dtypes)
print(df.info())
print(df.columns)

# Data Analysis
yearly_medals = df.groupby('Year').size()

# Calculate the total number of participating countries for each year
participating_countries_per_year = df.groupby('Year')['Country'].nunique()
# Combined plot for total medals, participating countries, and events
plt.figure(figsize=(14, 8))

# Calculate the number of medals obtained by year for each country
medals_per_year_country = df.groupby(['Year', 'Country']).size().unstack(fill_value=0)
print(yearly_medals)

country_medals = df.groupby('Country').size().sort_values(ascending=False)
print(country_medals)

medal_counts = df['Medal'].value_counts()
print(medal_counts)

# Data Visualization
# Plot the total number of participating countries for each year
plt.figure(figsize=(12, 6))
participating_countries_per_year.plot(kind='bar', color='green')
plt.title('Total Number of Participating Countries per Year')
plt.xlabel('Year')
plt.ylabel('Number of Countries')
plt.xticks(rotation=45)
plt.show()

# Plot the number of medals obtained by year for each country
medals_per_year_country.plot(kind='bar', stacked=True, figsize=(14, 8), colormap='tab20')
plt.title('Number of Medals Obtained by Year for Each Country')
plt.xlabel('Year')
plt.ylabel('Number of Medals')
plt.legend(title='Country', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.xticks(rotation=45)
plt.show()
yearly_medals.plot(kind='line', title='Total Medals per Year')
plt.xlabel('Year')
plt.ylabel('Number of Medals')
plt.show()

top_countries = country_medals.head(10)
top_countries.plot(kind='bar', title='Top 10 Countries by Medal Count')
plt.xlabel('Country')
plt.ylabel('Number of Medals')
plt.show()

medal_counts.plot(kind='pie', autopct='%1.1f%%', title='Medal Distribution')
plt.ylabel('')
plt.show()

top_countries.plot(kind='pie', autopct='%1.1f%%', title='Medal Distribution for top 10 country')
plt.ylabel('')
plt.show()
