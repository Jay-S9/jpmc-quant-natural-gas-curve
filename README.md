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

The objective is to construct a continuous forward price curve from discrete monthly observations and extend it by one calendar year in a manner consistent with observed market structure.

The methodology is intentionally deterministic and economically grounded, prioritizing transparency and robustness over unnecessary statistical complexity.

### 1. In-Sample Interpolation

The available dataset provides only end-of-month forward prices. However, storage contract valuation requires price estimates at arbitrary calendar dates. To construct a continuous pricing function within the observed range, linear interpolation is applied between adjacent monthly observations.

Linear interpolation is selected for the following reasons:

- Forward prices typically evolve smoothly in the absence of new market information.
- The dataset exhibits gradual month-to-month transitions without extreme discontinuities.
- The sample size (48 observations) does not justify high-order curve fitting or spline-based overfitting.
- The resulting curve remains transparent and easily interpretable for trading and risk discussions.

This approach produces a continuous time representation while preserving the observed structural dynamics of the market.

### 2. One-Year Extrapolation

The forward curve is extended by one calendar year beyond the final observed data point. The extrapolation methodology assumes persistence of the most recent 12-month seasonal structure.

Specifically, the final observed year's monthly price pattern is shifted forward by one calendar year. This approach reflects:

- Stable seasonal demand patterns driven by heating cycles and storage behavior.
- Absence of structural regime shifts within the observed sample.
- The need for conservative extension without imposing aggressive trend projections.

No explicit stochastic modeling, volatility forecasting, or macroeconomic trend extrapolation is introduced at this stage. The goal is to provide a stable and defensible forward pricing surface suitable for storage spread analysis rather than long-horizon speculative forecasting.

### 3. Modeling Philosophy

The design intentionally avoids machine learning frameworks, high-degree polynomial fitting, or autoregressive time-series models. Given the dataset size and business objective, such approaches would introduce unnecessary complexity and potential overfitting risk.

The resulting framework provides:

- Continuous time granularity
- Seasonal structure preservation
- Deterministic and interpretable behavior
- Controlled extrapolation horizon (one year)

This foundation supports subsequent storage contract valuation and spread analysis in a disciplined and economically consistent manner.
---

## Assumptions & Limitations

### Core Assumptions

1. **Smooth Forward Price Evolution**  
   Forward prices are assumed to evolve smoothly between observed monthly delivery points in the absence of new market information. Linear interpolation therefore provides a reasonable approximation within the observed range.

2. **Seasonal Persistence**  
   Seasonal demand patterns for natural gas, particularly winter heating demand and summer storage behavior, are assumed to persist over the one-year extrapolation horizon.

3. **No Structural Regime Shift**  
   The extrapolation assumes no abrupt macroeconomic shocks, geopolitical disruptions, supply shocks, or structural market changes within the extension period.

4. **Deterministic Framework**  
   The constructed curve represents expected price levels rather than probabilistic forecasts. Volatility dynamics and uncertainty bands are not modeled at this stage.

---

### Limitations

- The model does not incorporate macroeconomic drivers such as weather variability, geopolitical risk, production constraints, or policy changes.
- The extrapolation horizon is limited to one year; longer-term projections would require structural modeling.
- Monthly granularity restricts the ability to capture short-term volatility or intra-month price dynamics.
- No stochastic process (e.g., mean-reversion or jump dynamics) is explicitly modeled.
- The framework should be viewed as a pricing utility rather than a predictive trading model.

---

This forward curve construction is intended as a foundational tool for storage spread evaluation. More advanced modeling (e.g., stochastic simulation, regime detection, volatility modeling) could be layered onto this framework in subsequent development phases.
---

## Implementation

The forward curve is implemented as a reusable Python class:

`NaturalGasForwardCurve`

Key features:

- Loads and cleans monthly forward data
- Constructs continuous pricing curve via linear interpolation
- Extends curve by one year using seasonal repetition
- Optional mild linear trend adjustment
- Input validation with explicit supported date range
- Built-in visualization utility

The model is designed to be deterministic, interpretable, and modular, making it suitable as a foundational pricing utility for storage spread analysis.

---

### Core Class Interface

```python
curve = NaturalGasForwardCurve("data/NAT_GAS.csv", apply_trend=False)
price = curve.get_price("2025-01-15")

---

## Example Usage

[Section 7]
