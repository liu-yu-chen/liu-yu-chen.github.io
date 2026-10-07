+++
title = 'Shared gene signals in gastric cancer and GIST'
description = 'An exploratory GEO-based analysis combining differential expression, co-expression networks, feature selection, and a cautious Mendelian-randomization follow-up.'
category = 'BIOMEDICAL DATA SCIENCE · TRANSCRIPTOMICS'
status = 'Course research project'
period = 'GEO microarray analysis'
visual = 'omics'
weight = 3
chart = 'gastric'
figureAlt = 'Analysis pipeline: 581 intersecting co-expression hub genes, narrowed to 58 by Random Forest, 14 by LASSO, 8 eligible for cis-eQTL screening, 6 passing instrument filtering, and 4 included in the reported Mendelian-randomization forest plot.'
figureCaption = 'The counts follow the supplied project report. Of the four genes in the final MR figure, none of the reported associations reached statistical significance. These are computational candidate-gene analyses, not validated diagnostic markers or causal findings.'
+++
## Project question

Can expression data from public gastric-cancer and gastrointestinal-stromal-tumor (GIST) studies identify genes shared by the two conditions? The course project combines GEO microarrays, co-expression-network analysis, feature selection, and an exploratory Mendelian-randomization (MR) follow-up.

## Data and analysis

The reported intersection used **GSE146996** (50 gastric-cancer cases and 15 controls) and **GSE225819** (20 GIST cases and 20 controls). Differentially expressed genes were screened with **FDR < 0.05 and |log₂ fold change| > 1**. WGCNA identified shared turquoise-module signals; intersecting the two datasets produced **581 hub genes**.

Random Forest narrowed the set to **58** features and LASSO to **14** candidate genes. The follow-up then filtered genes against cis-eQTL and GWAS availability: eight entered follow-up, six passed instrument screening, and four appeared in the final MR plot.

## What the project supports

The results support a computational workflow for identifying and prioritizing shared candidates in these datasets. In the final MR results supplied with the report, **none of the four reported gene associations reached statistical significance**.

## Limits

The supplied report does not give verifiable numeric ROC-AUC values for its XGBoost validation sets, so none are presented here. The proposed markers remain computational candidates; the report does not establish clinical diagnostic performance or causal gene effects. Its dataset table also lists GSE54129, although its described differential-expression and WGCNA intersection results use GSE146996 and GSE225819.
