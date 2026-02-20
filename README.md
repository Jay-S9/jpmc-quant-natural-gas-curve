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

[Section 2]

---

## Data Overview

[Section 3]

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
