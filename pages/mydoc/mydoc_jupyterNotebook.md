---
title: Jupyter Notebook
tags: [formatting]
keywords: datatables, tables, grids, markdown, multimarkdown, jquery plugins
last_updated: May 21, 2020
summary: "Adding Jupyter notebooks to a page."
sidebar: mydoc_sidebar
permalink: mydoc_jupyterNotebook.html
folder: mydoc
notebookfilename:     test
---

There are 3 steps in adding jupyter notebook inside a note.

## Step #1: Add Jupyter File
Add the jupyter notebook file ```.ipynb``` inside the ```_data``` folder and rename it ```.json```.

{{site.data.alerts.warning}}
Make sure to place it in the same folder inside the ```jupyterNotebooks``` specified in the front matter.

```yaml
folder: mydoc
```
{{site.data.alerts.end}}


## Step #2: Add Front Matter
Add the file in the front matter.
```yaml
notebookfilename:     jupyterNotebook
```

## Step #3: Add Command
Add the command to render the Jupyter notebook in the note.

```ruby
{% raw %}
{% include jupyterNotebook.html %}  
{% endraw %}
```