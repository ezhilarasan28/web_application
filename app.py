import numpy as np
from flask import Flask, render_template, request
import pickle


app = Flask(__name__)
lreg = pickle.load(open('sal.pkl', 'rb'))


@app.route('/')
def home():
    return render_template('homep.html')


@app.route('/', methods=['GET','POST'])
def homenav():
    data1 = request.form['yrs']
    arr = np.array([[data1]])
    pred = lreg.predict(arr)
    output = round(float(pred[0]), 2)
    return render_template('homep.html', data=output)


if __name__ == "__main__":
    app.run(debug=True)