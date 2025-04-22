import matplotlib.pyplot as plt

import pandas as pd

# Example DataFrame definition
data = {
	'date': ['2023-01-01', '2023-02-01', '2023-03-01', '2023-04-01'],
	'revenue ($)': [1000, 1500, 2000, 1200]
}
df = pd.DataFrame(data)

plt.figure(figsize=(10, 5))
plt.plot(df['date'], df['revenue ($)'], marker='o', linestyle='-')
plt.xlabel("Date")
plt.ylabel("Revenue ($)")
plt.title("Sales Revenue Trend")
plt.xticks(rotation=45)
plt.grid(True)
plt.show()