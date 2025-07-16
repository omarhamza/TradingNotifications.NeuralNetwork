from utils import log

def predict(model, X):
    prediction = model.predict(X)
    shouldIBuyCrypto = float(prediction[0][0])
    log(f"prediction-----------: {shouldIBuyCrypto:.2f}")

    log("keras--------------------")
    print(model.summary())
    
    return prediction[0][0] >= 0.5