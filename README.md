# JPMorgan Chase Quantitative Research Simulation
## Natural Gas Forward Curve Construction

---

## Executive Summary

This project constructs a continuous, seasonally-aware forward price curve for natural gas using monthly end-of-month delivery prices from October 2020 to September 2024. The objective is to support pricing and evaluation of storage contracts by enabling price estimation at arbitrary calendar dates.

Natural gas storage contracts derive value from temporal price differentials. Market participants may inject gas during lower-demand periods (typically summer) and withdraw during higher-demand periods (typically winter), capturing seasonal spreads subject to storage costs and operational constraints. Accurate contract valuation therefore requires a pricing function defined over continuous time rather than discrete monthly observations.

The forward curve construction is implemented in two stages:

1. **In-Sample Interpolation:**
   Linear interpolation between observed monthly forward prices to produce continuous time granularity while preserving smooth price evolution consistent with forward market behavior.

2. **One-Year Extrapolation:**  
   Extension of the most recent 12-month seasonal structure forward by one calendar year, assuming persistence of seasonal demand patterns without imposing aggressive trend projections.

The resulting framework provides a deterministic pricing utility:

`get_price(date)`

which returns an estimated forward price for any supported calendar date. The design prioritizes economic interpretability, robustness, and modeling discipline over unnecessary complexity.
---

## Business Context

Natural gas markets exhibit strong seasonal dynamics driven primarily by demand fluctuations and storage cycles. Winter months typically experience elevated demand due to heating needs, while summer months see comparatively lower consumption levels. As a result, forward prices often reflect predictable seasonal patterns, with higher winter delivery prices relative to summer delivery months.

Commodity storage contracts derive value from these temporal price differentials. Market participants may purchase natural gas during lower-demand periods, store the physical commodity, and subsequently sell it during higher-demand months to capture seasonal spreads. The profitability of such strategies depends on the expected price difference between injection and withdrawal dates, net of storage and operational costs.

Because storage decisions are not restricted to month-end dates, pricing utilities must estimate forward prices at arbitrary calendar points. The available dataset provides discrete monthly snapshots of end-of-month delivery prices, which are insufficient for granular injection and withdrawal modeling. A continuous forward pricing representation is therefore required to support storage valuation, spread analysis, and scenario assessment.
---

## Data Overview

## Data Overview

The dataset consists of monthly end-of-month natural gas forward prices spanning from 31 October 2020 to 30 September 2024. Each observation represents the market price of natural gas delivered at the end of the corresponding calendar month.

Key characteristics of the dataset:

- **Frequency:** Monthly (end-of-month observations)
- **Time Horizon:** Approximately four years (48 data points)
- **Delivery Convention:** Prices correspond to forward delivery at month-end
- **Granularity Limitation:** Only discrete monthly snapshots are available

Visual inspection of the time series confirms a clear and recurring seasonal structure. Winter delivery months (typically November through February) consistently exhibit higher prices relative to late spring and early summer months. This pattern aligns with increased heating demand and established storage withdrawal cycles.

In addition to seasonality, the data shows a gradual upward shift in overall price levels across the sample period, with successive winter peaks trending modestly higher from 2021 through 2024. However, no abrupt structural breaks or extreme volatility regimes are observed within the dataset.

Given the limited sample size and monthly frequency, the dataset is well-suited for deterministic curve construction and seasonal modeling. It is not sufficiently large or granular to justify high-complexity stochastic or machine learning frameworks at this stage.
---

## Methodology

[Section 4]

---

## Assumptions & Limitations

[Section 5]

---

## Implementation

[Section 6]

---

## Example Usage

[Section 7]
