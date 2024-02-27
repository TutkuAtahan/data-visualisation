import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# import os
# for dirname, _, filenames in os.walk('dataset.csv'):
#     for filename in filenames:
#         print(os.path.join(dirname, filename))

data=pd.read_csv('dataset.csv')
data.head()

count_cat = data.groupby(['work_year','job_category']).size().reset_index(name='size')
count_salary = data.groupby(['work_year','job_category'])['salary_in_usd'].mean().reset_index(name='salary_mean')
count_salary['salary_mean'] = round(count_salary['salary_mean']/1000,2)
count_salary['salary_mean'] = count_salary['salary_mean'].astype('str') + "  "+ "Thousand USD"
grouped_data = pd.merge(count_cat,count_salary,on=['work_year','job_category'])

fig = px.scatter(
    grouped_data,
    x='work_year',
    y='job_category',
    size='size',
    color='job_category',
    hover_name='salary_mean',
    size_max=50,
    width=1000,
    height=600
)
fig.show()