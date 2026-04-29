# Project NYPD Enforcement Gap

## Members
- Haeji Ahn <ahaeji925@uchicago.edu>
- Amy Lin <amyslin@uchicago.edu>
- Amanda Song <amandasong@uchicago.edu>

## Summary of Milestone 3 plans
We plan to use logistic regression to train our model. As we are working with SQF data, specifically involving the use of force by the NYPD, logistic regression would enable us to identify the variables which are more strongly associated with the probability of physical force and predict a binary outcome based on the given demographic and situational features (i.e., whether an individual would experience physical force if stopped), even if our data is not perfectly linearly separable. We complement this with L2 regularization to control the complexity of our model. Due to the nature of our topic, there may be multicollinearity between some features, which may be better handled by L2 regularization compared to others as it shrinks and distributes weights evenly between them, enabling more stable estimates. We will interpret our linear model by analyzing the sign and magnitude of weights, which represent the relationship between each feature and the log-odds of experiencing physical force. Positive weights indicate a higher likelihood , while negative weights indicate a lower likelihood. Larger-magnitude weights also suggest a stronger relationship with the use of physical force, while smaller-magnitude weights indicate a weaker relationship. Overall, the weights would enable us to identify if patterns on the use of physical force differ among demographics and other situational factors.

To analyze the performance of our model, we plan to evaluate both training and test accuracy given that our model is not too imbalanced (~20% positive labels), as well as the precision and recall of our model. We would place slightly greater emphasis on recall to minimize false negatives (i.e., cases where individuals experience physical force but are not predicted). We plan on organizing our code into a structured pipeline with the following separate modules in src (directory containing our source files), subject to change: 
1. clean_data.py: Filtering relevant columns and data cleaning 
2. feature_engineer.py: Feature extraction and categorical data encoding
3. model_train.py: Model training and tuning
4. analyze_performance.py: Model testing and performance analysis



### DELETE BELOW IF NOT NEEDED - responses below have been combined into the two paragraphs above

## Summarize your Milestone 3 plans in a paragraph or two. Include answers to the following questions.

## Which linear model did you pick? Why?
We plan to use logistic regression to train our model. As we are working with SQF data, specifically involving the use of force by the NYPD, logistic regression would enable us to identify the variables which are more strongly associated with the probability of physical force and predict a binary outcome based on the given demographic and situational features (i.e., whether an individual would experience physical force if stopped), even if our data is not perfectly linearly separable.

## Which regularizer did you pick? Why?
We complement this with L2 regularization to control the complexity of our model. Due to the nature of our topic, there may be multicollinearity between some features, which may be better handled by L2 regularization compared to others as it shrinks and distributes weights evenly between them, enabling more stable estimates.

## How do you plan on describing your linear model and its output? What do small or large weights mean? 
We will interpret our linear model by analyzing the sign and magnitude of weights, which represent the relationship between each feature and the log-odds of experiencing physical force. Positive weights indicate a higher likelihood , while negative weights indicate a lower likelihood. Larger-magnitude weights also suggest a stronger relationship with the use of physical force, while smaller-magnitude weights indicate a weaker relationship. Overall, the weights would enable us to identify if patterns on the use of physical force differ among demographics and other situational factors.

## What metrics will you use to analyze the performance of your model?
To analyze the performance of our model, we plan to evaluate both training and test accuracy given that our model is not too imbalanced (~20% positive labels), as well as the precision and recall of our model. We would place slightly greater emphasis on recall to minimize false negatives (i.e., cases where individuals experience physical force but are not predicted). 

## How do you plan on organizing your code for your project?
We plan on organizing our code into a structured pipeline with the following separate modules in src (directory containing our source files), subject to change: 
1. clean_data.py: Filtering relevant columns and data cleaning 
2. feature_engineer.py: Feature extraction and data encoding
3. model_train.py: Model training and tuning
4. analyze_performance.py: Model testing and performance analysis