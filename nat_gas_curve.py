import pandas as pd
import numpy as np
from datetime import datetime
from pathlib import Path
import matplotlib.pyplot as plt


class NaturalGasForwardCurve:
    """
    Constructs a continuous forward price curve for natural gas
    using monthly end-of-month data with seasonal extrapolation.
    """

    def __init__(self, csv_path: str, apply_trend: bool = False):
        self.csv_path = Path(csv_path)
        self.apply_trend = apply_trend
        self._load_data()
        self._extend_curve()

    def _load_data(self):
        df = pd.read_csv(self.csv_path)

        df['Dates'] = pd.to_datetime(df['Dates'], format="%m/%d/%y")
        df['Prices'] = df['Prices'].astype(float)

        df = df.sort_values('Dates').reset_index(drop=True)

        self.df = df
        self.historical_start = df['Dates'].min()
        self.historical_end = df['Dates'].max()

    def _extend_curve(self):
        # --- Prepare historical data ---
        historical = self.df.copy()
        historical['ordinal'] = historical['Dates'].map(datetime.toordinal)

        x_hist = historical['ordinal'].values
        y_hist = historical['Prices'].values

        # --- Extend last 12 months seasonally ---
        last_12 = self.df.tail(12).copy()
        last_12['Dates'] = last_12['Dates'] + pd.DateOffset(years=1)
        last_12['ordinal'] = last_12['Dates'].map(datetime.toordinal)

        # --- Optional trend adjustment ---
        if self.apply_trend:
            slope, intercept = np.polyfit(x_hist, y_hist, 1)
            trend_adjustment = slope * (last_12['ordinal'] - x_hist.max())
            last_12['Prices'] = last_12['Prices'].values + trend_adjustment

        # --- Combine ---
        extended = pd.concat([historical[['Dates','Prices','ordinal']], last_12])
        extended = extended.sort_values('Dates').reset_index(drop=True)

        self.extended_df = extended
        self.extrapolated_end = extended['Dates'].max()

    def get_price(self, input_date: str):
        input_date = pd.to_datetime(input_date)

        if input_date < self.historical_start:
            raise ValueError(
                f"Date is before supported range (min: {self.historical_start.date()})."
            )

        if input_date > self.extrapolated_end:
            raise ValueError(
                f"Date exceeds supported horizon (max: {self.extrapolated_end.date()})."
            )

        ordinal = input_date.toordinal()

        x = self.extended_df['ordinal'].values
        y = self.extended_df['Prices'].values

        return float(np.interp(ordinal, x, y))

    def plot_curve(self):
        plt.figure(figsize=(10, 5))
        plt.plot(self.extended_df['Dates'], self.extended_df['Prices'])
        plt.title("Natural Gas Forward Curve (Extended)")
        plt.xlabel("Date")
        plt.ylabel("Price")
        plt.grid(True)
        plt.show()


if __name__ == "__main__":
    print("Baseline (no trend):")
    curve_base = NaturalGasForwardCurve("data/NAT_GAS.csv")
    print(curve_base.get_price("2025-01-15"))

    print("\nWith mild trend:")
    curve_trend = NaturalGasForwardCurve("data/NAT_GAS.csv", apply_trend=True)
    print(curve_trend.get_price("2025-01-15"))