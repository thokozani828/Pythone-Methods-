import pandas as pd

data = pd.read_csv("C:/Users/Admin/Favorites/Documents/TECHNICAL PROGRAMMING II/motor_insure.csv/motor_data11-14lats.csv")

print = (data.head(10))

print (data[data['SEAT_NUM'] > 40 ] [['MAKE', 'USAGE']])

import matplotlib.pyplot as plt

plt.plot (data['EFFECTIVE_YR'], data['CARRYING_CAPACITY'])
plt.ylabel ('EFFECTIVE_YEARS')
plt.xlabel ('CARRYING cAPACITY')
plt.tittle ('EFFECTIVE YEARS VS CARRYING CAPACITY')
plt.show()