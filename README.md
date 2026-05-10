# Sales Analytics Dashboard

## Project Overview

Sales Analytics Dashboard is an interactive data visualization application built using Streamlit. It allows users to upload CSV files, explore datasets, apply filters, view key performance indicators (KPIs), generate charts, and download filtered data.

This project demonstrates practical skills in Python, data analysis, and dashboard development that are highly relevant for software engineering, data analysis, and business intelligence roles.

---

## Features

- Upload CSV files
- Preview dataset in tabular format
- Display summary statistics
- Filter data by Category and Region
- View key metrics:
  - Total Sales
  - Average Sale
  - Highest Sale
- Generate:
  - Bar chart for Sales by Category
  - Pie chart for Sales by Region
- Download filtered data as CSV

---

## Technologies Used

- Python
- Streamlit
- Pandas
- Matplotlib

---

## Project Structure

dashboard_app/
│
├── app.py
├── requirements.txt
├── sample_sales.csv
└── README.md

---

## Installation

1. Clone the repository:

   git clone https://github.com/your-username/dashboard_app.git

2. Navigate to the project folder:

   cd dashboard_app

3. Install dependencies:

   pip install -r requirements.txt

---

## Running the Application

Run the Streamlit application using:

streamlit run app.py

If the `streamlit` command is not recognized, use:

python -m streamlit run app.py

The application will open in your browser at:

http://localhost:8501

---

## Sample Dataset Format

The application expects a CSV file with columns similar to:

- Date
- Category
- Region
- Sales

Example:

Date,Category,Region,Sales
2026-01-01,Electronics,North,50000
2026-01-02,Furniture,South,22000
2026-01-03,Clothing,East,12000

---

## How to Use

1. Launch the application.
2. Upload a CSV file or use the provided sample dataset.
3. Apply filters from the sidebar.
4. Analyze KPIs and charts.
5. Download the filtered dataset.

---

## Skills Demonstrated

- Python programming
- Data manipulation with Pandas
- Data visualization with Matplotlib
- Dashboard development using Streamlit
- File upload and download functionality
- Interactive filtering and analytics

---

## Use Cases

- Sales reporting
- Business performance analysis
- Inventory monitoring
- Regional trend analysis
- Data exploration

---

## Future Enhancements

- Add authentication system
- Connect to a SQL database
- Support additional chart types
- Export reports to PDF
- Add date range filters
- Deploy to Streamlit Cloud

---

## Interview Questions You Can Answer

1. What is Streamlit and why did you use it?
2. How did you implement file upload functionality?
3. How are KPIs calculated?
4. How does Pandas help in data analysis?
5. What is the purpose of `groupby()`?
6. How does `st.download_button()` work?
7. How would you connect this dashboard to a database?
8. How would you deploy this application?

---

## Author

Amrutha D N
