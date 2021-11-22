from flask import Flask, render_template, request
from flask_cors import CORS
from joblib import load
import sklearn
from models import get_history, create_history


pipeline = load("model_classification.joblib")

app = Flask(__name__)
CORS(app)
@app.route('/', methods=["GET", "POST"])
def main():
    if request.method == "POST":
        inp = request.form.get("inp")
        res = pipeline.predict([inp])
        proba= ((pipeline.predict_proba([inp]))[0])[0] * 100
        history = request.form.get("inp")
        history1 = create_history(history)
        percent = " %"

        if res == 1 and proba <= 20:
            return render_template('index.html', message = "Something is fishy but HATE SPEECH is far", pred="Prediction probability is ", prob = proba, percent=percent)
        elif res == 1 and proba <=40:
            return render_template('index.html', message = "WORD or SENTENCE likely to have HATE SPEECH", pred="Prediction probability is ", prob = proba, percent=percent)
        elif res == 1 and proba <= 60:
            return render_template('index.html', message = "SLIGHT HATE SPEECH DETECTED!", pred="Prediction probability is ", prob = proba, percent=percent)
        elif res == 1 and proba <= 80:
            return render_template('index.html', message = "HATE SPEECH IS DETECTED", pred="Prediction probability is ", prob = proba, percent=percent)
        elif res == 1 and proba <= 100:
            return render_template('index.html', message = "HATE SPEECH IS DETECTED DEFINITELY", pred="Prediction probability is ", prob = proba, percent=percent)
        elif res == 0:
            return render_template('index.html', message= "No Hate speech is found", pred= "Prediction probability is ", prob = proba, percent=percent)
        else:
            return render_template('index.html', message= "Nothing is found")
    history2 = get_history()
    return render_template('Index.html', history2=history2[::-1])

if __name__ == '__main__':
    app.run(debug=True)
