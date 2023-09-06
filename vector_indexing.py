import pandas as pd
import random
from datetime import datetime, timedelta

# Generate the sample data
num_records = 10000

data = {
    "order_id" : range(1, num_records + 1),
    "customer_id" : [random.randint(1, 1000) for _ in range(num_records)],
    "order_date" : [datetime(2023, 1, 1) + timedelta(days= random.randint(1,365)) for _ in range(num_records)],
    "product_id" : [random.randint(1, 100) for _ in range(num_records)],
    "quantity" : [random.randint(1, 10) for _ in range(num_records)]
}

# Create DataFrame
df = pd.DataFrame(data)

# Display the first few rows of the dataframe
print(df.head())

# Without Index : Simple Query
start_time = datetime.now()
result_without_index = df[df['customer_id'] == 42]
print("Query without index took:", datetime.now() - start_time)

# Create an index on the 'customer_id' column
df_indexed = df.set_index('customer_id')

# With Index: Query using the index
start_time = datetime.now()
result_with_index = df_indexed.loc[42]
print("Query with index took: ", datetime.now() - start_time)