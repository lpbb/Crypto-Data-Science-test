import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


punks_url = 'https://raw.githubusercontent.com/Omni-Analytics-Group/eth-data-science-course/master/courses/Module%201/punks.csv'
df_punks = pd.read_csv(punks_url, encoding='unicode_escape')

# get a first look to the data

# print(df_punks.head())
# print(df_punks.tail())
# print(df_punks.info())
# print(df_punks.describe(include='all'))

# first plots

# sns.scatterplot(x=df_punks.Crypto, y=df_punks.USD).set(title='USD vs. Crypto (ETH)')
# sns.scatterplot(x=df_punks.Crypto, y=df_punks.USD, hue = df_punks.Type).set(title='USD vs. Crypto (ETH)')
# plt.show()

# Creating a New Variable

df_punks['Ratio of Currency'] = df_punks['USD']/df_punks['Crypto']
# print(df_punks['Ratio of Currency'].describe())

# histogram

# sns.histplot(x=df_punks.Crypto, binwidth=1.5, element="poly").set(title='Histogram of Crypto') # binwidth is the length of each rectangular bar
# plt.show()

# most expensive punk

print(df_punks.loc[df_punks.Crypto.idxmax()])