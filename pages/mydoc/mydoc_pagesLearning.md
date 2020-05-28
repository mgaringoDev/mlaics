---
title: Pages - Learning
tags: [getting_started, formatting, content_types]
keywords: pages, authoring, exclusion, frontmatter
summary: "This shows how to set up pages for content used for each learning algorithm."
sidebar: mydoc_sidebar
permalink: mydoc_pagesLearning.html
folder: mydoc
---

{{site.data.mermaid.start}}
graph LR
	A(Algo-Family)
	a(To Do)
	b(General Thinking)
	c(Add to Sidebar)	

	B(Algo Sub Family HUB)	
	w(include hub.html)
	d(algoType)

	C(Sub Family Front Matter)	
	e(mlType)
	f(infoType)
	g(note)
	h(implementation)
	i(ref)

    A --> a
    a --> b
    b --> c

    A --> B
    B --> w
    w --> d

    B --> C    
    C --> e
    e --> f
    f --> g
    f --> h
    f --> i

{{site.data.mermaid.end}}


## Overview of the Family of Algorithm
Here create a __To Do__ section to keep track of what you need to do.

Also create the overall thinking behind this algorithm.

## Sub - Algorithm
For each individual family of algorithm there are sub families of algorithms where need a hub page.

In this hub page you need to include the ```hub.html``` with an appropriate ```algoType``` variable unique to that sub family algorithm.  

{% raw %}
```yaml
---
title: Linear Regression Hub
sidebar: supervised_sidebar
permalink: supervised_regression_linear_hub.html
folder: learning
---

{% include hub.html algoType="linearRegression" %}
```
{% endraw %}

## Add HUB to Sidebar
After creating this hub page, you need to add it to the sidebar so that it can be accessed.

## Adding Front Matter
The above hub page will gather all the pages with the key work that is passed to the ```algoType``` variable.  This is what links all the same type of sub-family algorithm.  In the front matter of the page there should be a variable called ```mlType``` which is the same as this ```algoType```.  So for the above section it will gather all sites with the ```mlType = linearRegression```.

```yaml
mlType: linearRegression
```

## Sorting Info Type
Each page is further divided into:
- __Notes:__ All notes associated with this particular sub family algorithm.
- __Implementation:__ All codes associated with this particular sub family algorithm.  This can include jupyter notebooks or raw python code.
- __References:__ All references pertaining to this algorithm that I used when creating notes and implementation. 

Continuing this example we need to add the following in the front matter.

### Note
```yaml
mlType: linearRegression
infoType: note
```
__OR__

### Implementation
```yaml
mlType: linearRegression
infoType: implementation
```

__OR__

### References
```yaml
mlType: linearRegression
infoType: ref
```