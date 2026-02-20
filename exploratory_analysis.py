import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("data/NAT_GAS.csv")

# Clean columns
df['Dates'] = pd.to_datetime(df['Dates'])
df['Prices'] = df['Prices'].astype(float)

# Plot
plt.figure(figsize=(10,5))
plt.plot(df['Dates'], df['Prices'])
plt.title("Natural Gas Monthly Prices")
plt.xlabel("Date")
plt.ylabel("Price")
plt.grid(True)
plt.show()