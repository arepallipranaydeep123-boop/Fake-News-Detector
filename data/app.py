from flask import Flask
from flask import render_template
from flask import request

from predictor import predict_news

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():

    news = request.form["news"]

    result, score = predict_news(news)

    return render_template(
        "index.html",
        result=result,
        score=score
    )

if __name__ == "__main__":
    app.run(debug=True)