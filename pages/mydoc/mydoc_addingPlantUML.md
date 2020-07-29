---
title: PlantUML
tags: [getting_started]
summary: Adding flowchart using PlantUML
sidebar: mydoc_sidebar
permalink: mydoc_addingPlantUML.html
folder: mydoc
pdfFile: http://pdf.plantuml.net/PlantUML_Language_Reference_Guide_en.pdf
---

## Adding Simple Graphs
To add [PlantUML charts](https://plantuml.com/) all you have to do is place the following set of liquid code in your md file.  For more information go to the repo [here](https://github.com/zhustec/jekyll-diagrams).

{% raw %}
```markdown
{% plantuml %}

{% endplantuml %}
```
{% endraw %}

Then place your mermaid graph in between the liquid code and it will render a flow chart automatically.  An example diagram can be seen below with the graph.

```html
@startuml
start
:ClickServlet.handleRequest();
:new page;
if (Page.onSecurityCheck) then (true)
  :Page.onInit();
  if (isForward?) then (no)
    :Process controls;
    if (continue processing?) then (no)
      stop
    endif

    if (isPost?) then (yes)
      :Page.onPost();
    else (no)
      :Page.onGet();
    endif
    :Page.onRender();
  endif
else (false)
endif

if (do redirect?) then (yes)
  :redirect process;
else
  if (do forward?) then (yes)
    :Forward request;
  else (no)
    :Render page template;
  endif
endif

stop
@enduml
```

{% plantuml %}
@startuml
@startuml
start
:ClickServlet.handleRequest();
:new page;
if (Page.onSecurityCheck) then (true)
  :Page.onInit();
  if (isForward?) then (no)
    :Process controls;
    if (continue processing?) then (no)
      stop
    endif

    if (isPost?) then (yes)
      :Page.onPost();
    else (no)
      :Page.onGet();
    endif
    :Page.onRender();
  endif
else (false)
endif

if (do redirect?) then (yes)
  :redirect process;
else
  if (do forward?) then (yes)
    :Forward request;
  else (no)
    :Render page template;
  endif
endif

stop
@enduml
{% endplantuml %}

## Configuration
The full documentation can be found [here](https://crashedmind.github.io/PlantUMLHitchhikersGuide/index.html).

## Types of Charts

PlantUML is a component that allows to quickly write :
- Sequence diagram
- Usecase diagram
- Class diagram
- Activity diagram (here is the legacy syntax)
- Component diagram
- State diagram
- Object diagram
- Deployment diagram 
- Timing diagram 

The following non-UML diagrams are also supported:
- Wireframe graphical interface
- Archimate diagram
- Specification and Description Language (SDL)
- Ditaa diagram
- Gantt diagram 
- MindMap diagram 
- Work Breakdown Structure diagram 
- Mathematic with AsciiMath or JLaTeXMath notation
- Entity Relationship diagram


## Live Editor
The live editor can be found [here](http://www.plantuml.com/plantuml/umla/PL5BRi8m4Dtx5BCa6mwGB8g4rAex12Umd1UmC7Ow7XTn-yOsZb1PPJBlepVFkoYQ9TsSAeFgzywQwmdywo3RY_QZmn4_2L4stQ1wZplD-en1sOasXsNQ1d-2IMpbiR_0N3kI2pnjX1CwHTG_IT_U5WkYhBJnC_1Ty_ZH-3vaTkPpC8YHJF32mSKigQAyiJw1vagn_lmc9ueIvZB2ZtPIgzh6GuYo2Xw8JT4YPhn698ABQAwld2-ibEh_2XwN5RZY5Qqsaru-dQghqjmOY35QXdbBr3UWdJaKbmLv2gVQtFib_RDJulfYW_f_HryJbYSamMrsMh2cRG5BWxlb9ztS7m00).  Just copy paste the content in the mermaid liquid tags.

