# Scale/standartization metho: z=(x-u)/s
# Where z is the new value, x is the original value, u is the mean and s is the standard deviation.

import pandas as pd
from sklearn import linear_model
from sklearn.preprocessing import StandardScaler
scale = StandardScaler()


df = pd.read_csv("datascale.csv")

data_WV = df[['Weight', 'Volume']]

scaledX = scale.fit_transform(data_WV)

print('This is data scale from Weight & Volume: '"\n", scaledX)
