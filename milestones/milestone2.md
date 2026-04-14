# Project NYPD Enforcement Gap

## Members
- Haeji Ahn <ahaeji925@uchicago.edu>
- Amy Lin <amyslin@uchicago.edu>
- Amanda Song <amandasong@uchicago.edu>

## Research Question
<INPUT RESEARCH QUESTION>

## Updated Proposal
Using data from the New York Police Department (NYPD), we are studying enforcement patterns, specifically stop, question, and frisk (SQF) actions, in New York City. We plan to analyze whether an arrest was made based on key features in the dataset, where our classification model will identify which stops lead to an arrest versus those that do not. By analyzing features such as how a stop was initiated, demographic information on the individual, suspected crime type, and location, we can see how these factors are associated with enforcement activity (or a lack thereof). Given the NYPD’s massive budget, finding evidence of an enforcement gap would suggest that systemic bias, as opposed to underfunding, drives the selection logic for law enforcement of different populations. The findings would increase transparency on the NYPD’s selective enforcement actions and highlight any discrepancies in such actions across precincts to interrogate institutional accountability. Machine learning enables us to analyze historical SQF data to identify if certain communities are systematically targeted by enforcement and to detect patterns of discretionary bias across precincts. This could also provide predictive insights on future enforcement actions, accounting for demographic and precinct-level factors as drivers of systemic outcomes.

## Dataset and Features
Our dataset is an Excel file from the NYPD's Stop, Question, and Frisk database, containing detailed information on all documented pedestrian stops made by NYPD officers based on the NYPD UF-250 form that they fill out post-stop. The dataset captures demographic and geographic information, factors leading to the stop (e.g., how the stop was initiated, suspected crime), and outcomes from the stop (e.g., frisk, search, arrest). We specifically focus on the most recent dataset from 2025, which has 26,422 records. 

Features we plan on using include the following:
1. "STOP_WAS_INITIATED": Whether a stop was initiated based on criminal weapon on scene, from a radio run, or self-initiated
2. "SUSPECTED_CRIME_DESCRIPTION": Crime that the individual was suspected to have committed
3. "SUSPECT_RACE_DESCRIPTION": Description of the individual's race
4. "FRISKED_FLAG": Whether the individual was frisked
5. "SEARCHED_FLAG": Whether the individual was searched
6. "STOP_LOCATION_PRECINCT": One of 78 police precincts where the stop occurred

The feature we plan on extracting is whether an individual is arrested from the stop ("SUSPECT_ARRESTED_FLAG"). This feature will be used as a label during the training of our model, and will subsequently be the feature that our model will be able to predict based on the given inputs.