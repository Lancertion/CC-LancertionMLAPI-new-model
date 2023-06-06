import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
import tensorflow as tf

np.set_printoptions(formatter={'float': lambda x: "{0:0.5f}".format(x)})


model = tf.keras.models.load_model('data/lungcancer.h5')

train_set = pd.read_csv('data/x.csv')
train_set.drop('Unnamed: 0', axis=1, inplace=True)


def transformed(df):
    s = StandardScaler().fit(train_set)
    X = s.transform(df)
    return X


def predict(df):
    preds = model.predict(df).argmax(axis=1)
    return preds


def get_result(data):
    df = pd.DataFrame({
        'Alcohol use': [data["alcohol_use"]],
        'Dust Allergy': [data["dust_allergy"]],
        'Genetic Risk': [data["genetic_risk"]],
        'Balanced Diet': [data["balanced_diet"]],
        'Obesity': [data["obesity"]],
        'Passive Smoker': [data["smoker"]],
        'Coughing of Blood': [data["coughing_of_blood"]]
    })

    X = transformed(df)
    predictions = predict(X)

    return predictions
