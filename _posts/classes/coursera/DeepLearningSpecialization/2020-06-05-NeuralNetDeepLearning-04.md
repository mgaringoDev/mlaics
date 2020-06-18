---
title:  04 - Deep Neural Networks
author:     Mario Garingo
keywords: deepLearningSpecialization, nndl
summary: Understand the key computations underlying deep learning, use them to build and train deep neural networks, and apply it to computer vision.
category: coursera
type: notes
sidebar: coursera_sidebar
---

## Deep L-layer neural network
![](typesOfNN)
- logistic regression is technically a 1 layer NN 
- Shallow NN is a NN with one or two layers.
- Deep NN is a NN with three or more layers.
	- many applications we don't know how deep to go
- We will use the notation `L` to denote the number of layers in a NN.
![](notationOfNN)
- `n[l]` is the number of neurons in a specific layer `l`.
- `n[0]` denotes the number of neurons input layer which is the same as `n[x]`. `n[L]` denotes the number of neurons in output layer.
- `g[l]` is the activation function.
- `a[l] = g[l](z[l])`
- `w[l]` weights is used for `z[l]`
- `x = a[0]`, `a[l] = y'`
- These were the notation we will use for deep neural network.
- So we have:
  - A vector `n` of shape `(1, NoOfLayers+1)`
  - A vector `g` of shape `(1, NoOfLayers)`
  - A list of different shapes `w` based on the number of neurons on the previous and the current layer.
  - A list of different shapes `b` based on the number of neurons on the current layer.

## Forward Propagation in a Deep Network

- Forward propagation general rule for one input:

{{site.data.alerts.warning}}
  ```
  z[l] = W[l]a[l-1] + b[l]
  a[l] = g[l](z[l])
  ```
{{site.data.alerts.end}}

- Forward propagation general rule for `m` inputs:

{{site.data.alerts.warning}}
  ```
  Z[l] = W[l]A[l-1] + B[l]
  A[l] = g[l](Z[l])
  ```
{{site.data.alerts.end}}
- `capitalized` letters are for vectorized implementation where you horizontally stack the corresponding `m` values for each of the `a`, `z`, and `b`

- notice that you need to compute activations for each layer 
	- We can't compute the whole layers forward propagation without a for loop so its OK to have a for loop here.

{{site.data.alerts.warning}}
- The dimensions of the matrices are so important you need to figure it out.
{{site.data.alerts.end}}

## Getting your matrix dimensions right

- The best way to debug your matrices dimensions is by a pencil and paper.

### Non-vectorized Approach
{{site.data.alerts.warning}}
- Dimension of `W[l]` is `(n[l],n[l-1])` . Can be thought by right to left.
- Dimension of `b[l]` is `(n[l],1)`
- `dw` has the same shape as `W`, while `db` is the same shape as `b`
- Dimension of `Z[l],` `A[l]`, `dZ[l]`, and `dA[l]`  is `(n[l],m)`
{{site.data.alerts.end}}

### Vectorized Approach
{{site.data.alerts.warning}}
- `Z[l]`, `A[l]` have the dimensions of `(n[l],m)`
- in backprop `dZ[l]`, `dA[l]` have the dimensions of `Z[l]`, `A[l]` which is `(n[l],m)`
{{site.data.alerts.end}}


## Why deep representations?
![](https://drive.google.com/uc?id=1e623OKnRndZQuMkMQ_E6KpszuYH3BMOs)
- Deep NN makes relations with data from simpler to complex. In each layer it tries to make a relation with the previous layer. E.g.:
	
	- 1) Face recognition application:  
		- first layer can be thought of feature detector and are simpler functions
		- subsequent layers will combine previous layers to create complex patterns     
		- > then composing them together in the later layers of a neural network so that it can learn more and more complex functions
		- >  one technical detail of this visualization, the edge detectors are looking in relatively small areas of an image, maybe very small regions like that.
		- > the main intuition you take away from this is just finding simple things like edges and then building them up
		- Image ==> Edges ==> Face parts ==> Faces ==> desired face

	- 2) Audio recognition application:
		- Audio ==> Low level sound features like (pitch,amplitude, white noise etc..) ==> Phonemes ==> Words ==> Sentences


- Neural Researchers think that deep neural networks "think" like brains (simple ==> complex)
- Circuit theory and deep learning:
	- circuit theory = using logic gates
	- example: generating XOR of each features
		- > in order to compute this XOR function, the hidden layer will need to be exponentially large, because essentially, you need to exhaustively enumerate our 2 to the N possible configurations of the input bits that result in the exclusive OR being either 1 or 0.  You end up needing a hidden layer that is exponentially large in the number of bits.
	- ![](https://drive.google.com/uc?id=1TFbz7MyGOor1JRLsY7Jas7jtmcwL5g3x)
- When starting on an application don't start directly by dozens of hidden layers. Try the simplest solutions (e.g. Logistic Regression), then try the shallow neural network and so on.

> over the last several years there has been a trend toward people finding that for some applications, very, very deep neural networks here with maybe many dozens of layers sometimes, can sometimes be the best model for a problem

## Building blocks of deep neural networks

- Forward and back propagation for a layer l:
  - ![](https://drive.google.com/uc?id=10L4hGW5qawevYbS1Ylm8kUFAwXbRbwFy)
- Deep NN blocks:
  - ![](https://drive.google.com/uc?id=1CWX7sspYwMAbUEPu8BIUlR40F7SWgUe8)

## Forward and Backward Propagation

- Pseudo code for forward propagation for layer l:

  ```
  Input  A[l-1]
  Z[l] = W[l]A[l-1] + b[l]
  A[l] = g[l](Z[l])
  Output A[l], cache(Z[l])
  ```

- Pseudo  code for back propagation for layer l:

  ```
  Input da[l], Caches
  dZ[l] = dA[l] * g'[l](Z[l])
  dW[l] = (dZ[l]A[l-1].T) / m
  db[l] = sum(dZ[l])/m                # Dont forget axis=1, keepdims=True
  dA[l-1] = w[l].T * dZ[l]            # The multiplication here are a dot product.
  Output dA[l-1], dW[l], db[l]
  ```

- If we have used our loss function then:

  ```
  dA[L] = (-(y/a) + ((1-y)/(1-a)))
  ```

- A lot of the magic comes from the data and not the lines of code.



## Parameters vs Hyperparameters
![])(iterationProcess)
- Main parameters of the NN is `W` and `b`
- __Hyper parameters (parameters that control the algorithm)__ are like:
  - Learning rate.
  - Number of iteration.
  - Number of hidden layers `L`.
  - Number of hidden units `n`.
  - Choice of activation functions.
  	- ReLU, tanh, sigmoid, leaky ReLU etc...
hyperparameter.
- __FUTURE__
	- On the next course we will see how to optimize hyperparameters.
	- momentum
	- minibatch size
	- regularization params
- You have to try values yourself of hyper parameters.
- In the earlier days of DL and ML learning rate was often called a parameter, but it really is (and now everybody call it) a 

{{site.data.alerts.warning}}

DEEP LEARNING is an empirical process (trail and error)

{{site.data.alerts.end}}


## Analogy Between the Brain

![](https://drive.google.com/uc?id=1-PSq11uVtxzcC9K82Qq308wfb6PS7BZv)
- very loose analogy with biological neuron which is a cell in the brain 
- node -> neuron
- weights -> axon 
- single neuron is more complex than what we think, its not just aggregate and fire and no real evidence that there exist some back prop process
- today DNN is very good at supervised learning and seeing patterns and that is as far as the human brain analogy goes because it is more complicated than we think


