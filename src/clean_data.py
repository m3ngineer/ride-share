import pandas as pd
import numpy as np

def clean_data(df):
    df['phone'].fillna(value='Unknown', inplace=True)
    df['last_trip_date'] = pd.to_datetime(df['last_trip_date'])

    df['churn'] = df['last_trip_date'] < '2014-06-01'

    df['no_rating_by_driver'] = df['avg_rating_by_driver'].isnull()
    df['signup_date'] = pd.to_datetime(df['signup_date'])
    df['signup_date'] = pd.to_numeric(df['signup_date'])
    df.drop('signup_date', axis=1, inplace=True)

    mean_rating_by_driver = df['avg_rating_by_driver'].mean()
    mean_rating_of_driver = df['avg_rating_of_driver'].mean()
    df['avg_rating_of_driver'].fillna(mean_rating_of_driver, inplace=True)
    df['avg_rating_by_driver'].fillna(mean_rating_by_driver, inplace=True)
    df['last_trip_date'] = pd.to_numeric(df['last_trip_date'])

    df = pd.get_dummies(df)

    y = df['churn'].values
    X = df.values

    df.drop(['churn', 'last_trip_date'], axis=1, inplace=True)

    return df, X, y
