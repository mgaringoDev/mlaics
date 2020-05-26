---
title: Regularization
sidebar: supervised_sidebar
permalink: supervised_regression_regularization.html
folder: learning
---

## Regularization
Sometimes, though having many basis functions or polynomials can lead to more flexibility in the model.  The model quickly leads to over-fitting when this happens.  The reason is that the coefficients of adjacent basis functions blow up and cancel each other out.  We need to limit such spike explicitly in the model by penalizing large values of the model parameters.  This introduction of penalty is called **regularization**.


### Ridge Regression (L2 Regularization)
This regularization penalizes the sum of squares (2-norms) of the model coefficients.

$$P = \alpha\sum_{N}^{n=1}\theta^2_n$$

here $$\alpha$$ is a free parameter that controls the strength of the penalty. You can think of this as controlling the complexity of the resulting model.  In the$$\lim_{\alpha\to 0}$$, we recover the standard linear regression results.  While the $$\lim_{\alpha\to\infty}$$ all model responses will be suppressed.

### Lasso Regression (L1 Regularization)
This regularization penalizes the sum of absolute values (1-norms) of the model coefficients.

$$P = \alpha\sum_{N}^{n=1}|\theta_n|$$

This type of regularization favours **sparse models** where possible, where it preferentially sets model coefficients to exactly zero.  With the lasso regression penalty, the majority of the coefficients are exactly zero, with the functional behavior being modeled by a small subset of the available basis functions.