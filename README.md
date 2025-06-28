
#  Job Application Tracker (Flask + Excel)

A simple web app built with Flask to help you track your job applications. You can easily add, update, search, and manage all your job applications, stored directly in an Excel file.

---

##  Features

-  Add new job applications  
-  Update status (Applied, Interviewed, Offered, Accepted, Rejected)   
-  View all applications with sorting and filtering  
-  Summary of application statuses on the homepage  
-  Flash messages after updates or deletions  
-  Excel-based storage (no database needed)

---

## Technologies used

- **Backend**: Python, Flask  
- **Frontend**: HTML, Bootstrap  
- **Data Storage**: Excel (`applications.xlsx`) using `pandas`

---

##  Project Structure

```
job-application-tracker/
│
├── app.py                # Main Flask app
├── requirements.txt
├── applications.xlsx      # Excel file storing application data
├── templates/             # HTML templates
│   ├── home.html
│   ├── add.html
│   ├── update.html
│   └── list.html
└── README.md              # Project documentation
```


---

##  How to Run This Project Locally

1. **Clone the repository**
   ```bash
   git clone https://github.com/dipikajadhav_2005/job-JobApplicationTracker.git
   cd JobApplicationTracker
   ```

2. **Install the required packages**
   ```bash
   pip install flask pandas openpyxl
   ```

3. **Run the Flask app**
   ```bash
   python app.py
   ```

4. **Open your browser**
   Go to: [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

---

##  Author

**Dipika J.**  

