from flask import Flask, render_template, request, jsonify
import pandas as pd
from sklearn.cluster import KMeans

app = Flask(__name__)

# Load and process the data
def load_and_prepare_data():
    file_path = 'customer_segmentation.csv'
    df = pd.read_csv(file_path, encoding='ISO-8859-1')
    
    # Clean column names
    df.columns = df.columns.str.strip().str.replace(' ', '').str.replace(r'[^\w]', '', regex=True)
    
    # Create TotalAmount column
    if 'TotalAmount' not in df.columns:
        df['TotalAmount'] = df['Quantity'] * df['UnitPrice']
    
    # Convert InvoiceDate to datetime
    df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])
    
    # Create customer-level data
    tx_user = df.groupby('CustomerID').agg({
        'InvoiceDate': lambda x: (pd.Timestamp('2011-12-01') - x.max()).days, # Recency
        'InvoiceNo': 'count',  # Frequency
        'TotalAmount': 'sum'   # Revenue
    }).reset_index()

    tx_user.columns = ['CustomerID', 'Recency', 'Frequency', 'Revenue']
    
    return tx_user

data = load_and_prepare_data()

# Clustering function
def apply_clustering(df):
    kmeans = KMeans(n_clusters=4, random_state=42)
    
    # Recency Clustering
    df['RecencyCluster'] = kmeans.fit_predict(df[['Recency']])
    df['RecencyCluster'] = df['RecencyCluster'].map({0: 3, 1: 2, 2: 1, 3: 0})
    
    # Frequency Clustering
    df['FrequencyCluster'] = kmeans.fit_predict(df[['Frequency']])
    df['FrequencyCluster'] = df['FrequencyCluster'].map({0: 3, 1: 2, 2: 1, 3: 0})
    
    # Revenue Clustering
    df['RevenueCluster'] = kmeans.fit_predict(df[['Revenue']])
    df['RevenueCluster'] = df['RevenueCluster'].map({0: 3, 1: 2, 2: 1, 3: 0})
    
    # Overall Score
    df['OverallScore'] = df['RecencyCluster'] + df['FrequencyCluster'] + df['RevenueCluster']
    
    # Segment Customers
    df['Segment'] = 'Low-Value'
    df.loc[df['OverallScore'] > 3, 'Segment'] = 'Mid-Value'
    df.loc[df['OverallScore'] > 6, 'Segment'] = 'High-Value'
    
    return df

# Apply clustering
data = apply_clustering(data)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get-data', methods=['GET'])
def get_data():
    response = data.to_dict(orient='records')
    return jsonify(response)

@app.route('/get-stats', methods=['GET'])
def get_stats():
    stats = data.groupby('Segment')[['Recency', 'Frequency', 'Revenue']].mean().to_dict()
    return jsonify(stats)

if __name__ == '__main__':
    app.run(debug=True)
