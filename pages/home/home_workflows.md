---
title: Workflows
summary: "Current workflow of project."
sidebar: home_sidebar
permalink: home_workflows.html
folder: home
toc: false
---

# Workflow
{{site.data.mermaid.start}}
stateDiagram
  
  LitReview --> Code
  Code --> LitReview
  Code --> jNotebook 
  Code --> pyModule
  jNotebook --> pyModule 
  pyModule --> jNotebook
  jNotebook --> roughNotes
  jNotebook --> Results

  pyModule -->  Documentation : run sphinx
  roughNotes --> Documentation : run makeDocs
  Results --> Documentation : run makeDocs

  Documentation --> PDF : run exportToPDF   
{{site.data.mermaid.end}}

# Daily Workflow
{{site.data.mermaid.start}}
stateDiagram
  
  jNotebook_Markdown --> pyModule
  jNotebook_Markdown --> notes : makeDocs.py
  jNotebook_Markdown --> results : makeDocs.py

  notes --> localDocs : makeDocs.py
  results --> localDocs : makeDocs.py
  pyModule --> localDocs : run sphinx
  

  localDocs --> jekyllServer
  localDocs --> updateGantt     
{{site.data.mermaid.end}}