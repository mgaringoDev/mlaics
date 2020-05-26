---
title: Gradient Descent
sidebar: supervised_sidebar
permalink: supervised_regression_gradientDescent.html
folder: learning
---

## Gradient Decent

{{site.data.alerts.warning}}
- sensitivity of initialization
- may stay at saddle or local minimas
- step size problems
	- too large of a step size increases the time of convergence because may jump back and forth around the minima
	- too small step of a step size increases the time of convergence because the steps towards the minima are too small
	- some ways in practice to improve step size is to:
		- change it linearly by the iteration
		- Newton's method: look at the second derivative to identify the local curvature of the function and decide of how big or small a step to take in a particular direction
{{site.data.alerts.end}}

### Stochastic / Online Gradient Descent
The classic gradient decent breaks down to taking the sum squared errors of the residual and update based on the weights of each data point.  For stochastic gradient decent we chose a point at random and use that point to update the gradient $$\nabla J$$.  In practice you do some sort of random ordering of the data and go through this ordering sequentially updating the parameter $$\beta$$.  This has the property that on average over the data points the optima $$E[\nabla J_n(\beta)] = \nabla J_n(\beta) = 0$$

{{site.data.alerts.note}}

{{site.data.alerts.tip}}

Pros:
- Lots of data = many more updates per pass
- computationally faster especially at the beginning where the error is large.  After only a few passes the updates become significant to reduce the error because the decision plane will move closer to the data cluster in space.
{{site.data.alerts.end}}

{{site.data.alerts.warning}}

Cons:
- no longer strictly "descent" 
	- harder to debug
	- harder to asses convergence
	- stopping condition may be harder to evaluate
{{site.data.alerts.end}}

Remedy:
- Mini-batch Updates
{{site.data.alerts.end}}

