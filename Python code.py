#!/usr/bin/env python
# coding: utf-8

# In[2]:


import zipfile
import os

# Unzipping the dataset
with zipfile.ZipFile("C:/Users/Admin/Downloads/netflix_data.zip", 'r') as zip_ref:
    zip_ref.extractall('Netflix_shows_movies')

# List the contents of the extracted directory
extracted_files = os.listdir('Netflix_shows_movies')
print("Extracted files:", extracted_files)

# Renaming the extracted file (assuming it's a CSV file and finding the correct file)
os.rename(f'Netflix_shows_movies/netflix_data.csv', 'Netflix_shows_movies/Netflix_shows_movies.csv')




# In[21]:


import pandas as pd

# Load the dataset
df = pd.read_csv('Netflix_shows_movies/Netflix_shows_movies.csv')
#View first 5 rows of the data set
df.head()


# In[15]:


# Display missing values
print(df.isnull().sum())

# Fill missing values with mode
df['director'].fillna(df['director'].mode()[0], inplace=True)
df['cast'].fillna(df['cast'].mode()[0], inplace=True)
df['country'].fillna(df['country'].mode()[0], inplace=True)
df['date_added'].fillna(df['date_added'].mode()[0], inplace=True)
df['rating'].fillna(df['rating'].mode()[0], inplace=True)

# Save cleaned data
df.to_csv('Netflix_shows_movies/Netflix_shows_movies_cleaned.csv', index=False)


# In[28]:


from sklearn.preprocessing import LabelEncoder
import seaborn as sns
import matplotlib.pyplot as plt

# Identify non-numeric columns
non_numeric_columns = df.select_dtypes(exclude=['number']).columns

# Initialize the label encoder
label_encoders = {}

# Encode non-numeric columns(assign numbers to non numeric values)
for column in non_numeric_columns:
    label_encoders[column] = LabelEncoder()
    df[column] = label_encoders[column].fit_transform(df[column].astype(str))

    
print(df.describe())

# Calculate the correlation matrix
correlation_matrix = df.corr()

# Display the correlation heatmap
plt.figure(figsize=(12, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
plt.title('Correlation Heatmap')
plt.show()




# In[22]:


import seaborn as sns
import matplotlib.pyplot as plt

# Most watched genres
plt.figure(figsize=(10, 6))
sns.countplot(y='type', data=df, order=df['type'].value_counts().index)
plt.title('Most Watched Genres')
plt.xlabel('Count')
plt.ylabel('Genre')
plt.show()

# Ratings distribution
plt.figure(figsize=(10, 6))
sns.histplot(df['rating'], bins=20, kde=True)
plt.title('Ratings Distribution')
plt.xlabel('Rating')
plt.ylabel('Frequency')
plt.show()


# In[ ]:




