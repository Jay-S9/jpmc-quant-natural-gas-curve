# Natural Gas Forward Curve – Model Review Q&A

This document outlines potential model review questions and structured responses.

---

## 1. Why use linear interpolation instead of spline methods?

Linear interpolation is selected due to:

- Smooth observed month-to-month transitions in forward prices.
- Limited sample size (48 observations), which does not justify higher-order fitting.
- Reduced overfitting risk compared to cubic splines.
- Greater interpretability and transparency for trading and risk discussions.

Given the business objective (pricing utility, not forecasting), linear interpolation is economically sufficient and defensible.

---

## 2. Why apply a linear trend instead of mean-reversion?

The optional trend adjustment reflects mild structural upward drift observed across historical winter peaks.

Mean-reversion modeling would require:

- Explicit stochastic specification.
- Parameter estimation beyond dataset capacity.
- Volatility modeling assumptions.

Given the deterministic objective and short (1-year) extension horizon, a linear drift provides minimal complexity while capturing structural directionality.

---

## 3. Why repeat only the most recent 12 months?

The most recent seasonal cycle reflects current market structure.

Repeating earlier years could:

- Embed outdated structural conditions.
- Dilute recent demand/supply dynamics.

Using the latest 12 months ensures:

- Seasonal persistence assumption
- Alignment with most recent pricing regime

---

## 4. How would volatility be modeled if required?

Volatility could be introduced via:

- Historical rolling standard deviation modeling
- Mean-reverting stochastic processes (e.g., Ornstein-Uhlenbeck)
- Jump-diffusion models for supply shocks
- Monte Carlo simulation of forward paths

This implementation intentionally avoids stochastic modeling to preserve deterministic pricing clarity.

---

## 5. How would structural breaks be handled?

Potential methods:

- Regime detection via change-point analysis
- Segmented trend fitting
- Rolling regression recalibration
- Incorporating macro drivers (weather, storage levels)

Current framework assumes no regime break within 1-year horizon.

---

## 6. How would you extend beyond one year?

Options include:

- Multi-year seasonal averaging
- Explicit supply-demand modeling
- Forward curve bootstrapping from futures market
- Structural commodity models (e.g., storage arbitrage models)

Long-horizon extension would require stronger economic modeling assumptions.

---

## 7. Why not decompose seasonality statistically?

Seasonal decomposition (e.g., STL) is feasible, but:

- Monthly granularity limits decomposition robustness.
- Sample size is modest.
- Business objective is forward pricing utility, not time-series inference.

Seasonal repetition of observed structure is sufficient and more interpretable for trading use.