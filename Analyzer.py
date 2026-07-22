import os
import pandas as pd

output_file = "Tech_Job_Market_Report.xlsx"

# Force delete any corrupt leftovers from previous crashes
if os.path.exists(output_file):
    try:
        os.remove(output_file)
    except PermissionError:
        print(f"[Error] Please close '{output_file}' if it is open in Excel!")

# 1. Create a structured mock dataset
data = {
    "Job_ID": [101, 102, 103, 104, 105, 106, 107, 108],
    "Role": ["Data Analyst", "QA Automation Engineer", "System Administrator", "Data Analyst", 
             "QA Automation Engineer", "IT Operations Specialist", "Business Analyst", "Technical Writer"],
    "Location": ["Salt Lake Sector V", "New Town", "Rajarhat", "Salt Lake Sector V", 
                 "New Town", "Salt Lake Sector V", "New Town", "Remote"],
    "Required_Skill": ["SQL & Excel", "Python & Selenium", "Networking & Git", "PowerBI & SQL", 
                      "Java & Selenium", "Linux & Networking", "Agile & Excel", "Markdown & Git"],
    "Salary_LPA": [4.5, 5.2, 4.0, 4.8, 5.5, 4.2, 6.0, 5.0]
}

df = pd.DataFrame(data)

# 2. Perform Data Analytics and aggregations
print("=== Processing Tech Job Market Data ===")
avg_salary_by_role = df.groupby("Role")["Salary_LPA"].mean().reset_index()
job_count_by_location = df.groupby("Location")["Job_ID"].count().reset_index().rename(columns={"Job_ID": "Openings"})

# 3. Export to a clean, fresh multi-sheet Excel Workbook
with pd.ExcelWriter(output_file, engine="openpyxl") as writer:
    df.to_excel(writer, sheet_name="Raw_Job_Data", index=False)
    avg_salary_by_role.to_excel(writer, sheet_name="Salary_Analysis", index=False)
    job_count_by_location.to_excel(writer, sheet_name="Location_Metrics", index=False)

print(f"\n[Success] Data processed successfully! Created file: '{output_file}'")
print("You can now open this file safely in Microsoft Excel.")
