---
title: Introduction
sidebar: featureReduction_sidebar
permalink: featureReduction_intro.html
folder: featureReduction
---

## Overview
A detailed overview can be found [here](https://www.kdnuggets.com/2015/05/7-methods-data-dimensionality-reduction.html)

{{site.data.alerts.todo}} 
- [ ] Missing Values Ratio
- [ ] Low Variance Filter
- [ ] High Correlation Filter
- [ ] Random Forests / Ensemble Trees
- [ ] Principal Component Analysis (PCA)
- [ ] Backward Feature Elimination
- [ ] Forward Feature Construction
{{site.data.alerts.end}}

## Comparisons

| Dimensionality Reduction                            | Reduction Rate | Accuracy on validation set | Best Threshold | AuC | Notes                                                                                                                                                                                                                                                                       |
|-----------------------------------------------------|----------------|----------------------------|----------------|-----|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Baseline                                            | 0%             | 73%                        | –              | 81% | Baseline models are using all input features                                                                                                                                                                                                                                |
| Missing Values Ratio                                | 71%            | 76%                        | 0.4            | 82% |                                                                                                                                                                                                                                                                             |
| Low Variance Filter                                 | 73%            | 82%                        | 0.03           | 82% | Only for numerical coloumns                                                                                                                                                                                                                                                 |
| High Correlation Filter                             | 74%            | 79%                        | 0.2            | 82% | No correlation available between numerical and nominal columns                                                                                                                                                                                                              |
| PCA                                                 | 62%            | 74%                        | –              | 72% | Only for numerical columns                                                                                                                                                                                                                                                  |
| Random Forrest / Ensemble Trees                     | 86%            | 76%                        | –              | 82% |                                                                                                                                                                                                                                                                             |
| Backward Feature Elimination + missing values ratio | 99%            | 94%                        | –              | 78% | Backward Feature Elimination and Forward Feature Construction are prohibitively slow  on high dimensional data sets. It becomes practical to use them, only if following other dimensionality reduction techniques, like here the one based on the number of missing values |
| Forward Feature Construction + missing values ratio | 91%            | 83%                        | –              | 63% | Same as backward feature elimination                                                                                                                                                                                                                                        |


