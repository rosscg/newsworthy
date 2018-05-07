from flask import Flask
from flask import Markup
from flask import Flask
from flask import render_template, request

from compare import run_user_comparison

app = Flask(__name__)


@app.route('/')
def form():
   return render_template('form.html')


@app.route("/chart", methods = ['POST', 'GET'])
def chart():

    if request.method == 'POST':
       form_data = request.form
       screen_name = form_data.get('screen_name')

    data = run_user_comparison(screen_name)

    # Test Data:
    #data = [('Guardian', 8, 1, 3), ('NY Times', 6, 1, 12), ('Bloomberg', 4, 0, 14), ('The Sun', 5, 0, 2), ('Fox News', 2, 0, 1), ('Breitbart', 6, 1, 0)]

    labels = [x[0] for x in data]
    values_agree = [x[1] for x in data]
    values_disagree = [x[2] for x in data]
    values_discuss = [x[3] for x in data]

    height = max(values_agree + values_disagree)
    height_discuss = max(values_discuss)

    return render_template('chart.html', height=height, height_discuss=height_discuss, values_agree=values_agree, values_disagree=values_disagree, values_discuss=values_discuss, labels=labels)



if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5001)
