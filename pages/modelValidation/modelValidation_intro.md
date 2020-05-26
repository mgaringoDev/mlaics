---
title: Introduction
sidebar: modelValidation_sidebar
permalink: modelValidation_intro.html
folder: modelValidation
---

## Overview

The recipe for supervised machine learning models if very simple:

1) Choose a class of model

2) Choose some model hyper-parameters

3) Fit the model to the training data

4) Use the model to predict un-seen or out-of-sample data

![](https://mermaid.ink/img/eyJjb2RlIjoiZ3JhcGggTFJcbiAgTW9kZWxTZWxlY3Rpb24gLS0-IEh5cGVyLVBhcmFtZXRlcnNcbiAgSHlwZXItUGFyYW1ldGVycyAtLT4gRml0TW9kZWxcbiAgRml0TW9kZWwgLS0-IFByZWRpY3ROZXdTYW1wbGVzXG4gIEZpdE1vZGVsLS0gdHVuaW5nIC0tPkh5cGVyLVBhcmFtZXRlcnNcbiAgRml0TW9kZWwgLS0-IE1vZGVsU2VsZWN0aW9uXG4gICBcblx0XHQiLCJtZXJtYWlkIjp7InRoZW1lIjoiZGVmYXVsdCJ9LCJ1cGRhdGVFZGl0b3IiOmZhbHNlfQ)

The most important part of this pipeline is the model selection and hyper-parameter tuning.  Therefore, in order to make an informed choice, we need a way to validate that our model and our hyper-parameters are a good fit to the data. While this may sound simple, there are some pitfalls that you must avoid to do this effectively. 

# Naives 
This is training and testing your model on the same dataset.  This leads to information leakage from the learning set to the testing set.  The algorithm basically learns the training data and because you are using the training data as a testing data the model will always give a higher than normal accuracy. 

An example of this is using KNN where **K** is equal to one.  

# Holdout Sets
This is basically **train_test_split** and **cross_validation**.  Where you withhold a portion of the observations to be used as a testing set to which you can identify the performance of the algorithm.  The remainder is used as a training set.

## Cross Validation
A sequence of fits where each subset of the data is used both as training set and as a validation set.

![](https://jakevdp.github.io/PythonDataScienceHandbook/figures/05.03-2-fold-CV.png)

### K-Fold
The performance can then be identified by taking the mean of the two trials.  This is essentially the basis of K-Fold validation.  Consider a 5-fold validation schema below.

![](https://jakevdp.github.io/PythonDataScienceHandbook/figures/05.03-5-fold-CV.png)

By repeating the validation across different subsets of the data gives better idea of the performance of the algorithm.  Usually K=5 and 10 based in the literature, but remember that the more the K the more computation and time it will take to perform validation.

Notice that if **K=N-1** where **N** is the number of samples this is what is known as **Leave-One-Out**. This type is mainly done when samples are really small.

Here is a visualization of the k-fold behavior.

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_cv_indices_0041.png)

Notice that cross-validation is not affected by class or groups.

### Leave One Out (LOO)
Each learning set is created by taking all the samples except for one for training the using the remaining sample as testing.

{{site.data.alerts.warning}}
- When compared with k-fold one builds __n__ samples > instead of __k__ dels, where $$n>k$$.> - Each model is trained on $$n-1$$ samp> les rather tha> n > $$(k-1)n/k$ 
- Computatio> nally expensive than k-fold
- Results usually have high variance as an estimator for > test error
{{site.data.alerts.end}}

#### Leave P Out (LPO)
Same methodology as LOO but instead of 1 sample you remove P samples.  For $$n$$ samples, this procedure $${n \choose p}$$. 


