# import all library
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import MinMaxScaler

data_df = pd.read_csv("diabetes.csv")

# print(data_df.head()) # shows all headers

# print(data_df.info()) # shows general info of dataset

# print(data_df.shape) # shows y,x value

# print(data_df.describe()) # only applicable to numerical values

# if no null don't need data inputation 
# print(data_df.isnull().sum()) # shows num of nulls in dataset

"""
DATA EXPLORATION
------------------------------------------------------------------------------------------------------------------
create a bar graph to see the distribution of the variable
"""
# print(data_df['Outcome'].value_counts())
# outcome_unique = data_df['Outcome'].value_counts().index
# outcome_unique = [str(u) for u in outcome_unique]
# outcome_cnt = data_df['Outcome'].value_counts()
# 
# sns.barplot(data=data_df, x=outcome_unique, y=outcome_cnt)
# plt.show()

# show distubution of variables by outcome
# data_df.groupby("Outcome").hist()
# plt.show()

# sns.boxplot(data=data_df['Pregnancies'])
# plt.show()

# Only for numerical values
# decide columns to remove is above .7 
# corr = data_df.corr()
# sns.heatmap(data=corr, annot=True, fmt=".2f")
# plt.show()


