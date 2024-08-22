#import pandas as pd
#df = pd.read_csv('GoogleApps.csv')
#print (df['Content Rating'].value_counts())
#temp = (df['Content Rating'].value_counts())
#print(temp['Everyone'])
#print(temp['Everyone 10+'])
#dil=(temp['Everyone']/temp['Everyone 10+'])
#print(round(dil,2))

#print(df.groupby(by = 'Content Rating')['Size'].agg(['min', 'max', 'mean']))
#print(df['Category'].value_counts()['BUSINESS'])

#temp = (df[Re'].value_counts())

#print(round(df.groupby(by='Type')['Rating'].mean(),2))

#df['Raying']

import pandas as pd
import matplotlib.pyplot as plt

s=pd.Series(data = [10, 5, 15, 20, 10], index= [1, 2, 3, 4, 5])
s.plot()
plt.show




