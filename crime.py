import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
dataset=pd.read_csv(r'C:\Users\santosh\Downloads\PAASBAAN-crime-prediction-master\data.csv')
data=pd.read_csv(r'C:\Users\santosh\Downloads\PAASBAAN-crime-prediction-master\data.csv')
print(dataset.head())
for col in data:
    print (type(data[col][1]))
data['timestamp'] = pd.to_datetime(data['timestamp'])
data['timestamp'] = pd.to_datetime(data['timestamp'], format = '%d/%m/%Y %H:%M:%S')
data['timestamp']
column_1 = data.ix[:,0]

db=pd.DataFrame({"year": column_1.dt.year,
              "month": column_1.dt.month,
              "day": column_1.dt.day,
              "hour": column_1.dt.hour,
              "dayofyear": column_1.dt.dayofyear,
              "week": column_1.dt.week,
              "weekofyear": column_1.dt.weekofyear,
              "dayofweek": column_1.dt.dayofweek,
              "weekday": column_1.dt.weekday,
              "quarter": column_1.dt.quarter,
             })
dataset1=dataset.drop('timestamp',axis=1)

data1=pd.concat([db,dataset1],axis=1)
data1.info()
data1.dropna(inplace=True)
data1.head()

sns.pairplot(data1,hue='act363')