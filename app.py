from flask import Flask, render_template, request
from model import predict_reminder

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():

    result = ""

    if request.method == "POST":

        study = int(request.form["study"])
        water = request.form["water"]
        sleep = int(request.form["sleep"])
        break_time = int(request.form["break"])

        prediction = predict_reminder(study, water, sleep, break_time)

        if prediction == 1:
            result = "Reminder Needed"
        else:
            result = "Healthy Routine"

    return render_template("index.html", result=result)


if __name__ == "__main__":
    app.run(debug=True)
