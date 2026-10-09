+++
title = 'Urban planning literature research'
description = 'A source-traceable research workflow, with a small local retrieval pilot and a planned cloud demo.'
category = 'LLM · NLP · RAG'
status = 'Final debugging & optimization'
period = 'Results through 8 October 2026'
weight = 1
visual = 'literature'
evidence = 'planning-literature'
+++
## What the project does

A literature-research application for urban planning that connects retrieval, screening, evidence organization, and LLM-assisted synthesis. It uses an existing model with a research corpus and workflow; it is not a claim to have trained a foundation model from scratch.

## Data science methods and outputs

| Method | Output | What it supports |
| --- | --- | --- |
| Lexical and semantic retrieval | Ranked records linked to source metadata | Finding relevant evidence in a research corpus |
| Citation and temporal context | Context for candidate evidence | Inspecting relevance and research development |
| Evidence matrix and source checking | Traceable claims and retained sources | Revising synthesis against its evidence |
| LLM-assisted synthesis | Structured review drafts and research prompts | Research assistance subject to source review |

The project is in final debugging and optimization, with a desktop research client and retrieval-service entry points already in place. A public cloud application will be linked after deployment.

## Existing pilot result

A 12-question local pilot dated 8 October 2026 compared Qwen3-4B-Thinking-2507 with and without database retrieval. The local assessment marked **10/12 retrieval-assisted answers correct**, versus **0/12 closed-book answers**. Two retrieval-assisted answers were marked missing and none incorrect; the closed-book condition had one missing and eleven incorrect answers.

{{< project-evidence >}}

This is a small, project-specific pilot assessed by a single model-based assessor, without expert validation. It does not establish broad benchmark performance or publication-grade reliability. The chart reproduces the saved pilot summary rather than rerunning inference.

## Planned cloud application

The intended online workflow is to enter a research question, inspect retrieved literature and source evidence, and review a generated synthesis. Cloud deployment and a public demo URL are pending. No live application link is shown until the deployed service is available.

## Result provenance

Local project documentation and `planning_thinking_benchmark_20261008/summary.json`. The pilot uses the project's local corpus and saved assessment; corpus size and production performance are not inferred from these twelve questions.
