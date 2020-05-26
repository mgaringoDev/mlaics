---
title: Overview
sidebar: supervised_sidebar
permalink: supervised_regression_intro.html
folder: learning
---

{{site.data.alerts.todo}}
- **Regression Algorithms**
	- [ ] Ordinary Least Squares Regression (OLSR)
	- [x] Linear Regression
	- [ ] Logistic Regression
	- [ ] Stepwise Regression
	- [ ] Multivariate Adaptive Regression Splines (MARS)
	- [ ] Locally Estimated Scatterplot Smoothing (LOESS)
{{site.data.alerts.end}}

Linear regression models are a good starting point for regression tasks. Such models are popular because they can be fit very quickly, and are very interpretable. You are probably familiar with the simplest form of a linear regression model (i.e., fitting a straight line to data) but such models can be extended to model more complicated data behavior.  For simple linear regression there is, in fact, an optimal solution, however for high dimensional spaces there are none and we need to regard the problem as an optimization problem. Regression fits a function to the data set, so what we are trying to do is to find a representative function and fit to our data set. Learning takes place as finding the best possible - local optimum - values of the function parameters. Linearity refer to the fact that we are tying to fit either a straight line or a polynomial function (polynomial regression).

This is a **parametric method** which means that there exists a relationship which can be expressed as a **fixed equation form to relate y and X**.  Where y are the output variables or response, and **X** are the input variables also known as covariates, features, independent variables or predictors.  The general form for linear regression is:

$$ y = f(X) + \epsilon $$

Various methods use different $$f(X)$$ and are usually statistical methods.  $$\epsilon$$ are the error terms that independent of $$X$$.  Linear regression then simplifies to identifying the coefficients of $$f(X)$$ by minimizing error based on the given data.


