# Maritime Choke Point Trends Monitor

This section examines how AIS transit calls have evolved in specific crossing locations, also referred to as "choke points", given the conflict in the Middle East and the escalating attacks in the Red Sea.

## Data

### AIS Statistics

We process daily transit calls and estimated volume (capactiy) since 2019 from the IMF's [PortWatch](https://portwatch.imf.org/) platform for key areas of interest: Bab el-Mandeb Strait, Cape of Good Hope, Suez Canal. As of this date, the latest data point available is February 19th, 2024.

Since the data is daily, we first conduct a 7-day moving average to smoothen out the data and mitigate the effect of daily anomalies.

```{figure} ../../reports/chokepoints/transit-calls-chokepoints.jpeg
---
align: center
---
AIS Transit Calls in Key Areas
```

The vertical dotted red lines mark the beginning of key periods of interest highlighted by the team.
- Middle East conflict: **October 7th**
- Red Sea crisis: **November 17th**

As can be seen in the first figure, there is a clear diversion of maritime transit that begins early-mid December 2023, and intensifies in the following months.

The following chart shows the same metric (# of cargo/tanker vessels) going back to 2019, to show a historical trend for these areas, and give more context to the recent diversion event.

```{figure} ../../reports/chokepoints/transit-calls-chokepoints-historical.jpeg
---
align: center
---
AIS Transit Calls in Key Areas, Historical
```

The historical chart also shows the Suez Canal blockage in early 2021, and an overall upward trajectory in transit calls in both Bab el-Mandeb Strait and Suez Canal.

## Methodology

As noted earlier, first we apply a 7-day moving average to the daily data.

We then prepare a simple baseline estimation for each day of the year and compare the recent daily values to this reference baseline.

### Reference Period

Given the volatility of 2021, we define our reference period as January 1st 2023 up to October 6th 2023. We calculate daily averages based on this time period.

The following chart separates transit calls for each area and includes a black line which signals the historical average for each area.

```{figure} ../../reports/chokepoints/transit-calls-chokepoints-ref.jpeg
---
align: center
---
AIS Transit Calls Relative to Historical Average
```

### Percentage Change

We calculate the percentage change between recent daily values and the baseline daily average.

```{figure} ../../reports/chokepoints/transit-calls-chokepoints-pct.jpeg
---
align: center
---
AIS Transit Calls % Change from Historical Average
```

### Summary Statistics

Finally, we provide some aggregate statistics (average values) per area for each period of interest.

- **Baseline**: January 1st, 2022 – October 6th, 2023
- **Middle East Conflict**: October 7th, 2023 - November 16th, 2023
- **Red Sea Crisis**: November 17th, 2023 - February 19th, 2024

```{figure} ../../reports/chokepoints/summary-table.png
---
align: center
---
Daily Average Values by Time Period
```

The following table shows the difference in average values (% change from baseline period).

```{figure} ../../reports/chokepoints/summary-table-pct.png
---
align: center
---
Daily Average Values by Time Period, % Change from Baseline
```

## Implementation

- [Notebook to create charts and tables](red-sea-chokepoints.ipynb)
