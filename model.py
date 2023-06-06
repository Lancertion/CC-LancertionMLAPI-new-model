from tensorflow import keras
from numpy import array


def getCategory(result):
    if (result[0] == 1):
        return "LOW"
    elif result[1] == 1:
        return "MEDIUM"
    else:
        return "HIGH"


def predict(data):
    model = keras.models.load_model("data/1.h5")
    input = array(data).astype(int)

    result = model.predict(input.reshape(1, 23))
    result = result[0].astype(int)

    return getCategory(result)
