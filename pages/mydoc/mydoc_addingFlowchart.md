---
title: MermaidJS
last_updated: April 4, 2020
tags: [getting_started]
summary: "Adding flowchart"
sidebar: mydoc_sidebar
permalink: mydoc_addingFlowchart.html
folder: mydoc
---

## Adding Simple Graphs
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


## Adding Complex Graphs With HTML Elements

You first need to change the security level of mermaid by adding the following:
{% raw %}
```markdown
{% include addMermaidSecurity.html %}
```
{% endraw %}

At which point you can add nodes that have HTML elements.  These elements can include lists and also images.

### List Example
{% raw %}
```markdown
{% include addMermaidSecurity.html %}
{{site.data.mermaid.start}}
graph TD
	A[<b>Open I/O</b><li>Serial</li><li>File Mangement</li><li>Window</li>]

	C[<b>About the Protocol</b>]

	subgraph Stimulation
	G[<b>Baseline</b><li>Eyes Closed No Light</li><li>Eyes Open Light</li><li>Eyes Light</li><li>Eyes with Screen</li>]
	H[<b>Static</b><li>Crescent</li><li>Singleton</li><li>Pickup Sticks</li><li>Green and Red</li>]
	I[<b>Audio</b><li>Baby Cry</li>]
	J[<b>Dynamic</b><li>Checkerboard</li><li>V Checkerboard</li><li>Colour</li>]
	end

	M[<b>Brain Recovery from Stimulation</b>]

	R[<b>Close I/O and Save Recording</b>]

	A --> C
	C --> G
	C --> H
	C --> I
	C --> J
	G --> M
	H --> M
	I --> M
	J --> M
	M -->R
{{site.data.mermaid.end}}
```
{% endraw %}

Will render the following:

{% include addMermaidSecurity.html %}
{{site.data.mermaid.start}}
graph TD
	A[<b>Open I/O</b><li>Serial</li><li>File Mangement</li><li>Window</li>]

	C[<b>About the Protocol</b>]

	subgraph Stimulation
	G[<b>Baseline</b><li>Eyes Closed No Light</li><li>Eyes Open Light</li><li>Eyes Light</li><li>Eyes with Screen</li>]
	H[<b>Static</b><li>Crescent</li><li>Singleton</li><li>Pickup Sticks</li><li>Green and Red</li>]
	I[<b>Audio</b><li>Baby Cry</li>]
	J[<b>Dynamic</b><li>Checkerboard</li><li>V Checkerboard</li><li>Colour</li>]
	end

	M[<b>Brain Recovery from Stimulation</b>]

	R[<b>Close I/O and Save Recording</b>]

	A --> C
	C --> G
	C --> H
	C --> I
	C --> J
	G --> M
	H --> M
	I --> M
	J --> M
	M -->R
{{site.data.mermaid.end}}

## Configuration
The list of configurable elements can be found [here](https://mermaid-js.github.io/mermaid/#/mermaidAPI).
```html
<script>
  var config = {
    theme:'default',
    logLevel:'fatal',
    securityLevel:'strict',
    startOnLoad:true,
    arrowMarkerAbsolute:false,

    flowchart:{
      htmlLabels:true,
      curve:'linear',
    },
    sequence:{
      diagramMarginX:50,
      diagramMarginY:10,
      actorMargin:50,
      width:150,
      height:65,
      boxMargin:10,
      boxTextMargin:5,
      noteMargin:10,
      messageMargin:35,
      messageAlign:'center',
      mirrorActors:true,
      bottomMarginAdj:1,
      useMaxWidth:true,
      rightAngles:false,
      showSequenceNumbers:false,
    },
    gantt:{
      titleTopMargin:25,
      barHeight:20,
      barGap:4,
      topPadding:50,
      leftPadding:75,
      gridLineStartPadding:35,
      fontSize:11,
      fontFamily:'"Open-Sans", "sans-serif"',
      numberSectionStyles:4,
      axisFormat:'%Y-%m-%d',
    }
  };
  mermaid.initialize(config);
</script>
```

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

