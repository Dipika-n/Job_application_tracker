# app.py
from flask import Flask, render_template, request, redirect, url_for
import pandas as pd
import uuid
import os

app = Flask(__name__)

FILE_NAME = 'applications.xlsx'

# Load data
def load_data():
    if os.path.exists(FILE_NAME):
        return pd.read_excel(FILE_NAME)
    else:
        return pd.DataFrame(columns=['Application ID', 'Company Name', 'Job Title', 'Status'])

# Save data
def save_data(df):
    df.to_excel(FILE_NAME, index=False)

#Homepage
@app.route('/')
def home():
    df = load_data()
    status_counts = df['Status'].value_counts().to_dict()
    return render_template('home.html', status_counts=status_counts)

#add new job application
@app.route('/add', methods=['GET', 'POST'])
def add_application():
    if request.method == 'POST':
        #collect form data
        company = request.form['company']
        job_title = request.form['job_title']
        status = request.form['status']
        #Generate unique application id
        app_id = f"APP{uuid.uuid4().hex[:4].upper()}"

        #append new data to existing dataframe
        df = load_data()
        df.loc[len(df)] = [app_id, company, job_title, status]
        save_data(df)

        return redirect(url_for('list_applications'))

    return render_template('add.html')

#Update status of application
@app.route('/update/<app_id>', methods=['GET', 'POST'])
def update_status(app_id):
    df = load_data()
    if request.method == 'POST':
        new_status = request.form['status']
        df.loc[df['Application ID'] == app_id, 'Status'] = new_status
        save_data(df)
        return redirect(url_for('list_applications'))

    app_data = df[df['Application ID'] == app_id].iloc[0]
    return render_template('update.html', application=app_data)

#list all applications
@app.route('/list')
def list_applications():
    df = load_data()

    # Get sorting & filtering values from URL parameters
    sort_by = request.args.get('sort_by', 'Company Name')
    filter_status = request.args.get('status') or None

    # Apply filtering if status is selected
    if filter_status:
        df = df[df['Status'] == filter_status]

    # Apply sorting if column is valid
    if sort_by in df.columns:
        df = df.sort_values(by=sort_by)

    # Pass everything to the template
    return render_template(
        'list.html',
        applications=df.to_dict('records'),
        current_sort=sort_by,
        current_filter=filter_status)

#Delete application
@app.route('/delete/<app_id>')
def delete_application(app_id):
    df = load_data()
    df = df[df['Application ID'] != app_id]  # Keep all except the deleted one
    save_data(df)
    return redirect(url_for('list_applications'))



if __name__ == '__main__':
    app.run(debug=True)
