import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px


df=pd.read_csv('dataset.csv')
df.head()


fig = px.choropleth(df.groupby('employee_residence')['salary_in_usd'].mean().reset_index(name='Average Salary'), 
                    locations='employee_residence',
                    locationmode='country names',
                    color= 'Average Salary',
                    hover_name='employee_residence',
                    color_continuous_scale='plasma')
fig.update_geos(projection_type="natural earth", showcoastlines=True)
fig.update_layout(title_text='World Map - Average Salary')
fig.show()
