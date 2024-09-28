import pandas as pd
from sklearn import linear_model

df = pd.read_csv("data.csv")

X_data = df[['Weight', 'Volume']]
y_data = df['CO2']

result_regression = linear_model.LinearRegression()
result_regression.fit(X_data.values, y_data.values)


predictedCO2 = result_regression.predict([[2300, 1300]])
predictedCO2_2 = result_regression.predict([[3300, 1300]])
predictedCO2_3 = result_regression.predict([[4300, 2700]])
reg_cfc = result_regression.coef_


print("Result of prediction: ", predictedCO2)
print("Result of prediction_2: ", predictedCO2_2)
print("Result of prediction_3: ", predictedCO2_3)
print("Result of Coefficient: ", reg_cfc)












## Predictions, Coefficient