import numpy as np
from flask import Flask, request, render_template
import pickle
from sklearn.preprocessing import PolynomialFeatures

app = Flask(__name__)
loaded_poly = pickle.load(open('sales_poly_model.pkl', 'rb'))
loaded_model = pickle.load(open('poly_converter.pkl', 'rb'))

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/predict',methods=['POST'])
def predict():
    # Get budget amounts for TV, radio, and newspaper ads from form data
    tv1 = int(request.form['TV'])
    radio1 = int(request.form['radio'])
    newspaper1 = int(request.form['newspaper'])
    
    # Transform input using loaded polynomial features
    campaign_poly = loaded_model.transform([[tv1, radio1, newspaper1]])

    # Predict using loaded model
    output = loaded_poly.predict(campaign_poly)

    return render_template('index.html', To_unit_sale_expected='Total expected Unit sell would be $ {}'.format(output))

if __name__ == "__main__":
    app.run(debug=True)