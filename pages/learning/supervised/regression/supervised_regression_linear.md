---
title: Linear Regression
sidebar: supervised_sidebar
permalink: supervised_regression_linear.html
mlType: linearRegression
infoType: note
folder: learning
---

## Overview
The model is a straight line in the form $$f(X)=y=mx+b$$.  We can use **sklearn.linear_model** module to obtain the m and b parameters given list of points [x,y].  The slope and intercept of the data are contained in the model's fit parameters, which in Scikit-Learn are always marked by a trailing underscore. Here the relevant parameters are **coef_** and **intercept_** of the model.

### Polynomial Basis Function 
One way to adapt linear regression to non-linear relationships between the variables is to transform the data according to some **basis funciton**.  The main idea is to take the multidimension linear model:

$$y=a_0+a_1x_1+a_2x_2+a_3x_3+...+a_nx_n$$

Now we let $$x_n=f_n(x)$$ where $$f_n()$$ is some transformation function.

For instance let $$f_n(x)=x^n$$, the our new model becomes a polynomial regression of the form:

$$y=a_0+a_1x+a_2x^2+a_3x^3+...+a_nx^n$$

Notice that this is still a linear regression because the coefficients $$a_0 - a_n$$ never multiple or divide one another, rather they are added.  The basic operation above effectively takes 1D **x** values and projected them into a higher dimension, so that a linear fit can fir more complicated relationships between **x** and **y**.

### Gaussian Basis Functions
Polynomials are **global** basis functions, each affecting the prediction over the whole input space.  Sometimes, **local** basis functions are more appropriate. One example is using functions proportional to Gaussian probability density:

$$\phi_j(x) = exp(\frac{-(x-\mu_j)^2}{2s^2})$$

Like the polynomial basis function we can also do a sum of Gaussian bases.  Where s is the spacing between each Gaussian basis function.