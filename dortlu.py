import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px


data=pd.read_csv('dataset.csv')
data.head()



fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(12, 10))


sns.lineplot(data=data, x='work_year', y='salary_in_usd', hue='company_size', ax=axes[0, 0])
axes[0, 0].set_title('Salary vs Work Year (Company Size)')


sns.lineplot(data=data, x='work_year', y='salary_in_usd', hue='work_setting', ax=axes[0, 1])
axes[0, 1].set_title('Salary vs Work Year (Work Setting)')

sns.lineplot(data=data, x='work_year', y='salary_in_usd', hue='employment_type', ax=axes[1, 0])
axes[1, 0].set_title('Salary vs Work Year (Employment Type)')

sns.lineplot(data=data, x='work_year', y='salary_in_usd', hue='experience_level', ax=axes[1, 1])
axes[1, 1].set_title('Salary vs Work Year (Experience Level)')

for ax in axes.flat:
    ax.set_xticks(data['work_year'].unique())  
    ax.set_xticklabels(data['work_year'].unique(), rotation=45)  

plt.tight_layout()


plt.show()
