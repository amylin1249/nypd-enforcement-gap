# Project NYPD Enforcement Gap

## Members
- Haeji Ahn <ahaeji925@uchicago.edu>
- Amy Lin <amyslin@uchicago.edu>
- Amanda Song <amandasong@uchicago.edu>

## Summary of Milestone 4 plans
In short paragraphs, summarize your Milestone 4 plans. Answer the following questions:

### How much progress have you made on your project so far? 
We have made considerable progress on our project thus far, with data cleaning completed and substantial progress made on our linear model (logistic regression). We have implemented functions to split our data into training and testing sets, and conducted cross-validation to tune our hyperparameter using different metrics such as precision and recall. Using the “best” hyperparameter under each metric, we generated and analyzed coefficients for our features. Moving forward, we will still have to determine which metric is most appropriate for tuning our hyperparameter and evaluate our model on the test set.

### Which nonlinear model did you pick? Why?
Among the two nonlinear models covered in class (i.e., K-Nearest Neighbors, decision trees), we picked decision trees. Given the size and complexity of our dataset, decision trees would be well-suited to model nonlinear relationships among our features. They are also less sensitive to outliers and would be able to identify the most significant features during training. To address the instability associated with one decision tree, we plan to enhance the model by implementing the random forest algorithm, aggregating predictions across multiple trees to improve performance. 

While K-Nearest Neighbors (KNN) is relatively easy to interpret, it may be less suitable for our classification problem due to the curse of dimensionality. As our model includes many features, distance calculations in KNN may be less meaningful in a high-dimensional space, making the algorithm less effective in its predictions. 

As for the neural network, we will select an architecture that aligns with our classification problem.

### How will you interpret the model's results?


### What metrics will you use to analyze the performance of your model?


### How are you organizing the code for your project?
Building on code organization from Milestone 3, we have organized our code into a structured pipeline with the following separate modules in src (directory containing our source files), subject to change: 
1. clean_data.py: Data cleaning, including feature extraction
2. train_linear_model.py: Linear (logistic) model training and tuning
3. train_nonlinear_model.py: Nonlinear (decision tree) model training and tuning
4. train_neural_network.py: Neural network training and tuning
5. analyze_performance.py: Model testing and performance analysis – *may be split into further sub-files if needed*
Note that we have get_basic_stats.py inside src from milestone2, but it is not a part of the pipeline.