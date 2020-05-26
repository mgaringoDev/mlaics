---
title: Course Summary
sidebar: dataSchool_sidebar
permalink: classes_dataSchool_sklearn_summary.html
summary: "What I learned and major take aways from the course"
folder: classes
---

## Summary
These are the things that I took away from taking this course:

- General summary of reading, processing, creating model, and validating the model
- Grid search was looked at
	- good use of the function 
- Pipeline was also looked at
	- creating pipeline is important because you can validate both the model and also the feature engineering portion

## Major Learning 

These are what I learned based on each of the section

[View Full Image of the pipeline](https://mermaid-js.github.io/mermaid-live-editor/#/view/eyJjb2RlIjoiZ3JhcGggVEJcbiAgICBzdWJncmFwaCBJbnN0YW50aWF0ZVxuICAgIEltcG9ydHMgLS0-IG1ha2VfY29sdW1uX3RyYW5zZm9ybWVyICAgIFxuICAgIG1ha2VfY29sdW1uX3RyYW5zZm9ybWVyICAgIFxuICAgIE1vZGVsIC0tPiBza2xlYW4uX21vZGVsX29mX2ludGVyc3RfXG4gICAgSHlwZXItUGFyYW1ldGVycyAtLT4gc2tsZWFuLl9tb2RlbF9vZl9pbnRlcnN0X1xuXG4gICAgbWFrZV9jb2x1bW5fdHJhbnNmb3JtZXIgLS0-IG1ha2VfcGlwZWxpbmVcbiAgICBza2xlYW4uX21vZGVsX29mX2ludGVyc3RfIC0tPiBtYWtlX3BpcGVsaW5lXG4gICAgZW5kXG5cbiAgICBzdWJncmFwaCBHcmlkU2VhcmNoLUNyb3NzVmFsaWRhdGVcbiAgICBtYWtlX3BpcGVsaW5lIC0tPiBHcmlkU2VhcmNoQ1YgICAgICBcbiAgICBtYWtlX3BpcGVsaW5lIC0tPiBSYW5kb21pemVkU2VhcmNoQ1YgIFxuICAgIGN2PWtmb2xkIFxuICAgIHBhcmFtX2dyaWQgXG4gICAgZW5kXG5cbiAgICBzdWJncmFwaCBEYXRhXG4gICAgZmVhdHVyZU1hdHJpeCAtLT4gbWFrZV9jb2x1bW5fdHJhbnNmb3JtZXJcbiAgICByZXNwb25zZVZlY3RvclxuICAgIGVuZFxuXG4gICAgc3ViZ3JhcGggT3B0aW1pemVkTW9kZWxcbiAgICBHcmlkU2VhcmNoQ1YgLS0-IGdyaWQuY3ZfcmVzdWx0c19cbiAgICBncmlkLmJlc3RfZXN0aW1hdG9yX1xuICAgIGdyaWQuYmVzdF9wYXJhbXNfXG4gICAgZ3JpZC5iZXN0X3Njb3JlXyAgICBcbiAgICBlbmQgICAgIiwibWVybWFpZCI6eyJ0aGVtZSI6ImRlZmF1bHQifSwidXBkYXRlRWRpdG9yIjpmYWxzZX0)

<div style=" overflow-x: scroll;">
{{site.data.mermaid.start}}
graph TB
    subgraph Instantiate
    Imports --> make_column_transformer    
    make_column_transformer    
    Model --> sklean._model_of_interst_
    Hyper-Parameters --> sklean._model_of_interst_

    make_column_transformer --> make_pipeline
    sklean._model_of_interst_ --> make_pipeline
    end

    subgraph GridSearch-CrossValidate
    make_pipeline --> GridSearchCV      
    make_pipeline --> RandomizedSearchCV  
    cv=kfold 
    param_grid 
    end

    subgraph Data
    featureMatrix --> make_column_transformer
    responseVector
    end

    subgraph OptimizedModel
    GridSearchCV --> grid.cv_results_
    grid.best_estimator_
    grid.best_params_
    grid.best_score_    
    end    
{{site.data.mermaid.end}}
</div>

# Genearl Pipeline
There are 4 steps in sklearn
1. import the class
2. instantiate the model 
    - this includes the tunning parameters
3. fit the model
4. predict

# Model Evaluation
Use the ```metrics``` module

# Cross-validation
Use the ```train_test_split``` module



