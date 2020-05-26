---
title: Linear Regression Implementation
sidebar: supervised_sidebar
permalink: supervised_regression_linear_implementation.html
mlType: linearRegression
infoType: implementation
folder: learning
---

## skLearn
We can use **sklearn.linear_model** module to obtain the m and b parameters given list of points [x,y].  The slope and intercept of the data are contained in the model's fit parameters, which in Scikit-Learn are always marked by a trailing underscore. Here the relevant parameters are **coef_** and **intercept_** of the model. 

The **LinearRegression** module can also fit in multidimensional linear models of the form $$y=a_0+a_1x_1+a_2x_2+...$$ where multiple $$x$$  values are geometrically the same as fitting a plane to 3D or fitting hyper-plane in higher dimensions.  Though higher dimensions are harder to visualize.

The **PolynomialFeatures** module is also in sklearn. Gaussian Basis Functions is not implemented in sklearn but is implemented in the jupyter notebook below.

Regularization is implemented in sklearn by importing the module **Ridge** from **sklearn.linear_model**.

[skLearn Regression](https://github.com/mgaringoDev/mymlPlaygroundNotes/blob/master/notebooks/Supervised/Regression/skLearn%20Regression%20Imlementation.ipynb)

## From Scratch
Look at the following Jupyter notebooks:

- [Linear Multiple Regression](https://github.com/mgaringoDev/mymlPlaygroundNotes/blob/master/notebooks/Supervised/Regression/Linear%20Multiple%20Regression%20Regression%20From%20Scratch%20Matrix%20Approach%20.ipynb)
- [Linear Regression From Scratch Simple Approach](https://github.com/mgaringoDev/mymlPlaygroundNotes/blob/master/notebooks/Supervised/Regression/Linear%20Regression%20From%20Scratch%20Simple%20Approach.ipynb)
- [In Depth: Linear Regression](https://jakevdp.github.io/PythonDataScienceHandbook/05.06-linear-regression.html)
- [Machine Learning and Big Date](http://www.kareemalkaseer.com/books/ml/linear-regression-intro)
- [Think Stats: Probability and Statistics for Programmers](http://greenteapress.com/thinkstats/thinkstats.pdf)
- [Applied Data Science](https://columbia-applied-data-science.github.io/appdatasci.pdf)
- [Modeling Data with Linear Combinations of Basis Functions](http://www.utstat.utoronto.ca/~radford/sta414.S11/week1b.pdf)
- [Linear regression (2): Gradient descent](https://www.youtube.com/watch?v=WnqQrPNYz5Q)
- [Gradient Descent step by step](https://www.youtube.com/watch?v=sDv4f4s2SB8)
- [CrossValidated Forum Question](https://stats.stackexchange.com/questions/117556/understanding-gaussian-basis-function-parameters-to-be-used-in-linear-regression)