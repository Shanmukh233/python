import matplotlib.pyplot as plt
import pandas as pd
dates = pd.date_range('2025-01-01', periods=10)
values = [10, 12, 15, 14, 18, 20, 17, 22, 24, 28]
plt.figure(figsize=(10, 4))
plt.plot(dates, values, marker='o', linestyle='-', color='blue')
plt.title("Time-Series Data Visualization")
plt.xlabel("Date")
plt.ylabel("Value")
plt.grid(True)
plt.gcf().autofmt_xdate()  # Auto-format date labels
plt.show()
