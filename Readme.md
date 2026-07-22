# Automated Tech Job Market Analyzer

A python-based data processing tool that aggregates regional tech job market data, performs metric analysis, and exports structured reports to Microsoft Excel for dynamic dashboard visualization.

## Features
- **Data Generation & Cleaning:** Simulates local market hiring trends (Kolkata tech hubs like Sector V / New Town).
- **Automated Analytics:** Utilizes Python (Pandas) to calculate average packages per role and demand distribution by location.
- **Excel Architecture:** Generates a multi-sheet workbook ready for corporate reporting.

## Tech Stack
- **Language:** Python
- **Libraries:** Pandas, OpenPyXL
- **Visualization:** Microsoft Excel (Pivot Tables, Slicers, Dynamic Charts)
- **Version Control:** Git

## Dashboard Preview
![Dashboard Preview](Dashboard.png)

## Processed Dataset Representation
Below is a structured layout of the data processed by the Python pipeline:

| Job_ID | Role | Location | Required_Skill | Salary_LPA |
| :--- | :--- | :--- | :--- | :--- |
| 1 | Data Analyst | Salt Lake Sector V | SQL & Excel | 4.5 |
| 2 | QA Automation Engineer | New Town | Python & Selenium | 5.2 |
| 3 | System Administrator | Rajarhat | Networking & Git | 4.0 |
| 4 | Data Analyst | Salt Lake Sector V | PowerBI & SQL | 4.8 |
| 5 | QA Automation Engineer | New Town | Java & Selenium | 5.5 |
| 6 | IT Operations Specialist | Salt Lake Sector V | Linux & Networking| 4.2 |
| 7 | Business Analyst | New Town | Agile & Excel | 6.0 |
| 8 | Technical Writer | Remote | Markdown & Git | 5.0 |

## How To Run
1. Install dependencies: `pip install pandas openpyxl`
2. Execute the script: `python analyzer.py`
3. Open `Tech_Job_Market_Report.xlsx` to view the generated data sheets.
