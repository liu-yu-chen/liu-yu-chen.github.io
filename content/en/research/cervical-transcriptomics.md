+++
title = 'Cervical-cancer transcriptomics & survival analysis'
description = 'An exploratory class project combining TCGA-CESC and GTEx expression data with survival-endpoint analysis.'
category = 'BIOMEDICAL DATA SCIENCE · MULTI-OMICS'
status = 'Exploratory course project'
period = 'Transcriptomic and clinical data analysis'
visual = 'omics'
weight = 4
chart = 'cervical'
figureAlt = 'Two panels distinguish the 328-sample expression dataset (309 TCGA-CESC tumors and 19 GTEx normal samples) from the 312-patient clinical survival dataset; the second panel shows reported event rates for four endpoints and highlights that disease-free interval is available for 178 patients.'
figureCaption = 'Expression and survival counts describe different analysis tables and should not be treated as one fully matched cohort. Event rates are descriptive, not treatment effects or prospective predictions. The report labels its conclusions exploratory and says external validation is still needed.'
+++
## Project scope

This course project explores transcriptomic differences between cervical tumor and normal-tissue samples, then describes clinical and survival endpoints in the supplied report. It combines data-processing steps, feature ranking, survival analysis, and machine-learning exercises.

## Expression data

The integrated expression table contains **309 TCGA-CESC tumor samples** and **19 GTEx normal-tissue samples** (328 samples total), with **14,794 retained genes** after the report's filtering and intersection steps. TCGA and GTEx expression values were transformed before analysis. The tumor-to-normal ratio is approximately **16:1**.

## Clinical outcomes

The separate clinical table describes **312 patients**. The report lists event rates of **23.4% for overall survival (OS)**, **18.2% for disease-specific survival (DSS)**, **15.2% for disease-free interval (DFI)**, and **23.4% for progression-free interval (PFI)**. DFI analysis is available for only **178 patients**, reflecting incomplete records. The expression and survival table counts are not interchangeable or established as one fully matched cohort.

## Interpretation and limits

The report's cross-validation table lists near-perfect XGBoost metrics, but its discussion explicitly calls the conclusions exploratory and notes overfitting risk, TCGA–GTEx batch effects, a small and imbalanced normal-tissue sample, and the absence of independent external-cohort and experimental validation. These scores should not be read as clinical diagnostic performance. The feature-ranked genes are computational candidates, not validated biomarkers.
