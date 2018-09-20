# Predicting churn for a ride-sharing company
A ride-sharing company (Company X) is interested in predicting rider retention. A sample dataset of users who signed up for an account during January 2014 were provided. Data was pulled on July 1, 2014.

## Defining metrics
Users were considered 'active' if they had taken a trip in the 30 days prior to data extraction (July 1).

As data is proprietary, it has not been included in this repository.

The goal of this analysis was the understand the factors are the best predictors for retaining users and produce suggestions for retaining users.

Below is an example of the information included in this dataset:

```
city: city this user signed up in
phone: primary device for this user
signup_date: date of account registration; in the form `YYYYMMDD`
last_trip_date: the last time this user completed a trip; in the form `YYYYMMDD`
avg_dist: the average distance (in miles) per trip taken in the first 30 days after signup
avg_rating_by_driver: the rider’s average rating over all of their trips
avg_rating_of_driver: the rider’s average rating of their drivers over all of their trips
surge_pct: the percent of trips taken with surge multiplier > 1
avg_surge: The average surge multiplier over all of this user’s trips
trips_in_first_30_days: the number of trips this user took in the first 30 days after signing up
luxury_car_user: TRUE if the user took a luxury car in their first 30 days; FALSE otherwise
weekday_pct: the percent of the user’s trips occurring during a weekday
```

## Process
Full process is detailed in a jupyter notebook entitled `ride-share.ipynb`. A summarized version is provided below:

### Data cleaning

### Model testing

### Model evaluation

### Interpretation

### Limitations of models

### Conclusions

- Code you used to build the model (submit via pull request)

- A (verbal) presentation including the following points:
    - How did you compute the target?
    - What model did you use in the end? Why?
    - Alternative models you considered? Why are they not good enough?
    - What performance metric did you use? Why?
    - Based on insights from the model, what actionable plans do you propose to reduce churn?
