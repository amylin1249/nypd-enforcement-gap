# Project NYPD Enforcement Gap

## Members
- Haeji Ahn <ahaeji925@uchicago.edu>
- Amy Lin <amyslin@uchicago.edu>
- Amanda Song <amandasong@uchicago.edu>

## Summarize your Milestone 3 plans in a paragraph or two. Include answers to the following questions.

## Which linear model did you pick? Why?
We plan to use logistics regression to train our model. 
Works well with datasets that are not perfectly linear

## Which regularizer did you pick? Why?
We complement this with L2 regularization, which will control the complexity of our model by shrinking weights evenly. Due to the nature of our project topic, there may be multicollinearity between some of our features, which may be better handled by L2 regularization compared to others as it distributes the weights between them, enabling more stable estimates.

## How do you plan on describing your linear model and its output? What do small or large weights mean? 


## What metrics will you use to analyze the performance of your model?
Training and test accuracy (given that our model is not too imbalanced with around 20% positive labels), precision, recall, F1 score (combination of both)

## How do you plan on organizing your code for your project?
To organize our code, the root will consist mainly of src (directory containing our source files), raw-data, and clean-data. Focusing on src, we plan to have the following key modules that eventually feed into __main__ (subject to change): 
1. clean_data.py: Filtering relevant columns and data cleaning 
2. feature_engineer.py: Feature extraction and data encoding
3. model_train.py: Model training and tuning
4. analyze_performance.py: Model testing and performance analysis