+++
title = 'Shenzhen–Hong Kong land-border dashboard'
description = 'Preliminary findings: mean daily crossings rose 67.7% in 2023–2025; weekends were 38.6% higher than weekdays. Model training is ongoing.'
category = 'TIME SERIES · FORECASTING'
status = 'Model training in progress'
period = 'Results through 8 October 2026'
weight = 2
visual = 'network'
evidence = 'border-dashboard'
+++
## Preliminary findings

- **Traffic grows while annual growth slows.** Mean daily two-way crossings across six ports increase from 358,214 in 2023 to 600,584 in 2025, a 67.7% rise. Annual daily-mean growth is 47.1% in 2024 and 14.0% in 2025. The reopening period makes 2023 an atypical baseline.
- **The weekend pattern is clearer than annual seasonality.** In 2023–2025, weekend traffic averages 618,180 crossings/day versus 446,059 on weekdays, 38.6% higher. Monthly rankings vary across years; a fixed holiday effect has not been established.
- **Port scale and function differ substantially.** In 2025, Lo Wu averages approximately 192,879 daily crossings and Futian / Lok Ma Chau Spur Line 161,755, followed by Shenzhen Bay at 121,669. Man Kam To is smallest at 5,799. Aggregate traffic cannot replace port-specific analysis.
- **The existing backtest supports further LSTM optimization.** Across 36 series in a 120-day rolling one-step test, median series MAE is 874.466 crossings/day, approximately 22.4% below the best simple baseline (same weekday last week, 1,127.588). This does not imply improvement for every series or validate future 30-day recursive forecasts.

These are preliminary findings from observations ending 7 October 2026 and the existing backtest. **Model training is ongoing**; the public cloud dashboard is not yet live. Findings will be updated as training and validation progress.

{{< project-evidence >}}

## What the project does

A planned data dashboard for six Shenzhen–Hong Kong land-border control points, combining passenger-traffic trends, port and direction comparisons, traveler categories, and daily forecasting. The project is in model training, building on existing local analyses and backtest results; the public cloud dashboard is pending.

## Data and measurement

The descriptive dataset covers **1 January 2023 – 7 October 2026**, with **1,376 days × six ports × two directions**. Arrival and departure are defined from Hong Kong's perspective. Counts are border crossings, not unique people; mainland visitors cannot be relabeled as Shenzhen residents.

## Methods linked to results

| Data science method | Existing result | Interpretation boundary |
| --- | --- | --- |
| Daily aggregation and annual comparison | Two-way daily mean rises from 358,214 in 2023 to 600,584 in 2025, up 67.7% | The 2023 reopening period makes the baseline atypical |
| Day-of-week grouping | Weekend mean 618,180 vs weekday mean 446,059 in 2023–2025, a 38.6% difference | Descriptive patterns, not an identified holiday effect |
| Multi-output LSTM with 56-day lookback | Median series MAE 874.466, versus 1,127.588 for the best simple baseline | 120-day rolling one-step backtest across 36 series |
| Time-ordered split and train-only standardization | Forecast evaluation excludes future observations from each day's input | One-step results do not validate 30-day recursive forecasts |

The LSTM predicts six ports × two directions × three traveler groups, using lagged traffic and calendar features. The last 120 days, 10 June – 7 October 2026, form the rolling one-step test. Median MAE is computed across series; its approximately 22.4% reduction relative to the same-weekday baseline is calculated from the saved summary values, not a guarantee for every port.

## Planned cloud dashboard

The intended interface will expose date, control-point, direction, and traveler-type comparisons, historical patterns, and clearly dated forecast results. Public cloud deployment is planned. The saved 30-day forecast was generated from observations ending 7 October 2026; it is a historical output, not a continuously updated live prediction.

## Limits and result provenance

Local outputs: `时序分析报告.md`, `daily_forecast/每日客流预测报告.md`, and `backtest_model_summary.csv`. Weather, traffic accessibility, temporary events, and operational arrangements are not included in the forecast. Descriptive cross-port changes cannot establish causal diversion. Only aggregate results are reproduced here; the application and raw dataset are not uploaded with this website.
