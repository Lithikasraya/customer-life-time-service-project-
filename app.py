from flask import Flask, render_template, request, redirect, url_for, session, jsonify
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Sample data for training the model
X_train = np.array([[5, 100, 0.8], [10, 200, 0.9], [3, 150, 0.7], [8, 250, 0.85]])
y_train = np.array([5000, 10000, 3000, 8000])

# Train a simple linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('home'))
    return render_template('login.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get input data from the form
    input_data = np.array([[float(request.form['purchase_history']), 
                             float(request.form['average_order_value']), 
                             float(request.form['retention_rate'])]])  # Convert to numpy array




    prediction = model.predict(input_data)
    return render_template('result.html', clv=prediction[0])  # Pass prediction to result.html


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        return redirect(url_for('send_message'))  # Redirect to send_message
    return render_template('contact.html')

@app.route('/send_message', methods=['POST'])
def send_message():
    # Handle the message sending logic here
    return redirect(url_for('home'))

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        return redirect(url_for('login'))
    return render_template('signup.html')

@app.route('/team')
def team():
    return render_template('team.html')
    
@app.route('/about')

def about():
    return render_template('about.html')

@app.route('/help')
def help():
    return render_template('help.html')

if __name__ == '__main__':
    app.run(debug=True)
