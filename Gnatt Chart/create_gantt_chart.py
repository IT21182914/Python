import pandas as pd

# Define the tasks and their corresponding start and end dates
tasks = {
    "Task": [
        "Research topic selection",
        "Requirement gathering",
        "Study on research area",
        "Topic approval",
        "Project proposal draft submission",
        "Proposal presentation",
        "Research and select technology stack",
        "System planning and design",
        "Collect and prepare training data",
        "Model development and fine-tuning",
        "Model testing and validation",
        "Feature extraction",
        "Behavior analysis and scoring",
        "Progress presentation - 50%",
        "Prepare research paper",
        "Integration with other components",
        "Testing and validation",
        "Progress presentation - 90%",
        "Final thesis with proofreader sign-off",
        "Deployment and feedback",
        "Final presentation",
    ],
    "Start Date": [
        "2024-05-01", "2024-06-01", "2024-07-01", "2024-08-01", 
        "2024-09-01", "2024-10-01", "2024-10-15", "2024-11-01", 
        "2024-12-01", "2025-01-01", "2025-02-01", "2025-03-01", 
        "2025-04-01", "2025-05-01", "2025-06-01", "2025-07-01", 
        "2025-08-01", "2025-09-01", "2025-10-01", "2025-11-01", 
        "2025-12-01"
    ],
    "End Date": [
        "2024-06-01", "2024-07-01", "2024-08-01", "2024-09-01", 
        "2024-10-01", "2024-11-01", "2024-11-01", "2024-12-01", 
        "2025-01-01", "2025-02-01", "2025-03-01", "2025-04-01", 
        "2025-05-01", "2025-06-01", "2025-07-01", "2025-08-01", 
        "2025-09-01", "2025-10-01", "2025-11-01", "2025-12-01", 
        "2026-01-01"
    ],
    "Duration": [
        "1 month", "1 month", "1 month", "1 month", 
        "1 month", "1 month", "2 weeks", "1 month", 
        "1 month", "1 month", "1 month", "1 month", 
        "1 month", "1 month", "1 month", "1 month", 
        "1 month", "1 month", "1 month", "1 month", 
        "1 month"
    ]
}

# Create the DataFrame
df_gantt = pd.DataFrame(tasks)

# Save to Excel
file_path = "AI_Interview_Gantt_Chart.xlsx"
df_gantt.to_excel(file_path, index=False)

print(f"Gantt chart saved to {file_path}")
