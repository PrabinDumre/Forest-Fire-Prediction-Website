from flask import Flask, render_template, request
import numpy as np
import pickle
import os

app = Flask(__name__)

# Load the model
model_path = os.path.join(os.path.dirname(__file__), 'model.pkl')
model = pickle.load(open(model_path, 'rb'))

@app.route('/')
def home():
    return render_template('forest_fire.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get values from the form
        oxygen = float(request.form['Oxygen'])
        temperature = float(request.form['Temperature'])
        humidity = float(request.form['Humidity'])
        
        # Make prediction
        prediction = model.predict([[oxygen, temperature, humidity]])
        
        # Format the prediction message
        if prediction[0] == 1:
            pred = 'It is in Danger. Probability of fire occurring is 1.00'
            body_class = 'danger-bg'
        else:
            pred = 'It is Safe. Probability of fire occurring is 0.00'
            body_class = 'safe-bg'
            
        return render_template('forest_fire.html', pred=pred, body_class=body_class)
        
    except Exception as e:
        return render_template('forest_fire.html', pred='Error: Invalid input values')

# Add this for Vercel
if __name__ == '__main__':
    app.run()
