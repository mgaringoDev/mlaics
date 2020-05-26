---
title: Artificial Neural Network Algorithms
sidebar: supervised_sidebar
permalink: supervised_ann_intro.html
folder: learning
---

{{site.data.alerts.todo}}
- **Artificial Neural Network Algorithms**
	- [ ] Perceptron
	- [ ] Multilayer Perceptrons (MLP)
	- [ ] Back-Propagation
	- [ ] Stochastic Gradient Descent
	- [ ] Hopfield Network
	- [ ] Radial Basis Function Network (RBFN)
{{site.data.alerts.end}}

# General Steps of a Neural Net

An entire neural net can be boiled down to the following steps

- Forward propagate the inputs through the network
- Compute error
- Update the weights and biases and perform forward propagations and error computations
- Repeat until desired number of iteration is achieved or the change in error is very small

# Mathematical Derivations

## Forward Propagations

### Input Layer to the Hidden Layer : L1 - L2

Where **$$z^{(2)}$$** is the **preactivation** of the synapse and **$$a^{(2)}$$** is the **activation**

\begin{align}
z^{(2)} = XW^{(1)} + b^{(2)} \\
\end{align}

$$
\begin{align}
a^{(2)} &= \sigma^{(2)}(z^{(2)}) \\
&= \tanh(z^{(2)})
\end{align}
$$

### Hidden Layer to Output Layer : L2 - L3

Where **$z^{(3)}$** is the **preactivation** of the synapse and **$a^{(3)}$** is the **activation**

\begin{align}
z^{(3)} = a^{(2)}W^{(2)} + b^{(3)} \\
\end{align}

\begin{align}
a^{(3)} &= \sigma^{(3)}(z^{(3)}) \\
&= softmax(z^{(3)})
\end{align}

Note that **$a^{(3)}$** is also the output of the NN which we can denote as **$\hat{y}$**

\begin{align}
a^{(3)} = \hat{y} = softmax(z^{(3)})\\
\end{align}

## Back Propagations

References:
- [Notes on Backpropagation](https://www.ics.uci.edu/~pjsadows/notes.pdf)
- [Machine Learning Cheat Sheet](https://ml-cheatsheet.readthedocs.io/en/latest/backpropagation.html#applying-the-chain-rule)
- [NN Softmax Activation](https://stats.stackexchange.com/questions/273465/neural-network-softmax-activation)
- [Backpropagation - softmac derivative](https://datascience.stackexchange.com/questions/32949/backpropagation-softmax-derivative)
- [DeepNotes](https://deepnotes.io/softmax-crossentropy)
- [Derivative of Softmax without cross entropy](https://math.stackexchange.com/questions/2843505/derivative-of-softmax-without-cross-entropy)
- [The softmax function and its derivative](https://eli.thegreenplace.net/2016/the-softmax-function-and-its-derivative/)
- [ML from scratch](http://www.wildml.com/2015/09/implementing-a-neural-network-from-scratch/)
- [Backpropagation with Softmax / Cross Entropy](https://stats.stackexchange.com/questions/235528/backpropagation-with-softmax-cross-entropy)
- [Derivative of Softmax loss function](https://math.stackexchange.com/questions/945871/derivative-of-softmax-loss-function)
- [How to implement softmax derivative](https://medium.com/@aerinykim/how-to-implement-the-softmax-derivative-independently-from-any-loss-function-ae6d44363a9d)

### Update $W^{(2)}$

We know that the output is just one giant equation which can be expressed as:

let C(x) be the cost function
\begin{align}
cost = C(\sigma^{(3)}(Z^{(3)}(a^{(3)}W^{(2)})))
\end{align}

To identify the derivative w.r.t $W^{(2)}$ we can perform the chain rule which leads to the following expression:

\begin{align}
cost = [C′(\hat{y})][\sigma^{(2)}′(z^{(3)})][Z′(W^{(2)})]
\end{align}

Based on the above equation it is now very easy to see how we can take the partial derivative of the cost function with respect to $W^{(2)}$ leading to the expression:

\begin{align}
\frac{\partial C}{\partial W^{(2)}} = 
\frac{\partial C}{\partial \hat{y}}  
\frac{\partial \hat{y}}{\partial z^{(3)}}  
\frac{\partial z^{(3)}}{\partial W^{(2)}}
\end{align}

Now we have three terms we can look at independently.

1. The first term looks at the partial derivative of the cost function **negative log likelihood** w.r.t to  $\hat{y}$ 

\begin{align}
\frac{\partial C}{\partial \hat{y}}  = 
\frac{\partial }{\partial \hat{y}}\big[ -\sum_{j}y_jlog(\hat{y}_j)\big]\\
\frac{\partial C}{\partial \hat{y}}  = 
y_j\frac{\partial }{\partial \hat{y}}\big[ \sum_{j}log(\hat{y}_j)\big]\\
\frac{\partial C}{\partial \hat{y}}  = 
\frac{y_j }{\hat{y}_j}\\
\end{align}

2. The second term is essentially the derivative of the activation function of the output layer w.r.t $z^{(3)}$.  Note that the activation function is given to **softmax** which is expressed as:

\begin{align}
softmax(z) = \frac{e^{z_i}}{\sum_{k=1}^N e^z_k}
\end{align}

Therefore we can express the second term as:

\begin{align}
\frac{\partial \hat{y}}{\partial z^{(3)}}   = \frac{\partial softmax}{\partial z^{(3)}}  = 
\frac{\partial }{\partial z^{(3)}}\frac{e^{z_i}}{\sum_{k=1}^N e^z_k}
\end{align}

where $j^{th}$ index of $k^{th}$ output

If we use the quotient rule, where the derivative of $f(x) = \frac{g(x)}{h(x)}$ is $f^\prime(x) = \frac{ g\prime(x)h(x) - h\prime(x)g(x)}{h(x)^2}$ we get

If j = k

\begin{align}
\frac{\partial  \frac{e^{z^{(3)}}}{\sum_{k=1}^N e^{z_k}}}{\partial z^{(3)}}&= \frac{e^{z^{(3)}} \sum_{k=1}^N e^{z_k} - e^{z^{(3)}}e^{z^{(3)}}}{\left( \sum_{k=1}^N e^{z_k}\right)^2} \\
&= \frac{e^{z^{(3)}} \left( \sum_{k=1}^N e^{z_k} - e^{z^{(3)}}\right )}{\left( \sum_{k=1}^N e^{z_k}\right)^2} \\
&= \frac{ e^{z^{(3)}} }{\sum_{k=1}^N e^{z_k} } \times \frac{\left( \sum_{k=1}^N e^{z_k} - e^{z^{(3)}}\right ) }{\sum_{k=1}^N e^{z_k} } \\
&= \hat{y}(1-\hat{y})
\end{align}

If j!=k

\begin{align}
\frac{\partial  \frac{e^{z^{(3)}}}{\sum_{k=1}^N e^{a_k}}}{\partial z^{(3)}}&= \frac{0 - e^{z^{(3)}}e^{z^{(3)}}}{\left( \sum_{k=1}^N e^{a_k}\right)^2} \\
&= \frac{- e^{z^{(3)}} }{\sum_{k=1}^N e^{a_k} } \times \frac{e^{z^{(3)}} }{\sum_{k=1}^N e^{a_k} } \\
&= - \hat{y}^2
\end{align}

Note that this will work but we can simplify the first two derivatives i.e. in general terms we can look at the cost function as it relates the the activation function. 

OR we can simultaneously look at the negative log likelihood of the softmax activation function as it relates to the activity in the output layer.

% 
\begin{align}
L &= - \sum_i y_i log(p_i) \\
\frac{\partial L}{\partial o_i} &= - \sum_k y_k \frac{\partial log(p_k)}{\partial o_i } \\
&= - \sum_k y_k \frac{\partial log(p_k)}{\partial p_k} \times \frac{\partial p_k}{ \partial o_i} \\
&= - \sum y_k \frac{1}{p_k} \times \frac{\partial p_k}{\partial o_i} \\
\end{align}

From the derivatives of the softmax we get

\begin{align}
\frac{\partial L}{\partial o_i}  &= -y_i(1-p_i) - \sum_{k\neq i} y_k \frac{1}{p_k}(-p_k.p_i) \\
&= -y_i(1-p_i) + \sum_{k \neq 1} y_k.p_i \\
&= - y_i + y_ip_i + \sum_{k \neq 1} y_k.p_i \\
&= p_i\left( y_i +  \sum_{k \neq 1} y_k\right) - y_i \\
&= p_i\left( y_i +  \sum_{k \neq 1} y_k\right)  - y_i
\end{align} 

Now note that y should be a [hot encoded vector](https://machinelearningmastery.com/why-one-hot-encode-data-in-machine-learning/) for the labels and so we can simplify the equation as:

\begin{align}
\frac{\partial L}{\partial o_i} = p_i - y_i\\
\frac{\partial C}{\partial z^{(3)}} = \hat{y} - y
\end{align}

Because the hot encoded vector $\sum_k y_k = 1$ and $y_i +  \sum_{k \neq 1} y_k = 1$

3. The final layer is just a linear relationship between the pre-activation and the weights and the slope of this linear relatinship is simply the activity in the hidden layer. Therefore we can express the final term as

\begin{align}
\frac{\partial z^{(3)}}{\partial W^{(2)}} = a^{(2)}
\end{align}

The final expression for the update is:

\begin{align}
\frac{\partial C}{\partial W^{(2)}} = \big[\hat{y} - y\big]a^{(2)}
\end{align}

\begin{align}
OR
\end{align}

\begin{align}
\frac{\partial C}{\partial W^{(2)}} &= \big[\frac{\partial C}{\partial \hat{y}}  \big] \big[\frac{\partial \hat{y}}{\partial z^{(3)}}  \big] \big[\frac{\partial z^{(3)}}{\partial W^{(2)}}\big]\\
&= \big[\frac{y}{\hat{y}}\big]\big[\hat{y}(1-\hat{y})\big]\big[a^{(2)}\big]
\end{align}

Therefore, there are two ways of implementing the update for the second set of weights using either equation 35 or equation 38. Note that $\big[\frac{\partial C}{\partial \hat{y}}  \big] \big[\frac{\partial \hat{y}}{\partial z^{(3)}}  \big] $ is sometimes refered to as **the backpropagating error or $\delta^{(2)}$** meaning that we can reduce the above equations to:

\begin{align}
\frac{\partial C}{\partial z^{(3)}} = \big[\delta^{(3)}\big]a^{(2)}\\
\end{align}

And because we know that we have perform a summation we can simplify this even more to

\begin{align}
\frac{\partial C}{\partial W^{(2)}} = a^{(2)T}\bullet\big[\delta^{(3)}\big]\\
\end{align}

### Update $b^{(3)}$

We can derive this by the same analytical reasoning as above.

\begin{align}
\frac{\partial C}{\partial b^{(3)}} = 
\frac{\partial C}{\partial z^{(3)}}  
\frac{\partial z^{(3)}}{\partial b^{(3)}}  
\end{align}

We know the first term is just the backpropagating error or $\delta^{(2)}$ and the second term is just 1 because deriving the preactivation function w.r.t to b will just give you 1.  The update value would just be

\begin{align}
\frac{\partial C}{\partial b^{(3)}} = \delta^{(3)}
\end{align}

### Update $W^{(1)}$

Performing the same analytical reasoning to we can represent $W^{(1)}$ in terms of cost function C(x) as:

\begin{align}
\frac{\partial C}{\partial W^{(1)}} = 
\frac{\partial C}{\partial \hat{y}}  
\frac{\partial \hat{y}}{\partial z^{(3)}}  
\frac{\partial z^{(3)}}{\partial \sigma^{(2)}}
\frac{\partial \sigma^{(2)}}{\partial a^{(2)}}
\frac{\partial a^{(2)}}{\partial W^{(1)}}
\end{align}

From the previous layet we know that the first two terms is just the propagration error of the previous layer.

\begin{align}
\frac{\partial C}{\partial \hat{y}}  
\frac{\partial \hat{y}}{\partial z^{(3)}}  = \delta^{(3)}
\end{align}

There third and forth terms are just the derivative of the forward propagation at that layer.  Which is the weight times the derivative of the activation function at that layer with respect to the activation.

\begin{align}
\frac{\partial z^{(3)}}{\partial \sigma^{(2)}} = W^{(2)}\\
\end{align}

\begin{align}
\frac{\partial \sigma^{(2)}}{\partial a^{(2)}} &= \sigma\prime^{(2)}(a^{(2)})\\
&= (1-tanh^2(a^{(2)}))
\end{align}


Finally the last term is just a linear relationship of the pre-activation of the hidden layer which is just the activation on the input layer.

\begin{align}
\frac{\partial a^{(2)}}{\partial W^{(1)}} = X
\end{align}

Therefore, the final update term is given by the equation

\begin{align}
\frac{\partial C}{\partial W^{(1)}} = 
\big[\delta^{(3)}\big]
\big[ W^{(2)}\big]
\big[(1-tanh^2(a^{(2)}))\big]
\big[X\big]
\end{align}

And because we have to perform a summation we can transpose W and X and perform the dot product using the following equation

\begin{align}
\frac{\partial C}{\partial W^{(1)}} = 
\big[X^T\big] \bullet 
\big[\big[\delta^{(3)}\big]\bullet
\big[ W^{(2)T}\big]
\big[(1-tanh^2(a^{(2)}))\big]\big]
\end{align}

Similar to the $W^{(2)}$ we can express the propagation error as

\begin{align}
\delta^{(2)} &= 
\frac{\partial C}{\partial \hat{y}}  
\frac{\partial \hat{y}}{\partial z^{(3)}}  
\frac{\partial z^{(3)}}{\partial \sigma^{(2)}}
\frac{\partial \sigma^{(2)}}{\partial a^{(2)}}\\
&=\big[\big[\delta^{(3)}\big]\bullet
\big[ W^{(2)T}\big]
\big[(1-tanh^2(a^{(2)}))\big]\big]
\end{align}

Simplifying equation 48 to

\begin{align}
\frac{\partial C}{\partial W^{(1)}} = 
X^T \bullet
\delta^{(2)}
\end{align}

### Updating $b^{(2)}$

From the previous reasoning of b^{(3)} we can say 

\begin{align}
\frac{\partial C}{\partial b^{(2)}} = \delta^{(2)}
\end{align}

### Final Update Equations

\begin{align}
W^{(2)} = W^{(2)}_{old} - learningrate * \frac{\partial C}{\partial W^{(2)}}\\
b^{(3)} = b^{(3)}_{old} - learningrate * \frac{\partial C}{\partial b^{(3)}}\\
W^{(1)} = W^{(1)}_{old} - learningrate * \frac{\partial C}{\partial W^{(1)}}\\
b^{(2)} = b^{(2)}_{old} - learningrate * \frac{\partial C}{\partial b^{(2)}}
\end{align}
