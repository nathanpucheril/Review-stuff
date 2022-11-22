from flask import Flask, render_template
from flask import request
import sqlite3

app = Flask(__name__)


@app.route("/", methods=('GET', 'POST'))
def hello_world():
    if request.method == 'POST':
        feedback_string = request.form.get('feedback')
        print(feedback_string)
        return render_template('FeedbackForm.html')
    else:
        return render_template('FeedbackForm.html')

@app.route('feedback/v1/create', methods=('POST'))
def feedback_create():
    pass


# vars: feedback_id, project_id, array[feedback_ids]
@app.route('feedback/v1/get/')
def feedback_bulk_get():
    pass

@app.route('bug_report/v1/create')
def bug_report_create():
    pass


# vars: feedback_id, project_id, array[feedback_ids]
@app.route('bug_report/v1/get/')
def bug_report_bulk_get():
    pass

# TODO
@app.route('feedback/search')
def feedback_get():
    pass


@app.route('feedback/search')
def feedback_get():
    pass



@app.route('feedback/delete')
def __feedback_delete_internal():
    pass


@app.route("/insertFeedback", methods=('GET', 'POST'))
def insert_review():
    return "<p>inserted feedback</p>"


def insert_feedback(feedback):
    return ""


"""start with feedback and bug end points
    recieved either data and put it into a data base
"""

if __name__ == '__main__':
    app.run(debug=False)
