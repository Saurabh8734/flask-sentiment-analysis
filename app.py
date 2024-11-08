from flask import Flask, request, jsonify
import pickle

app = Flask(__name__)

with open("sentiment_model.pkl","rb") as model_file:
    vectorizer, model = pickle.load(model_file)

@app.route("/predict", methods=["POST"])
def predict():
    # Getting text input from request
    data =  request.get_json()
    text =  data.get("text")

    # Transform text input to model format
    text_vector = vectorizer.transform([text])

    # Predict sentiment
    prediction = model.predict(text_vector)[0]

    # Return result
    return jsonify({"sentiment":prediction})


if __name__ == "__main__":
    app.run(debug = True)
