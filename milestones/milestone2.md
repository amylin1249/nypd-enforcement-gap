# Project NYPD Enforcement Gap

## Members
- Haeji Ahn <ahaeji925@uchicago.edu>
- Amy Lin <amyslin@uchicago.edu>
- Amanda Song <amandasong@uchicago.edu>

## Research Question
To what extent do demographic characteristics (e.g, race, age, sex) predict the use of physical force during a police encounter, after controlling for situational factors (e.g., location, why the stop was initiated, the suspected crime) and procedural outcomes (e.g., occurrence of a frisk, occurrence of a search, occurrence of an arrest)?

## Updated Proposal
Using data from the New York Police Department (NYPD), we are studying enforcement patterns, specifically stop, question, and frisk (SQF) actions, in New York City. We plan to analyze the use of physical force based on key features in the dataset, where our classification model will identify which stops lead to physical escalation versus those that do not. By analyzing features such as demographic information (race, age, sex), situational factors (location, why the stop was initiated, suspected crime type), and procedural outcomes (occurrence of a frisk, search, or arrest), we can see how these factors are associated with the severity of enforcement activity. Given the NYPD’s massive budget, finding evidence of a disparity in treatment would suggest that systemic bias, as opposed to underfunding, drives the escalation logic for law enforcement of different populations. The findings would increase transparency on the NYPD’s use of force patterns and highlight any discrepancies in such actions across precincts to interrogate institutional accountability. Machine learning enables us to analyze historical SQF data to identify if certain communities are systematically targeted by intrusive enforcement and to detect patterns of discretionary bias across precincts. This could also provide predictive insights on future enforcement actions, accounting for demographic and precinct-level factors as drivers of systemic outcomes.

## Dataset and Features
Our dataset is an Excel file from the NYPD's Stop, Question, and Frisk database, containing detailed information on all documented pedestrian stops made by NYPD officers based on the NYPD UF-250 form that they fill out post-stop. The dataset captures demographic and geographic information, factors leading to the stop (e.g., how the stop was initiated, suspected crime), and outcomes from the stop (e.g., frisk, search, arrest). We specifically focus on the most recent dataset from 2025, which has 26,422 records. 

Features we plan on using include the following:
1. "SUSPECT_RACE_DESCRIPTION": Description of the individual's race
2. "SUSPECT_REPORTED_AGE": Reported age of the individual
3. "SUSPECT_SEX": Sex of the individual
4. "STOP_LOCATION_PRECINCT": One of 78 police precincts where the stop occurred
5. "STOP_WAS_INITIATED": Whether a stop was initiated based on C/W on scene, from a radio run, or self-initiated
6. "SUSPECTED_CRIME_DESCRIPTION": Crime that the individual was suspected to have committed
7. "FRISKED_FLAG": Whether the individual was frisked
8. "SEARCHED_FLAG": Whether the individual was searched
9. "SUSPECT_ARRESTED_FLAG": Whether the individual was arrested

The feature we plan on extracting is whether an individual experienced use of physical force by the police officer, which we will extract by combining "PHYSICAL_FORCE_CEW_FLAG", "PHYSICAL_FORCE_DRAW_POINT_FIREARM_FLAG", "PHYSICAL_FORCE_HANDCUFF_SUSPECT_FLAG", "PHYSICAL_FORCE_OC_SPRAY_USED_FLAG", "PHYSICAL_FORCE_OTHER_FLAG", "PHYSICAL_FORCE_RESTRAINT_USED_FLAG", and "PHYSICAL_FORCE_WEAPON_IMPACT_FLAG".

Notes: 
1. Run *uv run python process_data.py* in the *src* folder to generate basic statistics and visualizations.
2. We have reached out to the owners of the dataset to get a data dictionary, to ensure that we know exactly what the data reports.