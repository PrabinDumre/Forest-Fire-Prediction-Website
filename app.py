from flask import Flask, request, render_template, url_for
import pickle
import numpy as np

app = Flask(__name__)

# Load the model
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template("forest_fire.html")

@app.route('/predict', methods=['POST', 'GET'])
def predict():
    if request.method == 'POST':
        int_features = [int(x) for x in request.form.values()]
        final = [np.array(int_features)]
        prediction = model.predict_proba(final)
        output = '{0:.{1}f}'.format(prediction[0][1], 2)

        if float(output) > 0.5:
            return render_template('forest_fire.html', 
                                pred='It is in Danger.\nProbability of fire occurring is {}'.format(output),
                                body_class='danger-bg')
        else:
            return render_template('forest_fire.html',
                                pred='It is safe.\n Probability of fire occurring is {}'.format(output),
                                body_class='safe-bg')
    return render_template('forest_fire.html')

if __name__ == '__main__':
    app.run(debug=True)
