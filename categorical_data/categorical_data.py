import pandas as pd
from sklearn import linear_model


cars = pd.read_csv('data.csv')
ohe_cars = pd.get_dummies(cars[['Car']], dtype=int)

colors = pd.DataFrame({'color': ['blue', 'red', 'green']})
dummies = pd.get_dummies(colors, drop_first=True, dtype=int)
dummies['color'] = colors['color']

print('This is dummy_colors: '"\n", dummies)
# print('This is colors: ', colors)

X = pd.concat([cars[['Volume', 'Weight']], ohe_cars], axis=1)
y = cars['CO2']

regr = linear_model.LinearRegression()
regr.fit(X.values, y.values)

predictCO2 = regr.predict(
    [[2300, 1300, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0]])


# print(ohe_cars.to_string())
# print(predictCO2)
