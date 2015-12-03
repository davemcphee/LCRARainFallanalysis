# LCRA RainFall Analysis
Using LCRA rain data, create a more useful Impervious Coverage policy for Austin

Some pandas info on the rainfall dataset. rainfalls contains 0 values, sample does not. probably pointless to calculate rainfall percentiles with 0 values
```
In [27]: rainfall['inches'].describe()
Out[27]:
count    342367.000000
mean          0.001034
std           0.017036
min           0.000000
25%           0.000000
50%           0.000000
75%           0.000000
max           2.450000
Name: inches, dtype: float64

In [28]: sample['inches'].describe()
Out[28]:
count    6819.000000
mean        0.051933
std         0.109225
min         0.010000
25%         0.010000
50%         0.020000
75%         0.040000
max         2.450000
Name: inches, dtype: float64

In [29]: sample['inches'].describe(percentiles=[0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.
Out[29]: .9, 0.95, 0.99, 1.0])
count    6819.000000
mean        0.051933
std         0.109225
min         0.010000
10%         0.010000
20%         0.010000
30%         0.010000
40%         0.010000
50%         0.020000
60%         0.020000
70%         0.040000
80%         0.060000
90%         0.110000
95%         0.220000
99%         0.540000
100%        2.450000
max         2.450000
Name: inches, dtype: float64
```
