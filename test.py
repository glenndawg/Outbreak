import pandas as pd
from datetime import date

x = []

i = 20

start_date = date.today()
time_stamp_index = pd.date_range(start_date, periods=i, freq="W")

for j in range(0,i):
    x.append(time_stamp_index[j])

print(start_date)

for j in range(0,i):
    print(time_stamp_index[j], ':' ,x[j])
print(x)
print(time_stamp_index)

# frequency codes:

# Alias    Description
# B        business day frequency
# C        custom business day frequency
# D        calendar day frequency
# W        weekly frequency
# M        month end frequency
# BM       business month end frequency
# CBM      custom business month end frequency
# MS       month start frequency
# SMS      semi-month start frequency (1st and 15th)
# BMS      business month start frequency
# CBMS     custom business month start frequency
# Q        quarter end frequency
# BQ       business quarter end frequency
# QS       quarter start frequency
# BQS      business quarter start frequency
# A, Y     year end frequency
# BA, BY   business year end frequency
# AS, YS   year start frequency
# BAS, BYS business year start frequency
# BH       business hour frequency
# H        hourly frequency
# T, min   minutely frequency
# S        secondly frequency
# L, ms    milliseconds
# U, us    microseconds
# N        nanoseconds