from flask import Flask,request,render_template
import numpy as np
import pandas as pd
import numpy as np
import pickle

## loading the model
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

## loading the power transformer
with open('power_transformer.pkl', 'rb') as f:
    transformer = pickle.load(f)

## loading the scaler.pkl
with open('scaler.pkl', 'rb') as f:
    sc = pickle.load(f)

## create flask app
app = Flask(__name__)


## route
@app.route('/')
def index():
    return render_template("index.html")

@app.route("/predict" , methods=['POST'])
def predict():
    cement = float(request.form['cement'])
    blastFurnace = float(request.form['blastFurnace'])
    flyAsh = float(request.form['flyAsh'])
    water = float(request.form['water'])
    superplasticizer = float(request.form['superplasticizer'])
    courseAggregate = float(request.form['courseAggregate'])
    fineaggregate = float(request.form['fineaggregate'])
    age = int(request.form['age'])

    features = np.array([[cement , blastFurnace,flyAsh ,water,superplasticizer,courseAggregate,fineaggregate,age]])

    ## power transformer
    transformed_input = transformer.transform(features)

    ## scaling
    transformed_input = sc.transform(transformed_input)

    pred = model.predict(transformed_input).reshape(1,-1)

    return render_template('index.html' , strength=pred[0][0])



## python main
if __name__ == "__main__":
    app.run(debug=True)