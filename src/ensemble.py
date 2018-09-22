import numpy as np
import pandas as pd
from sklearn.model_selection import KFold
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

class EnsembleModel():
    def __init__(self, clf_list):
        self.clf_list = clf_list

    def fit(self,X,y):
        for clf in self.clf_list:
            clf.fit(X,y)

    def predict(self,X):
        n = len(self.clf_list)
        preds = np.array([clf.predict(X).astype(int) for clf in self.clf_list])
        pred = np.sign((preds.sum(axis=0) - (n // 2)) / n)

        if n % 2 == 1:
            pred[np.where(pred<0)] = 0
        else:
            mask = pred==0
            c = mask.sum()
            nums = np.random.randint(0,2,c)
            pred[mask] = nums
            pred[np.where(pred<0)] = 0
        return pred

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
    df.drop(['churn', 'last_trip_date'], axis=1, inplace=True)
    X = df.values

    return df, X, y

    return df, X, y

def cv_scores(clf, X, y, n_splits=3):
    kf = KFold(n_splits=n_splits)

    accuracies = []
    precisions = []
    recalls = []
    f1_scores = []

    for train, test in kf.split(X):
        X_train, X_test = X[train], X[test]
        y_train, y_test = y[train], y[test]
        clf.fit(X_train,y_train)
        y_pred = clf.predict(X_test)
        accuracies.append(accuracy_score(y_test, y_pred))
        precisions.append(precision_score(y_test, y_pred))
        recalls.append(recall_score(y_test, y_pred))
        f1_scores.append(f1_score(y_test, y_pred))

    accuracies = np.array(accuracies)
    precisions = np.array(precisions)
    recalls = np.array(recalls)
    f1_scores = np.array(f1_scores)

    accuracy = accuracies.mean()
    precision = precisions.mean()
    recall = recalls.mean()
    f1 = f1_scores.mean()

    return accuracy, precision, recall, f1
