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

---

# Advanced Model Defense – Interview-Level Challenges

---

## 8. Why linear trend instead of mean-reversion (e.g., Ornstein–Uhlenbeck)?

### ❌ Weak Answer

"Mean-reversion requires more parameters and volatility modeling, and the dataset is small."

(Too shallow. Sounds like avoiding math.)

### ✅ Strong Answer

Natural gas spot prices often exhibit mean-reversion due to storage arbitrage and supply constraints. However, this implementation models a forward curve for storage pricing, not spot price dynamics. The objective is deterministic curve construction over a short one-year extension horizon.

Introducing an Ornstein–Uhlenbeck process would require:
- Estimating reversion speed
- Modeling volatility
- Defining long-term equilibrium levels

Given only 48 monthly observations and the absence of stochastic simulation objectives, a mild linear drift provides a minimal and interpretable structural adjustment without embedding strong assumptions about long-run equilibrium.

### 🧠 Why This Works

It:
- Acknowledges financial theory
- Distinguishes spot vs forward behavior
- Respects modeling scope
- Avoids sounding mathematically insecure

---

## 9. Why not use cubic splines for smoother interpolation?

### ❌ Weak Answer

"Spline might overfit."

(Too short, sounds hand-wavy.)

### ✅ Strong Answer

Cubic splines introduce additional curvature between monthly observations, which may artificially imply intra-month convexity unsupported by the data. The dataset shows smooth transitions without abrupt changes, making linear interpolation sufficient.

Given the deterministic objective and small sample size, spline smoothing risks introducing shape artifacts without economic justification.

### 🧠 Why This Works

It ties shape control to economic realism.

---

## 10. What if a structural break occurs next year?

### ❌ Weak Answer

"The model wouldn’t handle it."

(Too passive.)

### ✅ Strong Answer

The current framework assumes regime stability within the one-year extrapolation horizon. If a structural break occurs, the model should be recalibrated using updated forward observations.

In a production setting, this curve would be rebuilt periodically as new data arrives, rather than treated as a static forecast.

### 🧠 Why This Works

It:
- Shows awareness of model lifecycle
- Demonstrates operational realism
- Avoids pretending the model predicts shocks

---

## 11. How would you extend beyond one year?

### ❌ Weak Answer

"Add more trend."

(Over-simplistic.)

### ✅ Strong Answer

Longer-horizon extension would require stronger structural modeling assumptions. Possible approaches include:

- Multi-year seasonal averaging
- Storage arbitrage structural models
- Bootstrapping from futures market curves
- Stochastic simulation incorporating volatility and mean-reversion

Extending deterministically beyond one year without additional structure would materially increase model risk.

### 🧠 Why This Works

It:
- Recognizes scope boundaries
- Demonstrates awareness of professional modeling frameworks
- Shows intellectual restraint

---

## 12. Why not use sinusoidal regression like the example solution?

While sinusoidal regression provides a smooth parametric representation of annual periodicity, it imposes a strong assumption that seasonal behavior follows a stable sinusoidal form with constant amplitude and frequency.

The implemented approach instead preserves empirically observed seasonal structure directly from the most recent 12-month cycle. This avoids imposing a specific functional shape on seasonality and reduces structural model risk.

Given the limited dataset (48 observations) and the deterministic pricing objective, empirical seasonal repetition provides a more conservative and interpretable solution.