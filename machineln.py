import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

# speed = [99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86]
# speed_wide = [32, 111, 138, 28, 59, 77, 97]
# speed_middle = [86, 87, 88, 86, 87, 85, 86]

# speed_variance = speed = [32, 111, 138, 28, 59, 77, 97]


# mean_res = np.mean(speed)

# median_res = np.median(speed)

# mode_res = stats.mode(speed)

# std_res = np.std(speed_wide)
# std_res_middle = np.std(speed_middle)

# variance_res = np.var(speed_variance)

# print(mean_res)
# print(median_res)
# print(mode_res)
# print(std_res)
# print(std_res_middle)
# print("Variance(dispersia): ", variance_res)
# # ------------------------------------------------

# ages = [5, 31, 43, 48, 50, 41, 7, 11, 15, 39,
#         80, 82, 32, 2, 8, 6, 25, 36, 27, 61, 31]

# age_75 = np.percentile(ages, 75)
# age_20 = np.percentile(ages, 20)

# print("Control 75%: ", age_75)
# print("Control 20%: ", age_20)
# -------------------------------------------------

# res_bds = np.random.uniform(0.5, 3.0, 150)
# # print('Array with 250 float 0 --> 5: '"\n", res_bds)

# res_bds = np.random.uniform(0.1, 5.0, 100000)


# plt.hist(res_bds, 100)
# plt.show()
# -------------------------------------------

# res_normal_dd = np.random.normal(5.0, 1.0, 100000)

# plt.hist(res_normal_dd, 1000)
# plt.show()
# -------------------------------------
# Scatter Plot


# car_age = [5, 7, 8, 7, 2, 17, 2, 9, 4, 11, 12, 9, 6]
# car_speed = [99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86]

# plt.title("Car INFO")
# plt.xlabel("CAR AGE")
# plt.ylabel("CAR SPEED")

# plt.scatter(car_age, car_speed)
# plt.show()
# --------------------------------

# x_red = np.random.normal(5.0, 1.0, 1000)
# y = np.random.normal(10.0, 2.0, 1000)

# plt.scatter(x_red, y)
# plt.show()
# ----------------------------------------------?
# FOR AGE
# x_age = [5, 7, 8, 7, 2, 17, 2, 9, 4, 11, 12, 9, 6]
# y_speed = [99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86]

# slope, intercept, r, p, std_err = stats.linregress(x_age, y_speed)


# def my_result(res):
#     return slope * res + intercept


# res_model = list(map(my_result, x_age))

# plt.scatter(x_age, y_speed)
# plt.plot(x_age, res_model)
# plt.show()
# ---------------------------------------------
# FOR SPEED (BUT QUESTION IS OPEN.....)

# x_age = [5, 7, 8, 7, 2, 17, 2, 9, 4, 11, 12, 9, 6]
# y_speed = [99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86]

# slope, intercept, r, p, std_err = stats.linregress(x_age, y_speed)


# def my_result(res):
#     return slope * res + intercept


# res_model = list(map(my_result, y_speed))

# plt.scatter(y_speed, y_speed)
# plt.plot(y_speed, res_model)
# plt.show()
# -----------------------------------

# Polymonial Regression

x_hour = [1, 2, 3, 5, 6, 7, 8, 9, 10, 12, 13, 14, 15, 16, 18, 19, 21, 22, 23, 00]
y_speed = [100, 90, 80, 60, 60, 55, 60, 65, 70, 70, 75, 76, 78, 79, 90, 99, 99, 100, 120, 120]


my_model = np.poly1d(np.polyfit(x_hour, y_speed, 3))

my_line = np.linspace(1, 24, 100)


plt.scatter(x_hour, y_speed)
plt.plot(my_line, my_model(my_line), color = 'r')
plt.show()
