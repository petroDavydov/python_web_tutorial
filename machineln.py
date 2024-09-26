import numpy as np
from scipy import stats

speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]

mean_res = np.mean(speed)

median_res = np.median(speed)

mode_res = stats.mode(speed)

print(mean_res)
print(median_res)
print(mode_res)
