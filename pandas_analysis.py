# examples of how to do pandas analysis on dataset

import pandas as pd

# read CSV file from repo, convert date from string to datetime objects, set dates as index.
rainfall = pd.read_csv('https://github.com/davemcphee/LCRARainFallanalysis/blob/master/data/LadyBirdLakeRainfallWithZeroValues.csv?raw=true', parse_dates=['datetime'], index_col=['datetime'])

# calculating various percentiles
rainfall['inches'].describe(percentiles=[0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.9, 0.95, 0.99, 1.0])

# samples are taken roughly 15 mins apart, but let's cleanly resample into hours
# Im resampling the original data, including zeroes. 
hours = rainfall.resample('60Min', how='sum')

# now we remove any hours that had a total of 0.0 inches of rainfall, leaving us with data on 
# rain falls per hour, if any rain fell that hour.
nozeroes = hours[hours['inches'] > 0]

# .describe() returns lots of stats on a dataset, but we can ask it to provide more percentiles 
# if needed, like this:
nozeroes['inches'].describe(percentiles=[0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.9, 0.925, 0.95, 0.975, 0.99, 1.0])

''' output looks like this:
count    3182.000000
mean        0.111292
std         0.242054
min         0.010000
10%         0.010000
20%         0.010000
30%         0.010000
40%         0.020000
50%         0.030000
60%         0.050000
90%         0.260000
92.5%       0.340000
95%         0.480000
97.5%       0.750000
99%         1.273800
100%        3.490000
max         3.490000
Name: inches, dtype: float64'''

