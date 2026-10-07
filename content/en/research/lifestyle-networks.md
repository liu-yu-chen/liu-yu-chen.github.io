+++
title = 'Lifestyle, networks & depressive symptoms'
description = 'A 105,138-record cancer-screening survey analyzed as a conditional-association network, with a disjoint holdout and sensitivity checks.'
category = 'PUBLIC HEALTH · NETWORK SCIENCE'
status = 'Manuscript analysis'
period = '105,138 survey records'
visual = 'network'
weight = 1
chart = 'lifestyle'
figureAlt = 'Two charts: the ten largest reported direct partial correlations with the SDS score and changes in displayed network edges as the absolute correlation threshold rises.'
figureCaption = 'Left: the ten strongest reported conditional associations with SDS score. Right: the displayed network becomes smaller as the readability threshold rises; it is a plotting threshold, not a significance test. The separate holdout checks directional repeatability within this survey.'
+++
## Research question

How do recorded lifestyle, work, and demographic variables relate conditionally to depressive-symptom scores in a cancer-screening survey? Do the selected connections keep their direction in different respondents from the same survey?

## Data and approach

The supplied manuscript analyzes **105,138 cleaned survey records** in a **36-node partial-correlation network**. Ledoit–Wolf shrinkage was used for covariance estimation. The displayed network contains 107 of 595 possible pairwise connections at an absolute-correlation display threshold of 0.04.

A separate, age-stratified split assigned **63,082 respondents to discovery** and **42,056 to the holdout**. The 13 displayed SDS-score edges selected in discovery all kept the same direction in the holdout; **12 of 13** also remained above the 0.04 display threshold.

## What the results show

Longer recorded sleep latency, higher sugary-drink intake categories, and more frequent sleep-medication use had positive partial correlations with SDS score. These are conditional associations among questionnaire variables. They do not establish that a behavior causes depressive symptoms, that an inverse association is protective, or that a respondent has a clinical depression diagnosis.

All SDS-score edge differences between the analyzed sex and age groups included zero under the manuscript's simultaneous bootstrap bands. This analysis did not find clear demographic differences in individual SDS links after accounting for the tested edges.

## Sensitivity and limits

The number of displayed connections depends on the prespecified figure threshold: as it rises from 0.03 to 0.06, the reported total goes from 130 to 62 connections, while direct SDS links go from 15 to 7. The threshold is used to make the graph readable; it does not indicate statistical significance.

After identifying respondents with identical answers across the 20 SDS items, the manuscript reports that **31,013 records (29.5%)** had that pattern. The secondhand-smoke edge weakened from **r = −0.125** in the full sample to **r = −0.068** in the sensitivity sample. This is a material data-quality limitation, not evidence that exposure is protective. The random holdout tests repeatability within one survey and cannot rule out artifacts shared across both halves. The study is cross-sectional.
