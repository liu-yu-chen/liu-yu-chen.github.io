+++
title = 'How agent-based modeling research is changing'
description = 'A review of 29,139 agent-based modeling publications, evolving research topics, early LLM use, and scientific collaboration.'
category = 'AGENT-BASED MODELING · LITERATURE ANALYSIS'
status = 'Review manuscript'
period = '29,139 publications · 1972–2025'
visual = 'literature'
weight = 2
chart = 'abm'
inlineCharts = true
sourceDocument = 'agent_based_modeling_review_revised_v4.docx'
figureAlt = 'Report-based charts on cohort composition, analysis stages, and quantitative results.'
figureCaption = 'Values transcribed from the supplied manuscript or report. Arithmetic reconstructions are labeled; these charts do not represent a new analysis of raw data.'
+++
## Research question

How has agent-based modeling (ABM) changed in scale, application themes, simulated entities, LLM use, and scientific collaboration? This quantitative review connects long-run field development with the early 2023–2025 diffusion of LLM-enabled methods.

## Corpus and data sources {#research-data}

The strict corpus contains 29,139 English research publications dated 1972–2025. Records were collected from Web of Science, PubMed, and DBLP, deduplicated, and enriched with OpenAlex abstracts where possible. Records still lacking abstracts, non-research publication types, and non-English material were excluded.

| Database coverage in the reported corpus | Papers | Exclusively indexed there |
| --- | ---: | ---: |
| Web of Science | 26,307 | 15,130 |
| PubMed | 9,671 | 607 |
| DBLP | 4,640 | 2,201 |

Database counts overlap: 11,201 papers are indexed in two or more sources. Adding the three source counts therefore double-counts records. Primary-topic percentages use the 29,139-paper denominator. Multi-label subthemes instead use 65,733 assigned mentions, because a paper can receive two or three labels.

## Methods linked to findings

| Data science method | Corresponding finding | Interpretation boundary |
| --- | --- | --- |
| Taxonomy-guided LLM classification | 236 of 29,139 publications classified as using LLMs methodologically. | Labels depend on corpus coverage and classification validation. |
| Annual shares and trend tests | LLM shares rise from 1.50% (2023) to 5.65% (2025); trend p < 0.001. | Describes adoption, not effects on research quality. |
| Coauthorship networks and community detection | Reported communities increase from 8 to 52 across analyzed periods. | Network structure is sensitive to period and construction choices. |

## Analytical methods {#research-methods}

The manuscript uses structured title-and-abstract classification through the DeepSeek API. Requests use temperature 0, JSON output, abstracts capped at 6,000 characters, and explicit topic, agent-type, LLM-use, and role taxonomies. Parsed fields are checked before merging into the corpus. This is taxonomy-guided classification, rather than an unsupervised LDA topic model.

An LLM counts as used only if it contributes to the research method. Background mentions, writing assistance, editing, translation, and literature searching are excluded. LLM involvement in simulated agent decisions is distinguished from supporting code, data generation, analysis, and interfaces.

The review combines annual counts and shares, Cochran–Armitage trend tests, decade-based logistic models with Benjamini–Hochberg correction, Poisson growth analyses, and coauthorship-community detection. The 2018–2022 versus 2023–2025 period comparison is descriptive; it does not identify an LLM-caused change.

## Main results {#research-results}

Annual output rises from 134 papers in 2000 to 2,495 in 2025, approximately 18.6-fold (calculated from the two reported counts). Epidemiology/public health is the leading primary domain, followed by simulation methodology and ecology/environment. Publication expansion and thematic redistribution are separate findings.

{{< research-results >}}

### Themes and simulated agents

Ecology/environment declines from about 28.0% of annual papers in 2001 to roughly 15% in 2025. Public health reaches 40.9% in 2022, while transport grows to about 11% by 2025. These endpoints describe relative emphasis, not uninterrupted trajectories. Humans/households account for 41.20% of modeled-entity classifications; patients and biological entities account for 22.34%.

### Early LLM diffusion

Only 236 papers (0.81% of the entire historical corpus) are classified as using an LLM. Annual LLM-paper counts grow from 32 to 63 to 141 in 2023–2025, with corresponding annual shares of 1.50%, 2.75%, and 5.65% (trend p < 0.001). The 2025/2023 share ratio is 3.77. Among 235 papers with classifiable roles, 140 use LLMs for agent behavior or decisions; the reported Wilson 95% interval for their 59.6% share is 53.2–65.6%.

### Collaboration and interpretation

The manuscript reports detected communities increasing from 8 to 52 across its analyzed periods, suggesting a more extensive but modular collaboration structure. LLM-related papers have lower reported international-collaboration shares than comparison papers (20.3% versus 31.6%; q = 5.5 × 10⁻⁴). These are corpus associations, not evidence that LLM use reduces collaboration.

## Interpretation and limits {#research-limits}

Coverage, abstract availability, taxonomies, and automated labeling shape every estimate. The review is not a census of all ABM publications, and classification consistency is not a substitute for human validation. The post-release window spans only three years. Growing adoption cannot demonstrate behavioral validity, model reproducibility, or causal changes in the field; those need independent benchmarks and sensitivity checks.
