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
![](https://drive.google.com/uc?id=1X7bPRB36Xa4cP0f-OMTIxJmtdH5L4d_0)
Previously we denote the features as X but for NN we typically use $$A^{[0]}$$ to denote the input layer.  Note that you don't count the input layer as part of the naming convention.  Only the number of hidden layers and the output layers.  When propagating through the NN you can think of it as applying regression algo over and over again.
![](https://drive.google.com/uc?id=1oIHngm5wuP_FfKTo0cKQmmGknYLWagCK)



## Vectorizing
![](https://drive.google.com/uc?id=1EkYTUhxC2jtt1m-1YNeO4dq5GTl24Xjf)

> So, another way to think of this is that we have four logistic regression units there, and each of the logistic regression units, has a corresponding parameter vector, w. By stacking those four vectors together, you end up with this four by three matrix.

This is called $$W^{[1]}$$ as weights of the first hidden layer.

> When we're vectorizing, one of the rules of thumb that might help you navigate this, is that while we have different nodes in the layer, we'll stack them vertically.


>  So, just a recap, we figured out that z_[1] is equal to w_[1] times the vector x plus the vector b_[1], and a_[1] is sigmoid times z_[1]., marked from 6 minutes 30 seconds till 6 minutes 42 secondsSo, just a recap, we figured out that z_[1] is equal to w_[1] times the vector x plus the vector b_[1], and a_[1] is sigmoid times z_[1].

![](https://drive.google.com/uc?id=1806pw2k5qifiP9Oogjmf-as-J1iIRLC-)

> this last upper unit is a lot like logistic regression, except that instead of writing the parameters as w and b, we're writing them as w_[2] and b_[2], with dimensions one by four and one by one.

![](https://drive.google.com/uc?id=1B7piiGlCJG3WyW13-2H2EMbbuHX1hUWy)

```X``` is defined by horizontal concatenation of all the training samples.  Similarly, you can do that for $$Z^{[1]} , Z^{[1]} , Z^{[2]} , A^{[2]}$$ where the column corresponds to the activation of each sample and the row corresponds to its subsequent node activation.

> the analogy is that we went from lower case vector xs to just capital case X matrix by stacking up the lower case xs in different columns.

>  horizontal index corresponds to different training example, when you sweep from left to right you're scanning through the training cells.

> vertically the different indices in the matrix A corresponds to different hidden units.

### Justification
![](https://drive.google.com/uc?id=1tL9uiiVOm6VgPbFmwAs9X3DkQuyXXUJ5)

> When you took the different training examples and stacked them up in different columns, then the corresponding result is that you end up with the z's also stacked at the columns.

> So on this slide, I've only justified that z1 equals w1x plus b1 is a correct vectorization of the first step of the four steps we have in the previous slide, but it turns out that a similar analysis allows you to show that the other steps also work on using a very similar logic.

![](https://drive.google.com/uc?id=17Y_3KSBbrZkDMPLNLzvgAy-S64sDbDjj)
> So this kind of shows that the different layers of a neural network are roughly doing the same thing or just doing the same computation over and over.


## Activation Functions
![](https://drive.google.com/uc?id=1qLbIyEA1cxRJUkyExVdKVvkr5jwyI9Hv)
- So far we are using sigmoid, but in some cases other functions can be a lot better.
- Sigmoid can lead us to gradient decent problem where the updates are so low.
- Sigmoid activation function range is [0,1]
  `A = 1 / (1 + np.exp(-z)) # Where z is the input matrix`
- Tanh activation function range is [-1,1]   (Shifted version of sigmoid function)
  - In NumPy we can implement Tanh using one of these methods:
    `A = (np.exp(z) - np.exp(-z)) / (np.exp(z) + np.exp(-z)) # Where z is the input matrix`

    Or
    `A = np.tanh(z)   # Where z is the input matrix`
- It turns out that the **tanh activation usually works better than sigmoid activation function for hidden units because the mean of its output is closer to zero**, and so it centers the data better for the next layer.

> The one exception is for the output layer because if y is either 0 or 1, then it makes sense for y hat to be a number, the one to output that's between 0 and 1 rather than between minus 1 and 1.

> So the one exception where I would use the sigmoid activation function is when you are using binary classification, in which case you might use the sigmoid activation function for the output layer.

- Sigmoid or Tanh function disadvantage is that if the input is too small or too high, the slope will be near zero which will cause us the gradient decent problem by slowing it down.
- One of the popular activation functions that solved the slow gradient decent is the RELU function.
  `RELU = max(0,z) # so if z is negative the slope is 0 and if z is positive the slope remains linear.`
 
> in practice you could pretend the derivative, when z is equal to 0, you can pretend it's either 1 or 0 and then you kind of work just fine.

- So here is some basic rule for choosing activation functions, 
	- if your classification is between 0 and 1, use the output activation as sigmoid 
	- all other unites you should use RELU


- Leaky RELU activation function different of RELU is that if the input is negative the slope will be so small. It works as RELU but most people uses RELU.
  `Leaky_RELU = max(0.01z,z)  #the 0.01 can be a parameter for your algorithm.`

> And I know that for half of the range of z, the slope of ReLU is 0, but in practice, enough of your hidden units will have z greater than 0. Play video for highlighted transcript with text, So learning can still be quite fast for most training examples., marked from 7 minutes 39 seconds till 7 minutes 43 secondsSo learning can still be quite fast for most training examples.

{{site.data.alerts.warning}}
- In NN you will decide a lot of choices like:
  - No of hidden layers.
  - No of neurons in each hidden layer.
  - Learning rate.       (The most important parameter)
  - Activation functions.
  - And others..
- It turns out there are no guide lines for that. You should try all activation functions for example.
- It depends purely on the application and features.  

> And I think that by testing these different choices for your application, you'd be better at future-proofing your neural network architecture against the idiosyncracies of your problem, as well as evolutions of the algorithms.

{{site.data.alerts.end}}

## Why do you need non-linear activation functions?

- If we removed the activation function from our algorithm that can be called linear activation function.
- Linear activation function will output linear activations and so the output will just be a linear combination of your input features.
  - Whatever hidden layers you add, the activation will be always linear like logistic regression (So its useless in a lot of complex problems)

> Some of the cases that are briefly mentioned, it turns out that if you have a linear activation function here and a sigmoid function here, then this model is no more expressive than standard logistic regression without any hidden layer.

> So unless you throw a non-linearity in there, then you're not computing more interesting functions even as you go deeper in the network.

- You might use linear activation function in one place - in the **output layer** if the output is real numbers (regression problem). But even in this case if the output value is non-negative you could use RELU instead.  Or sometime even compression.

## Derivatives of activation functions
{{site.data.alerts.note}}

Check the notes below for derivations.

{{site.data.alerts.end}}

- Derivation of Sigmoid activation function:

  ```
  g(z)  = 1 / (1 + np.exp(-z))
  g'(z) = (1 / (1 + np.exp(-z))) * (1 - (1 / (1 + np.exp(-z))))
  g'(z) = g(z) * (1 - g(z))
  ```

- Derivation of Tanh activation function:

  ```
  g(z)  = (e^z - e^-z) / (e^z + e^-z)
  g'(z) = 1 - np.tanh(z)^2 = 1 - g(z)^2
  ```

- Derivation of RELU activation function:

  ```
  g(z)  = np.maximum(0,z)
  g'(z) = { 0  if z < 0
            1  if z >= 0  }
  ```

- Derivation of leaky RELU activation function:

  ```
  g(z)  = np.maximum(0.01 * z, z)
  g'(z) = { 0.01  if z < 0
            1     if z >= 0   }
  ```

## Gradient descent for Neural Networks
- In this section we will have the full back propagation of the neural network (Just the equations with no explanations).
- Gradient descent algorithm:
  - NN parameters:
    - `n[0] = Nx`
    - `n[1] = NoOfHiddenNeurons`
    - `n[2] = NoOfOutputNeurons = 1`
    - `W1` shape is `(n[1],n[0])`
    - `b1` shape is `(n[1],1)`
    - `W2` shape is `(n[2],n[1])`
    - `b2` shape is `(n[2],1)`
  - Cost function `I =  I(W1, b1, W2, b2) = (1/m) * Sum(L(Y,A2))`
  - Then Gradient descent:

    ```
    Repeat:
    		Compute predictions (y'[i], i = 0,...m)
    		Get derivatives: dW1, db1, dW2, db2
    		Update: W1 = W1 - LearningRate * dW1
    				b1 = b1 - LearningRate * db1
    				W2 = W2 - LearningRate * dW2
    				b2 = b2 - LearningRate * db2
    ```

- Forward propagation:

  ```
  Z1 = W1A0 + b1    # A0 is X
  A1 = g1(Z1)
  Z2 = W2A1 + b2
  A2 = Sigmoid(Z2)      # Sigmoid because the output is between 0 and 1
  ```

- Backpropagation (derivations):   
  ```
  dZ2 = A2 - Y      # derivative of cost function we used * derivative of the sigmoid function
  dW2 = (dZ2 * A1.T) / m
  db2 = Sum(dZ2) / m
  dZ1 = (W2.T * dZ2) * g'1(Z1)  # element wise product (*)
  dW1 = (dZ1 * A0.T) / m   # A0 = X
  db1 = Sum(dZ1) / m
  # Hint there are transposes with multiplication because to keep dimensions correct
  ```

For vectorization just stack them horizontally like before and treat them as matrices and apply the same tricks as before.

![](https://drive.google.com/uc?id=1ZH3-fLZszu92pNmyyzno2UJERyAKGP10)

## Random Initialization

- In logistic regression it wasn't important to initialize the weights randomly, while in NN we have to initialize them randomly.

- If we initialize all the weights with zeros in NN it won't work (initializing bias with zero is OK):
  - __all hidden units will be completely identical (symmetric)__ - compute exactly the same function
  - on each gradient descent iteration all the hidden units will always update the same

> both hidden the units have the same influence on the output unit.

- To solve this we __initialize the W's with a small random numbers__:

  ```
  W1 = np.random.randn((2,2)) * 0.01    # 0.01 to make it small enough
  b1 = np.zeros((2,1))                  # its ok to have b as zero, it won't get us to the symmetry breaking problem
  ```

- We need small values because in sigmoid (or tanh), for example, if the weight is __too large you are more likely to end up even at the very start of training with very large values of Z__. Which __causes your tanh or your sigmoid activation function to be saturated__, thus __slowing down learning__. If you don't have any sigmoid or tanh activation functions throughout your neural network, this is less of an issue.
  - These large values will cause the inputs of the tanh activation function to also be very large, which causes the gradients to be close to zero.  Which leads to slow small updates and creates a slower algorithm.

- Constant 0.01 is alright for 1 hidden layer networks, but if the NN is deep this number can be changed but it will always be a small number.