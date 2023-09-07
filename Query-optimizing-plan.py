# Simulating a basic database schema with table and data
tables = {
    "orders" : {"order_id" : "int", "customer_id": "int", "order_date":"date"},
    "customers" : {"customer_id" : "int", "name":"string", "email":"string"},
    "order_items" :{"order_id": "int", "product_id": "int", "quantity": "int"}
}

# Simulating statistics (cardinality) for tables

table_statistics = {
    "orders": {"rows": 1000, "avg_row_size": 50},
    "customers" : {"rows": 200, "avg_row_size": 40},
    "order_items" : {"rows": 3000, "avg_row_size":30}
}

# Simulating a query to find total sales for each customer
query = """
SELECT c.name, SUM(oi.quantity) as total_quantity FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
JOIN order_items oi ON o.order_id = oi.order_id
GROUP BY c.name
"""

# Step 1 : Parsing and Syntax Analysis (Not simulated here)

# Step 2 : Optimizer: Choose Join Order (Simulated)
# For Simplicity, we'll consider only one join order here.
join_order = ["customers", "orders", "order_items"]

# Step 3 : Cost Estimation and plan Selection (Simulated)
# Let's simulate a simple cost estimation based on cardinality and row sizes.
total_cost = sum(table_statistics[table]["rows"] for table in join_order)
print("Total estimated cost:", total_cost)

# Step 4 : Execution (Simulated)
# Let's print the selected join order and execute the query
print("Selected Join Order:", join_order)
print("Executing query:")
print(query)

# Output the query result (simulated)
# In a real scenario, you would connect to a database and execute the query.
# Here we'll just print some simulated query results.
query_results = [
    ("Alice", 100),
    ("Bob", 150),
    ("Charlie", 200)
]

print("\nQuery Results:")
for row in query_results:
    print(row)