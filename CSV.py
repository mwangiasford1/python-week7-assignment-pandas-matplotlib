import pandas as pd

# Creating the DataFrame from the given dictionary
data = {
    'product': ['smart tv', 'hp laptop', 'macbook', 'iphone'],
    'date': ['2023-01-01', '2023-02-01', '2023-03-01', '2023-04-01'],
    'revenue ($)': [1000, 1500, 2000, 1200],
    'quantity sold': [5, 3, 2, 4],
}

# Load the data into a DataFrame
df = pd.DataFrame(data)

# Calculate the total revenue
total_revenue = df['revenue ($)'].sum()

# Find the best-selling product (based on Quantity Sold)
best_selling_product = df.loc[df['quantity sold'].idxmax(), 'product']

# Identify the day with the highest sales (based on revenue)
highest_sales_day = df.loc[df['revenue ($)'].idxmax(), 'date']

# Save the results to a new file called sales_summary.txt
with open('sales_summary.txt', 'w') as file:
    file.write(f"Total Revenue: ${total_revenue}\n")
    file.write(f"Best-Selling Product: {best_selling_product}\n")
    file.write(f"Day with Highest Sales: {highest_sales_day}\n")

print("Sales summary has been saved to sales_summary.txt.")

