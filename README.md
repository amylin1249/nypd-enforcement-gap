# NYPD Enforcement Gap

## Members
- Haeji Ahn <ahaeji925@uchicago.edu>
- Amy Lin <amsylin@uchicago.edu>
- Amanda Song <amandasong@uchicago.edu>


## Abstract
The New York Police Department (NYPD) is the largest municipal police department in the United States and is known to have a large operating budget that is greater than the combined budgets of several other agencies in New York City. Our project aims to study enforcement patterns, specifically stop, question, and frisk (SQF) actions, and identify which stops lead to physical escalation based on key features in the dataset. We aim to answer the question: To what extent do demographic characteristics (e.g, race, age, sex) predict the use of physical force during a police encounter, after controlling for situational factors (e.g., location, why the stop was initiated, the suspected crime)?

Given the NYPD’s massive budget, finding evidence of a disparity in treatment would suggest that systemic bias, not underfunding, drives the escalation logic for law enforcement of different populations. Overall, the findings from our models would increase transparency on the NYPD’s use of force patterns and highlight any discrepancies in such actions across patrol boroughs to interrogate institutional accountability.


## Final Report
View the final report here: [NYPD Use of Force Final Report](https://drive.google.com/file/d/1thRrmlFTj4hrptw08muKC_4v_jTs68zo/view?usp=sharing)


## Setup and Execution
1. Clone this repository by running `git clone https://github.com/amylin1249/nypd-enforcement-gap.git` in your terminal, then `cd nypd-enforcement-gap`.
2. Run `uv sync` in the project root directory to install the required packages and set up the virtual environment.
3. *[Optional -- these files should already be included in the repository]* To regenerate the clean data file, run `uv run python -m src` in the root directory.
4. To load our models, please first navigate to our *src* directory by running `cd src/`. Then, run the relevant command below for each model implementation:  
    a. Linear model: `code train_linear_model.ipynb`  
    b. Non-linear model: `code train_nonlinear_model.ipynb`  
    c. Neural network: `code train_neural_network.ipynb`
5. To run the code for our models, please click *Run All* within the respective Jupyter notebook.


## Data Sources
### Data Source 1: NYPD Stop, Question and Frisk Data -- 2025 Excel file
https://www.nyc.gov/site/nypd/stats/reports-analysis/stopfrisk.page

### Data Source 2: NYC Mayor's Office of Criminal Justice -- NYC Youth Crime in Context: Arrest & Recidivism
https://criminaljustice.cityofnewyork.us/reports/nyc-youth-crime-in-context-arrest-recidivism/


## Acknowledgments
Many thanks to our CAPP30254 instructor, Hannah Morgan, and our assigned TA, Mauro Ttito, for their support and guidance.
