import pandas as pd
import random
from datetime import datetime, timedelta

# Generate sample time series data
start_date = datetime(2023, 1, 1)
end_date = datetime(2023, 1, 10)
time_range = pd.date_range(start= start_date, end=end_date, freq="H")

data = {
    'timestamp' : time_range,
    "value" : [random.randint(0, 100) for _ in range(len(time_range))]
}

df = pd.DataFrame(data)
print(df)

# Filter data for a specific time range
start_time = datetime(2023, 1, 5, 12)
end_time = datetime(2023, 1, 6, 12)
filtered_data = df[(df["timestamp"]>= start_time) & (df["timestamp"] <= end_time)]
print("Filtered Data:")
print(filtered_data)

# Calculate the mean value for the filtered data
mean_value = filtered_data['value'].mean()
print("Mean Value:", mean_value)

