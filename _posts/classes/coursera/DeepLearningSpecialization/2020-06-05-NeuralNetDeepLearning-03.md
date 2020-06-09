---
title:  03 - Shallow neural networks
author:     Mario Garingo
keywords: deepLearningSpecialization, nndl
summary: Learn to build a neural network with one hidden layer, using forward propagation and backpropagation.
category: coursera
type: notes
sidebar: coursera_sidebar
---

## Neural Network Representation
![](nnRep2)
Previously we denote the features as X but for NN we typically use $$A^{[0]}$$ to denote the input layer.  Note that you don't count the input layer as part of the naming convention.  Only the number of hidden layers and the output layers.  When propagating through the NN you can think of it as applying regression algo over and over again.

![](nnRep3)


### Vectorizing
![](nnRep4)
> So, another way to think of this is that we have four logistic regression units there, and each of the logistic regression units, has a corresponding parameter vector, w. By stacking those four vectors together, you end up with this four by three matrix.

This is called $$W^{[1]}$$ as weights of the first hidden layer.

> When we're vectorizing, one of the rules of thumb that might help you navigate this, is that while we have different nodes in the layer, we'll stack them vertically.


>  So, just a recap, we figured out that z_[1] is equal to w_[1] times the vector x plus the vector b_[1], and a_[1] is sigmoid times z_[1]., marked from 6 minutes 30 seconds till 6 minutes 42 secondsSo, just a recap, we figured out that z_[1] is equal to w_[1] times the vector x plus the vector b_[1], and a_[1] is sigmoid times z_[1].

![](nnRep5)

> this last upper unit is a lot like logistic regression, except that instead of writing the parameters as w and b, we're writing them as w_[2] and b_[2], with dimensions one by four and one by one.