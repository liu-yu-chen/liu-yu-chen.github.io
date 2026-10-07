+++
title = 'Cervical-cancer transcriptomics & survival analysis'
description = 'An exploratory class project combining TCGA-CESC and GTEx expression data with survival-endpoint analysis.'
category = 'BIOMEDICAL DATA SCIENCE · MULTI-OMICS'
status = 'Exploratory course project'
period = 'Transcriptomic and clinical data analysis'
visual = 'omics'
weight = 4
chart = 'cervical'
inlineCharts = true
sourceDocument = 'FULL_REPORT_FOR_CISC7201.docx'
figureAlt = 'Report-based charts on cohort composition, analysis stages, and quantitative results.'
figureCaption = 'Values transcribed from the supplied manuscript or report. Arithmetic reconstructions are labeled; these charts do not represent a new analysis of raw data.'
+++
## Project question and my contribution

This exploratory course project combines tumor-versus-normal transcriptomic analysis with a separate clinical-survival analysis. The team report lists my contribution as data engineering, gene selection, and overall-sample survival analysis. The project asks which expression features separate the available tissue samples and how recorded clinical factors relate to survival outcomes.

## Data and preprocessing {#research-data}

The expression matrix contains 309 TCGA-CESC tumor samples and 19 GTEx normal-cervix samples. The starting TCGA matrix has 60,660 genes; filtering and cross-source intersection retain 14,794. The clinical table contains 312 patients, with mean age 48.3 years and age range 20–88. These tables are not established as one fully matched cohort.

| Data component | Size | Main interpretive issue |
| --- | ---: | --- |
| Expression samples | 328 | Tumor:normal ≈ 16:1 |
| Retained genes | 14,794 | High dimension relative to sample size |
| Clinical OS / PFI status | 312 each | Observational outcomes with censoring |
| DSS status / DFI status | 308 / 178 | Endpoint-specific missingness |

The report transposes matrices, standardizes identifiers, log₂(x+1)-transforms TCGA FPKM-UQ and GTEx TPM values, and retains genes above its expression threshold in at least 20% of samples. A shared log transform does not make the original units or batch effects equivalent; the report acknowledges that TCGA–GTEx batch correction was not performed.

## Analytical methods {#research-methods}

The expression workflow uses exploratory XGBoost tissue classification, cross-validation, and relative feature-importance ranking. The clinical workflow describes event-status and follow-up distributions, draws Kaplan–Meier curves, uses log-rank comparisons, and fits univariable and multivariable Cox models for OS.

OS means death from any cause; DSS concerns disease-specific death; DFI concerns a disease-free interval before a recorded recurrence; PFI concerns progression or recurrence. Each endpoint has its own available sample. Censoring indicates that an event was not observed within the recorded follow-up, not proof it can never occur.

## Main results {#research-results}

Expression filtering retains 24.4% of the starting 60,660 genes (calculated from the report counts). Normal tissue represents only 5.8% of expression samples (19/328, calculated). The report ranks 15 candidate expression features and states that its top four account for more than 80% of relative importance; this is model-specific importance, not biological effect size.

{{< research-results >}}

### Endpoint coverage and prognosis

Reported event rates are OS 23.4%, DSS 18.2%, DFI 15.2%, and PFI 23.4%. DFI includes only 178 records; DSS has 308 non-missing statuses. The descriptive table’s medians of OS.time (636 days), DFI.time (769.5 days), and PFI.time (576.5 days) summarize recorded times, including censored observations. They should not be relabeled as Kaplan–Meier median survival estimates.

The adjusted Cox table reports stage IVA HR = 13.91 (95% CI 2.93–66.13; p = 0.0009) and stage IVB HR = 10.21 (2.05–50.80; p = 0.0045), relative to the model’s reference category, whose name is not specified in that table. Age has HR = 1.013 per year (0.995–1.032; p = 0.1612). The model concordance index is 0.641. Wide stage intervals indicate substantial uncertainty; a non-significant coefficient does not establish absence of association.

### Treatment comparisons and model scores

The report compares 97 radiotherapy-plus-cisplatin patients with only eight non-cisplatin radiotherapy patients. That imbalance and observational treatment assignment prevent a causal treatment-efficacy interpretation. Its near-perfect XGBoost cross-validation scores likewise cannot demonstrate clinical diagnostic performance in an external population.

## Interpretation and limits {#research-limits}

Small normal-tissue numbers, cross-source batch effects, high dimensionality, endpoint missingness, and treatment imbalance limit inference. Classification may capture source differences as well as biology. Features are computational candidates; independent external cohorts, appropriate harmonization, a fully specified survival model, and experimental validation are required before clinical translation.
