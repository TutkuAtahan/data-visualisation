import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px


data=pd.read_csv('dataset.csv')
data.head()



grouped_data = data.groupby(['job_category','job_title'])['salary_in_usd'].mean().reset_index()
fig = px.bar(grouped_data,
            x='job_title',
            y='salary_in_usd',
            color='job_category',
            title='salary mean of each job  title',
            height=800,
            width=1000)
fig.update_layout(xaxis_title = 'job title', yaxis_title='mean salary in usd')
fig.show()