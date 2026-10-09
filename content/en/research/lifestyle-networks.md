+++
title = 'Lifestyle, networks & depressive symptoms'
description = 'A 105,138-record cancer-screening survey analyzed as a conditional-association network, with a disjoint holdout and sensitivity checks.'
category = 'PUBLIC HEALTH · NETWORK SCIENCE'
status = 'Manuscript analysis'
period = '105,138 survey records'
visual = 'network'
weight = 1
chart = 'lifestyle'
inlineCharts = true
sourceDocument = 'Lifestyle_Network_Depressive_Symptoms_Manuscript.docx'
figureAlt = 'Report-based charts on cohort composition, analysis stages, and quantitative results.'
figureCaption = 'Values transcribed from the supplied manuscript or report. Arithmetic reconstructions are labeled; these charts do not represent a new analysis of raw data.'
+++
## Research question

This project studies how lifestyle, work, and demographic variables co-occur with depressive symptoms in a cancer-screening survey. It asks three connected questions: which variables have direct conditional associations with the SDS symptom score, whether those associations repeat in other respondents, and whether the network differs across sex and age groups.

## Data and measurement {#research-data}

The manuscript analyzes 105,138 cleaned respondent records. The 36-node network includes the continuous SDS standard score alongside age, education, insurance, BMI, smoking, alcohol, diet, sleep, work, commuting, and physical activity. SDS measures symptom severity; it does not establish a clinical depression diagnosis. Several exposures are ordered questionnaire categories rather than continuous quantities.

| Analysis group | Records | Purpose |
| --- | ---: | --- |
| Women / men | 66,151 / 38,987 | Sex-specific networks |
| Ages 18–34 / 35–49 / 50+ | 44,310 / 39,061 / 21,767 | Prespecified descriptive strata |
| Discovery / holdout | 63,082 / 42,056 | Age-stratified 60% / 40% internal replication |

Records without an SDS score were excluded. Remaining missing variables were median-filled in network preparation. A separate upstream issue concerns secondhand smoke: only 29,928 respondents had an observed source value; 75,210 values had been filled by random-forest iterative imputation. This is important when interpreting that edge.

## Methods linked to findings

| Data science method | Corresponding finding | Interpretation boundary |
| --- | --- | --- |
| Ledoit–Wolf partial correlations | 36 nodes; 107 displayed edges; 13 direct SDS links at |r| ≥ 0.04. | Conditional associations, not intervention effects. |
| 60/40 discovery–holdout check | All 13 selected links retain direction; 12 exceed the display threshold in holdout. | Internal repeatability within the same survey. |
| Bootstrap simultaneous bands | 4 sex-related and 1/3/1 age-contrast edge differences; none is a direct SDS edge. | No resolved SDS-edge difference under this criterion. |

## Analytical methods {#research-methods}

1. Standardize variables within each analysis sample, estimate a Ledoit–Wolf shrinkage covariance matrix, and convert its inverse into partial correlations. Each edge describes a linear association conditional on the other modeled variables.
2. Display edges with |r| ≥ 0.04 to improve readability. This is a plotting rule, not a significance threshold. Node strength summarizes absolute displayed connections, not effects on SDS.
3. Re-estimate the network in two equal random halves. Separately, select SDS links in the 60% discovery sample and check their direction and magnitude in the disjoint 40% holdout. These are two different internal checks.
4. Compare 595 edges among 35 non-age variables for sex and three pairwise age contrasts, using 200 within-group bootstrap resamples and simultaneous uncertainty bands within each contrast. The main network has 36 nodes; 595 is the group-comparison edge count, not all possible pairs in that network.
5. Repeat estimation after excluding identical SDS response patterns, among observed-source secondhand-smoke records, and at display thresholds from 0.03 to 0.06.

## Main results {#research-results}

The full network displays 107 edges, including 13 direct SDS-score links. All 13 discovery-selected links keep their direction in the holdout; 12 also remain above 0.04. Light leisure activity is a threshold-sensitive case: discovery r = −0.043 versus holdout r = −0.033. The separate split-half check also retains 12 of 13 main SDS links, with tea frequency as its boundary case.

{{< research-results >}}

### Sleep and diet associations

Sleep latency (r = +0.077), sugary-drink intake category (+0.068), and sleep-medication frequency (+0.067) have positive full-sample SDS associations. After excluding identical SDS answers, these become +0.106, +0.062, and +0.072. Their consistently positive direction is more defensible than treating any coefficient as an intervention effect; medication use may reflect existing sleep problems or symptom severity.

### Group comparisons and data quality

Four women–men edge differences and 1, 3, and 1 differences in the three age contrasts have simultaneous bands excluding zero. These involve lifestyle-to-lifestyle links. No direct SDS-score edge difference excludes zero. This does not prove equality between populations; it means this analysis did not resolve an individual SDS-link difference under its across-edge criterion.

Identical answers across all 20 SDS items occur in 31,013 records (29.5%). The secondhand-smoke association weakens from −0.125 to −0.068 after their exclusion and to −0.058 in the observed-exposure subset. Daytime sleepiness changes sign in the response-pattern check. These results motivate a questionnaire and data-processing audit, rather than a protective interpretation of an inverse edge.

## Interpretation and limits {#research-limits}

The study is cross-sectional and self-reported. Partial correlations depend on numeric coding, variable inclusion, linearity, and missing-data handling. Bootstrap precision is limited by 200 replicates, and simultaneous bands cover edges within each contrast rather than all four contrasts together. Internal random splits share the same survey and cleaning decisions. External replication and longitudinal measurements are needed to assess transportability and temporal order.
