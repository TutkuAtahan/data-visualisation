import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px


df=pd.read_csv('dataset.csv')
df.head()



plt.figure(figsize=(8,10))
plt.subplot(211)
sns.barplot(data = df.groupby('job_title')['salary_in_usd'].mean().sort_values(ascending=False).reset_index(name='Average Salary').head(15),
           x='Average Salary', y='job_title')
plt.title('highest average salary')
plt.subplot(212)
sns.barplot(data = df.groupby('job_title')['salary_in_usd'].mean().sort_values(ascending=False).reset_index(name='Average Salary').tail(15),
           x='Average Salary', y='job_title')
plt.title('lowest average salary')
plt.show()