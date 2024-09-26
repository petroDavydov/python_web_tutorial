import numpy as np
from scipy import stats

speed = [99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86]
speed_wide = [32, 111, 138, 28, 59, 77, 97]
speed_middle = [86, 87, 88, 86, 87, 85, 86]

speed_variance = speed = [32, 111, 138, 28, 59, 77, 97]


mean_res = np.mean(speed)

median_res = np.median(speed)

mode_res = stats.mode(speed)

std_res = np.std(speed_wide)
std_res_middle = np.std(speed_middle)

variance_res = np.var(speed_variance)

print(mean_res)
print(median_res)
print(mode_res)
print(std_res)
print(std_res_middle)
print("Variance(dispersia): ", variance_res)
# ------------------------------------------------

