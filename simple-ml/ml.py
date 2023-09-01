# import libraries
import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt

# for model creations & evaluations
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# read csv file 
def read_csv():
    return pd.read_csv("diabetes.csv")

# explore data
def data_expore(df):
    print("Columns:")
    print(df.head(), "\n")
    print("Size (y,x):")
    print(df.shape, "\n")
    print("Check null value:")
    print(df.isnull().sum(), "\n")
    print("Check duplicates")
    print(df.duplicated().sum(), "\n")


# Pre-processing
# separate target variables from input variables
def i_o(df):
    x = df[df.columns[:-1]]
    y = df['Outcome'] # df.Outcome
    # print(x, y, sep="\n")

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, stratify=df.Outcome, random_state=123)
    return [x_train, x_test, y_train, y_test]


def compare_model_acc(models, train_test):
    scores = {}
    for name, model in models:
        model.fit(train_test[0], train_test[2])
        y_pred = model.predict(train_test[1])
        scores[name] = accuracy_score(train_test[3], y_pred)
    return scores
    


if __name__ == "__main__":
    models = [
        ('LR', LogisticRegression(solver='liblinear')),
        ('DT', DecisionTreeClassifier()),
        ('RF', RandomForestClassifier(n_estimators=10))
    ]

    diabetes = read_csv()
    # data_expore(diabetes)
    train_test = i_o(diabetes)
    scores = compare_model_acc(models, train_test)
    print(scores)
