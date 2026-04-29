# Project NYPD Enforcement Gap

## Members
- Haeji Ahn <ahaeji925@uchicago.edu>
- Amy Lin <amyslin@uchicago.edu>
- Amanda Song <amandasong@uchicago.edu>

## Which linear model did you pick? Why?
logistics regression

## Which regularizer did you pick? Why?
L1/ L2

## How do you plan on describing your linear model and its output? What do small or large weights mean? 


## What metrics will you use to analyze the performance of your model?
Training and test accuracy (given that our model is not too imbalanced - xx positive labels, xx negative labels), precision, recall, F1 score (combination of both)

## How do you plan on organizing your code for your project?
clean_data.py: data cleaning and encoding, processing
feature_engineer.py: make new feature(feature extraction and transformation)
model_train.py: training and hyperparameter(lambda) tuning
evaluate_visualize.py: performance analysis