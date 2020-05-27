---
title: Bibliography and bibtex
tags: [formatting]
summary: "Setting up the bibtex integration in jekyll."
sidebar: mydoc_sidebar
permalink: mydoc_bib.html
folder: mydoc
---

## Jekyll Plug-in
I used the [jekyll-scholar](https://gist.github.com/roachhd/ed8da4786ba79dfc4d91) plugin.

For more reading look at:

- [Jekyll and BibTex](https://pages.lip6.fr/Pascal.Poizat/blog/posts/2016/02/01/jekyll-and-bibtex/)
- [citation-style-language](https://github.com/citation-style-language/styles)

## Configuration
To configure the plug-in you have to add the following in the ```_config.yml``` file.

```yaml
# the styles can be found here: https://github.com/citation-style-language/styles
scholar:  
  style: _bibliography/ieee.csl
  bibliography: mybib.bib
  bibliography_template: bib
```

Everything is self explanatory except for the ```bibliography_template``` which is the layout for when you call ```{% raw %}{% bibliography --cited %}{% endraw %}```.

## Usage

### Step 1
Update the bib file.

### Step 2
Add citation to the note using,

{% raw %}
```
{% cite __key__ %}
```
{% endraw %}

where ```__key__``` is the key to that specific item in the ```bib``` file.

### Step 3
Add reference to the bottom of the note using,
{% raw %}
```
{% bibliography --cited %}
```
{% endraw %}


OR

{% raw %}
```
{% include addRef.html %}
```
{% endraw %}

