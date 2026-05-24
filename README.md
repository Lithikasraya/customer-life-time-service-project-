# Customer Lifetime Value (CLV) Prediction

A Flask-based web application for predicting Customer Lifetime Value using machine learning.

## Repository

**GitHub:** [https://github.com/Lithikasraya/customer-life-time-service-project-.git](https://github.com/Lithikasraya/customer-life-time-service-project-.git)

## Overview

This CLV prediction system helps businesses estimate the total revenue they can expect from customers throughout their relationship. It uses machine learning models trained on customer transaction data to make accurate predictions.

## Features

- User authentication (Login/Sign Up)
- CLV prediction based on customer metrics
- Interactive web interface
- Team member information
- Contact and support pages
- Help documentation

## Technologies Used

- **Backend:** Python, Flask
- **Frontend:** HTML, CSS, JavaScript
- **Machine Learning:** Scikit-learn, NumPy, Pandas
- **Styling:** Responsive CSS with mild, light color scheme

## Installation

1. Clone the repository:
```bash
git clone https://github.com/Lithikasraya/customer-life-time-service-project-.git
cd customer-life-time-service-project-
```

2. Create a virtual environment (optional but recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the application locally:
```bash
python app.py
```

5. Open your browser and navigate to: `http://127.0.0.1:5000`

## Deployment

### Deploy to Google Cloud Platform (App Engine)

1. Install Google Cloud SDK
2. Initialize your project:
```bash
gcloud init
gcloud auth application-default login
```

3. Deploy:
```bash
gcloud app deploy
```

### Deploy to Heroku

1. Install Heroku CLI
2. Login to Heroku:
```bash
heroku login
```

3. Create a new app:
```bash
heroku create your-app-name
```

4. Deploy:
```bash
git push heroku main
```

5. View your app:
```bash
heroku open
```

### Deploy to Other Platforms

The application uses `gunicorn` as the WSGI server and includes configuration for:
- **Procfile** - For Heroku deployment
- **app.yaml** - For Google Cloud App Engine deployment
- **requirements.txt** - All Python dependencies

Ensure your deployment platform can run Python 3.9+ and install dependencies from `requirements.txt`.

## Project Structure

```
KIET-CSC-DS-T5/
├── app.py                           # Main Flask application
├── segmentation_app.py              # Segmentation module
├── README.md                        # Project documentation
├── static/
│   ├── styles.css                   # Main stylesheet
│   ├── app_styles.css              # App-specific styles
│   ├── segmentation_styles.css     # Segmentation styles
│   └── js/
│       └── script.js               # JavaScript utilities
└── templates/
    ├── home.html                   # Home page
    ├── login.html                  # Login page
    ├── signup.html                 # Sign up page
    ├── about.html                  # About page
    ├── contact.html                # Contact page
    ├── help.html                   # Help page
    ├── team.html                   # Team page
    └── result.html                 # Prediction result page
```

## Team

- **Prakash** - prakashrepaka57@gmail.com
- **Lithika Sraya C** - lithikasrayac@gmail.com
- **Satyanarayana** - sg7905568@mail.com
- **Sruthi** - sruthikadali24@gmail.com
- **VenkataRaju** - venkatarajujalligampala@gmail.com

## License

This project is part of KIET-CSC-DS-T5 course work.