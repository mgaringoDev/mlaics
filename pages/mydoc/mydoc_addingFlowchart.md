---
title: MermaidJS
last_updated: April 4, 2020
tags: [getting_started]
summary: "Adding flowchart"
sidebar: mydoc_sidebar
permalink: mydoc_addingFlowchart.html
folder: mydoc
---

To add [mermaid flow charts](https://mermaid-js.github.io/mermaid/#/flowchart) all you have to do is place the following set of liquid code in your md file.

{% raw %}
```markdown
{{site.data.mermaid.start}}

{{site.data.mermaid.end}}
```
{% endraw %}

Then place your mermaid graph in between the liquid code and it will render a flow chart automatically.  An example diagram can be seen below with the graph.

```html
graph LR
    A[Hard edge] -->|Link text| B(Round edge)
    B --> C{Decision}
    C -->|One| D[Result one]
    C -->|Two| E[Result two]
```

{{site.data.mermaid.start}}
graph LR
    A[Hard edge] -->|Link text| B(Round edge)
    B --> C{Decision}
    C -->|One| D[Result one]
    C -->|Two| E[Result two]
{{site.data.mermaid.end}}

## Types of Charts
There are several charts you can create using mermaid.
- [Flowchart](https://mermaid-js.github.io/mermaid/#/flowchart)
- [Sequence Diagrams](https://mermaid-js.github.io/mermaid/#/sequenceDiagram)
- [Class Diagrams](https://mermaid-js.github.io/mermaid/#/classDiagram)
- [State Diagram](https://mermaid-js.github.io/mermaid/#/stateDiagram)
- [Entity Relationship Diagrams](https://mermaid-js.github.io/mermaid/#/entityRelationshipDiagram)
- [Gantt](https://mermaid-js.github.io/mermaid/#/gantt)
- [Pie Chart](https://mermaid-js.github.io/mermaid/#/pie)

## Live Editor
The live editor can be found [here](https://mermaid-js.github.io/mermaid-live-editor/).  Just copy paste the content in the mermaid liquid tags.

