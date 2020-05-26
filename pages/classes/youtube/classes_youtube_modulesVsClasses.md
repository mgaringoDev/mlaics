---
title: Python - Object-Oriented Programming Tutorial Modules Versus Classes
sidebar: youtube_sidebar
permalink: classes_youtube_modulesVsClasses.html
folder: classes
---

This note looks at the differences between Modules vs Classes.  These notes pertain to the O'Rilley YouTube video.

[O'Reilly](https://www.youtube.com/watch?v=NmiwZ4y1iiM)

<iframe width="560" height="315" src="https://www.youtube.com/embed/NmiwZ4y1iiM" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Modules vs Classes
- Pyton __modules__ are files that contain Python code
- Python modules can be executed or imported
- Modules can contain class definitions
- Sometimes a module consists of a single class; in this case a module may seem synonymous with a class.

### Module 
Lets say you have a module called mymod.

```python
var = 10

def dothis():
	print("I did this")
```

Recall that module is just python code.  So you can do the following to import this

```python
import mymod
```

OR assigning a variable to the module

```python
import mymod as mm
```

OR using variables directly

```python
from mymod import var, dothis
```


### Classes 
Lets say you have a module called ```decimal``` with a class called ```Decimal```. You can do something like this.  

{{site.data.alerts.warning}}
Notice that case matters.
{{site.data.alerts.end}}

```python
from decimal import Decimal

print( Decimal('3.5') + Decimal('4.5'))
```

The above created 2 decimal objects.

