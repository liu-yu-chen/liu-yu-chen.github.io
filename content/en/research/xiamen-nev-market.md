+++
title = 'What matters to Xiamen EV buyers?'
description = 'An Xiamen consumer-research project combining 8,058 online comments with a 368-response survey, text analysis, and consumer-feature analysis.'
category = 'COMPUTATIONAL SOCIAL SCIENCE · MARKET RESEARCH'
status = 'Student research project'
period = 'Xiamen, China · questionnaire n = 368'
visual = 'literature'
weight = 5
chart = 'ev'
inlineCharts = true
sourceDocument = '厦门市新能源汽车市场调研.docx'
figureAlt = 'Report-based charts on cohort composition, analysis stages, and quantitative results.'
figureCaption = 'Values transcribed from the supplied manuscript or report. Arithmetic reconstructions are labeled; these charts do not represent a new analysis of raw data.'
+++
## Project question and my contribution

What do consumers discuss about new-energy vehicles, and which characteristics are associated with purchase intention in the Xiamen survey? This student project combines online text analysis, field questionnaires, consumer segmentation, and shop observation. My listed responsibilities are text mining, Random Forest feature analysis, questionnaire design, clustering, and LDA topic modeling.

## Data sources and field design {#research-data}

| Source | Reported size | What it contributes |
| --- | ---: | --- |
| Cleaned online texts | 8,058 | Product vocabulary, sentiment, topic interpretation |
| Distributed questionnaires | 403 | Formal survey fieldwork |
| Valid questionnaires | 368 | Descriptive and consumer-feature analysis |
| Shop-observation interviews | 10 | Qualitative purchase-process context |

The report describes collecting vehicle-related Weibo texts and removing advertising and other irrelevant content. Text mining informed the questionnaire before fieldwork. The survey combines district-level stratification with population-proportional selection of streets or townships, followed by systematic street-intercept recruitment. All six Xiamen districts were included, with 13 selected streets. The abstract calls the design three-stage, while the detailed methods explicitly describe two recruitment stages; achieved representativeness is not established by those labels alone.

The reliability table appears in the pilot-survey section and reports a 20-response, eight-item scale, Cronbach’s α = 0.895, and KMO = 0.715. These figures should not be described as reliability estimates from all 368 formal responses. The formal questionnaire yield is 91.32%.

## Analytical methods {#research-methods}

Chinese tokenization and word-frequency analysis summarize salient product terms. Sentiment scoring classifies online texts as positive, neutral, or negative. LDA identifies five interpretable topic groups; their keywords guide questionnaire design rather than measuring every resident’s priorities.

Descriptive statistics and contingency-table tests examine survey responses. A scikit-learn Random Forest uses occupation, income, education, age, and gender as features and purchase intention as the response; feature importance summarizes the fitted model. The detailed clustering section uses a five-cluster K-means analysis, although the abstract also mentions k-modes. Shop observation contributes qualitative context about information needs, trust, and service expectations.

## Main results {#research-results}

The report classifies 4,027 texts as positive, 1,950 as neutral, and 2,081 as negative: 50.0%, 24.2%, and 25.8% after rounding. The selected word-frequency entries highlight experience, intelligence, price, price cuts, technology, space, and functions.

{{< research-results >}}

### Topics and consumer features

The actual LDA interpretation table labels its five groups passenger experience, price, performance, appearance, and safety. It provides representative words but no numeric topic shares, so the topic cards do not imply prevalence or rank.

Occupation (0.297) and income (0.272) have the highest reported Random Forest importance, followed by education (0.172), age (0.166), and gender (0.091). These are model-specific scores, not causal effects or population purchase probabilities. Qualitative observations distinguish basic product-information questions from experienced consumers’ questions about offers and after-sales service.

### What remains unresolved in the report

The clustering methods describe 290 existing or prospective buyers, but the five profile counts are 91, 40, 14, 103, and 17, totaling 265. The 25-case gap is not reconciled. Word-frequency table totals also should not be treated as unique-comment denominators: terms can recur or co-occur, and some sentiment subtotals do not equal the listed term counts.

## Interpretation and limits {#research-limits}

Online commenters, street-intercept respondents, and ten shop interviewees are distinct samples. Return yield and pilot reliability do not establish population representation. The report’s mismatched cluster counts and inconsistent method labels need audit, and model performance is not independently validated here. The findings support project-level hypotheses about product communication and consumer segmentation, rather than city-wide forecasts or causal marketing effects.
