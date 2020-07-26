import csv
import os
import pandas as pd 
import numpy as np 

directory='./testFiles/'
a=os.listdir(directory)
li=[]

for filename in a:
    df=pd.read_csv(directory+filename, index_col=None, header=0)
    li.append(df)

frame=pd.concat(li, axis=0, ignore_index=True)
c=df.loc[0,'Received At']

print(frame.dtypes)
print(c)
print(type(c))