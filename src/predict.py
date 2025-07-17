from entities.Prediction import Prediction
from utils import log

def predict(model, X):
    prediction = model.predict(X)
    prediction_score = float(prediction[0][0])
    log(f"prediction-----------: {prediction_score:.2f}")

    log("keras--------------------")
    print(model.summary())
    
    return (
        Prediction.BUY if prediction_score > 0.6 else
        Prediction.SELL if prediction_score < 0.2 else
        Prediction.NONE
    )