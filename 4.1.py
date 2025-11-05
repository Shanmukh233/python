#4.1 1)
'''import pandas as pd

# Create a Pandas Series
data = [10, 20, 30, 40, 50]
series = pd.Series(data)

print("Pandas Series:")
print(series)

#4.1 2)
import pandas as pd

# Create a Pandas Series
data = [10, 20, 30, 40, 50]
series = pd.Series(data)

# Convert to Python list
python_list = series.tolist()

print("Converted Python list:", python_list)
print("Type of object:", type(python_list))'''

import pandas as pd

data=[10,20,30,40]
series=pd.Series(data)

print(series)


py_list=series.tolist()
