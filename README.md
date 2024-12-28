# Forest-Fire-Prediction-Website

This project is a web application designed to predict the likelihood of forest fires using a machine learning model. It leverages a dataset and provides an intuitive interface to input key features, which are used to generate fire risk predictions.


# Features
Interactive User Interface: Built using HTML, CSS, and JavaScript for smooth interaction.<br>
Machine Learning Model: Trained to predict forest fires based on relevant features.<br>
Backend with Python: Handles data processing and communication with the machine learning model.<br>
Deployment: Configured for easy deployment on platforms like Google Cloud using app.yaml.<br>

# Repository Structure
app.py: The main backend Python script that handles requests and connects the frontend with the machine learning model.<br>
forest_fire.py: Script responsible for data preprocessing and calling the machine learning model.<br>
model.pkl: Pretrained machine learning model stored as a pickle file.<br>
Forest_fire.csv: The dataset used for training the machine learning model.<br>
templates/: Contains HTML templates for the web pages.<br>
static/: Contains static files such as CSS and JavaScript.<br>
requirements.txt: Lists the Python dependencies required for this project.<br>
app.yaml: Configuration file for deploying the application on platforms like Google Cloud.<br>

# Usage
Enter the required features (such as temperature, humidity, etc.) into the web interface, and the model will predict the likelihood of a forest fire based on the input values.

# License
This project is licensed under the MIT License - see the LICENSE file for details.
