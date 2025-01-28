# Q.4 Read a csv file and display its first five rows.
# Note-: Download dataset from https://www.kaggle.com/datasets/uciml/iris)
# Q.5 From the csv file (uploaded in the Q.4) delete row 4, and delete column 3. Display the
# result.

import pandas as pd
df=pd.read_csv('/Users/yashagarwal/Downloads/archive/Iris.csv')

print(df.head())

print(df.drop(df.columns[[1,4]],axis=1))

print(df.drop(df.columns[[1,4]],axis=1,inplace=True))

