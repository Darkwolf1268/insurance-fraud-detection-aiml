from flask import Flask,request,jsonify
import pickle

app = Flask(__name__)

model = pickle.load(open("model/model.pkl","rb"))

@app.route("/")
def home():
    return "Insurance Fraud Detection API"

@app.route("/predict",methods=["POST"])
def predict():

    data = request.json["features"]

    prediction = model.predict([data])

    if prediction[0]==1:
        result="Fraud Claim"
    else:
        result="Genuine Claim"

    return jsonify({"prediction":result})

if __name__=="__main__":
    app.run(debug=True)
