import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
import tensorflow as tf

np.set_printoptions(formatter={'float': lambda x: "{0:0.5f}".format(x)})

# Load the pre-trained machine learning model
model = tf.keras.models.load_model('./lungcancer.h5')

train_set = pd.read_csv('./x.csv')
train_set.drop('Unnamed: 0', axis=1, inplace=True)

# Collect user input

# Function to preprocess user input
# def preprocess_input(train_set):
#     s = preprocessing.StandardScaler().fit(train_set)
#     return s
#     # Perform preprocessing steps, feature engineering, etc.
#     # Return preprocessed input as a DataFrame or array


def transformed(df):
    s = StandardScaler().fit(train_set)
    X = s.transform(df)
    return X


def predict(df):
    preds = model.predict(df).argmax(axis=1)
    return preds


def getResult(data):
    df = pd.DataFrame({
        'Alcohol use': [data["alcohol_use"]],
        'Dust Allergy': [data["dust_allergy"]],
        'Genetic Risk': [data["genetic_risk"]],
        'Balanced Diet': [data["balanced_diet"]],
        'Obesity': [data["obesity"]],
        'Passive Smoker': [data["smoker"]],
        'Coughing of Blood': [data["coughing_of_blood"]]
    })

    print(data)

    X = transformed(df)
    predictions = predict(X)

    return predictions


if __name__ == "__main__":
    # df = pd.DataFrame({
    #     'Alcohol use': [4],
    #     'Dust Allergy': [5],
    #     'Genetic Risk': [7],
    #     'Balanced Diet': [6],
    #     'Obesity': [6],
    #     'Passive Smoker': [4],
    #     'Coughing of Blood': [7]
    # })

    data = {
        "alcohol_use": 4,
        "dust_allergy": 5,
        "genetic_risk": 7,
        "balanced_diet": 6,
        "obesity": 6,
        "smoker": 4,
        "coughing_of_blood": 7,
    }

    print(getResult(data))
