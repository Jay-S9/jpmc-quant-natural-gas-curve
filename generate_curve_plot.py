from nat_gas_curve import NaturalGasForwardCurve
import matplotlib.pyplot as plt

curve = NaturalGasForwardCurve("data/NAT_GAS.csv", apply_trend=True)

plt.figure(figsize=(10, 5))
plt.plot(curve.extended_df["Dates"], curve.extended_df["Prices"])
plt.title("Natural Gas Forward Curve (Seasonal + Trend Extension)")
plt.xlabel("Date")
plt.ylabel("Price")
plt.grid(True)

plt.savefig("visuals/forward_curve.png", dpi=300)
plt.show()