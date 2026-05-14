# Project NYPD Enforcement Gap

## Members
- Haeji Ahn <ahaeji925@uchicago.edu>
- Amy Lin <amyslin@uchicago.edu>
- Amanda Song <amandasong@uchicago.edu>

## Summary of Milestone 4 plans
In short paragraphs, summarize your Milestone 4 plans. Answer the following questions:

### How much progress have you made on your project so far? 
We have made considerable progress on our project thus far, with both our data cleaning completed and our linear model (logistic regression) nearly completed. For the linear model, we split our data into training and testing sets, conducted 5-fold cross-validation to tune our hyperparameters (best C value to maximize recall, and penalty term). We generated coefficients for our features with the training set, and we will need to evaluate our model on the testing set.

### Which nonlinear model did you pick? Why?
Among the two main nonlinear models covered in class (K-Nearest Neighbors and decision trees), we picked decision trees. Given the size and complexity of our dataset, decision trees would be well-suited to model nonlinear relationships among our features. They are also less sensitive to outliers and would be able to identify the most significant features during training. To address the instability associated with one decision tree, we plan to enhance the model by implementing the random forest algorithm, aggregating predictions across multiple trees to improve performance. 

While K-Nearest Neighbors (KNN) is relatively easy to interpret, it may be less suitable for our classification problem due to the curse of dimensionality. Because our model includes many features, distance calculations in KNN may be less meaningful in a high-dimensional space, making the algorithm less effective in its predictions. 

As for the neural network, we will select an architecture that aligns with our classification problem.

### How will you interpret the model's results?
The first thing we will look at in our decision tree result is what feature sits at the root node; this represents the feature that most predicts use of force on an individual. We will then follow the path of the decision tree to see how different factors (location, race, age, etc.) combine to create a higher risk of having force used. We will also use the feature_importances_ attribute to see how much each feature contributes to reducing node impurity. 

### What metrics will you use to analyze the performance of your model?
To analyze the performance of our model, we plan to primarily focus on recall. Recall is especially important as we aim to minimize false negatives (i.e., cases where individuals experience physical force but are not predicted). False negatives could understate the severity of the use of force by the NYPD on certain individuals or demographic groups, potentially diluting the need for police accountability and the overall relevance of the issue to policymakers. Secondarily, we will use the F1 score to balance recall with precision to ensure that our model does not produce an excessive number of false positives while we focus on minimizing false negatives. We do not plan to rely on accuracy as a metric because our dataset is imbalanced (~20% positive labels).

### How are you organizing the code for your project?
Building on code organization from Milestone 3, we have organized our code into a structured pipeline with the following separate modules in src (directory containing our source files), subject to change: 
1. clean_data.py: Data cleaning, including feature extraction
2. train_linear_model.py: Linear (logistic) model training and tuning
3. train_nonlinear_model.py: Nonlinear (decision tree) model training and tuning
4. train_neural_network.py: Neural network training and tuning
5. analyze_performance.py: Model testing and performance analysis – *may be deleted if this is incorporated into our other files*
Note that we have get_basic_stats.py inside src from milestone2, but it is not a part of the pipeline.