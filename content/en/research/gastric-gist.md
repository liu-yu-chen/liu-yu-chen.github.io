+++
title = 'Shared gene signals in gastric cancer and GIST'
description = 'An exploratory GEO-based analysis combining differential expression, co-expression networks, feature selection, and a cautious Mendelian-randomization follow-up.'
category = 'BIOMEDICAL DATA SCIENCE · TRANSCRIPTOMICS'
status = 'Course research project'
period = 'GEO microarray analysis'
visual = 'omics'
weight = 3
chart = 'gastric'
inlineCharts = true
sourceDocument = 'Report.pdf'
figureAlt = 'Report-based charts on cohort composition, analysis stages, and quantitative results.'
figureCaption = 'Values transcribed from the supplied manuscript or report. Arithmetic reconstructions are labeled; these charts do not represent a new analysis of raw data.'
+++
## Project question

This course project asks whether public gastric-cancer (GC) and gastrointestinal-stromal-tumor (GIST) expression datasets share gene signals that can be prioritized for follow-up. It links differential expression, co-expression modules, biological enrichment, machine-learning feature selection, and genetic-association analysis.

## Data sources {#research-data}

The report lists three GEO microarray datasets. Its described differential-expression and WGCNA intersection uses the first two below; the third is listed in the source table but its contribution to those intersection results is not established.

| Dataset | Disease | Cases / controls | Platform | Reported role |
| --- | --- | ---: | --- | --- |
| GSE146996 | Gastric cancer | 50 / 15 | GPL17586 | Differential expression and WGCNA |
| GSE225819 | GIST | 20 / 20 | GPL15207 | Differential expression and WGCNA |
| GSE54129 | Gastric cancer | 111 / 21 | GPL570 | Listed additional dataset |

These are separate tumor cohorts, not patients with confirmed GC–GIST comorbidity. Shared expression signals therefore do not directly establish mechanisms of co-occurring disease.

## Analytical methods {#research-methods}

1. Use limma to compare cases with controls, selecting genes at FDR < 0.05 and |log₂ fold change| > 1; display patterns with volcano plots and expression heatmaps.
2. Build WGCNA modules using the reported top 5,000 variable genes, minimum module size 30, and merge cut height 0.25. Intersect the selected turquoise modules across datasets.
3. Contextualize the intersecting genes with GO, KEGG, and protein–protein interaction analyses. Enrichment identifies overrepresented annotations; it does not verify pathway activity experimentally.
4. Fit Random Forest with 1,000 trees and node size 5, then use binomial LASSO with ten-fold cross-validation and lambda.min to narrow candidate features. The report also constructs XGBoost models and displays ROC / precision–recall curves.
5. Screen cis-eQTLs at p < 5 × 10⁻⁸, clump at r² < 0.001, require F-statistic > 10, and match available gastric-cancer GWAS records for an exploratory MR follow-up. The report describes Wald-ratio estimation.

## Main results {#research-results}

Differential-expression screening identifies 3,452 upregulated and 692 downregulated genes in GC, versus 3,529 upregulated and 3,037 downregulated genes in GIST. The selected turquoise modules contain 2,872 and 1,905 genes respectively; their intersection contains 581.

{{< research-results >}}

### Biological interpretation and feature selection

The report highlights wound healing, extracellular-matrix organization, and cell adhesion in GO analysis, and cytoskeletal regulation, PI3K–Akt signaling, and ECM–receptor interactions in KEGG. These annotations suggest follow-up questions about tissue repair and the tumor microenvironment, without establishing a shared causal mechanism.

Random Forest narrows the 581 features to 58, and LASSO retains 14 candidates: HSD11B1, LBH, PMEPA1, ECT2, FKBP10, CLDN1, ENG, HSPH1, WSB1, ATP1B3, PTPN12, CD44, SPP1, and FNDC1. The reported optimal LASSO penalty is 2.37 × 10⁻³. These are selected features in the supplied data, not established diagnostic markers.

### Why only four genes appear in the final MR figure

Six of the 14 candidates lack qualifying cis-eQTL information, leaving eight. WSB1 and ATP1B3 fail instrument screening, leaving six genes and eight independent SNPs. LBH and ENG then cannot be matched to the target GWAS. The final plot shows CLDN1, CD44, SPP1, and PTPN12; none of their reported associations reaches statistical significance.

## Interpretation and limits {#research-limits}

The report does not provide verifiable numeric validation-set XGBoost AUCs, so the website does not reconstruct curves or claim diagnostic performance. Cohorts are small, feature selection may be sample-dependent, and eQTL / GWAS coverage limits the MR analysis. An independent cohort that includes actual comorbidity cases, stronger validation design, and experimental follow-up would be needed for clinical or causal conclusions.
