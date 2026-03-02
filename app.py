from flask import Flask, render_template, request
import numpy as np

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    prediction = None
    plan = []
    timetable = []

    if request.method == "POST":
        try:
            gpa = float(request.form["gpa"])
            hours = float(request.form["study_hours"])
            absences = int(request.form["absences"])
            tutoring = int(request.form["tutoring"])
            support = int(request.form["support"])

            # Simple scoring logic (instead of ML for now)
            score = gpa*20 + hours*2 - absences*1 + tutoring*5 + support*3

            if score > 80:
                prediction = "Good Performance"
                plan = [
                    "Continue current schedule",
                    "Revise weekly",
                    "Practice mock tests"
                ]
                timetable = [
                    ("6-7 PM", "Revision"),
                    ("7-8 PM", "Practice Questions"),
                    ("8-8:30 PM", "Break"),
                    ("8:30-9:30 PM", "Weak Subject")
                ]

            elif score > 50:
                prediction = "Average Performance"
                plan = [
                    "Increase study hours",
                    "Focus on weak subjects",
                    "Take weekly tests"
                ]
                timetable = [
                    ("5-6 PM", "Concept Study"),
                    ("6-7 PM", "Practice Problems"),
                    ("7-7:30 PM", "Break"),
                    ("7:30-9 PM", "Revision")
                ]
            else:
                prediction = "Needs Improvement"
                plan = [
                    "Study daily",
                    "Get tutoring support",
                    "Follow strict schedule"
                ]
                timetable = [
                    ("4-5 PM", "Basics"),
                    ("5-6 PM", "Practice"),
                    ("6-6:30 PM", "Break"),
                    ("6:30-8 PM", "Homework + Revision")
                ]

        except:
            prediction = "Invalid input"

    return render_template(
        "index.html",
        prediction=prediction,
        plan=plan,
        timetable=timetable
    )


if __name__ == "__main__":
    app.run(debug=True)
