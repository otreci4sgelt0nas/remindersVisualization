import pandas as pd
import matplotlib.pyplot as plt

# Load data from CSV
df = pd.read_csv('tasks.csv', parse_dates=['Due Date', 'Completion Date'])

# Ensure the 'Completion Date' is properly formatted as date (removing time part if present)
df['Completion Date'] = pd.to_datetime(df['Completion Date']).dt.date

# Count the number of tasks completed each day
completion_counts = df['Completion Date'].value_counts().sort_index()

# Create a date range from the earliest to the latest completion date in the data
date_range = pd.date_range(start=completion_counts.index.min(), end=completion_counts.index.max())

# Reindex the completion_counts to include all dates in the date range, filling missing dates with 0
completion_counts = completion_counts.reindex(date_range.date, fill_value=0)

# Plot as an area chart
plt.figure(figsize=(15, 6))
plt.fill_between(date_range, completion_counts, color="skyblue", alpha=0.4)
plt.plot(date_range, completion_counts, color="Slateblue", alpha=0.6, linewidth=2)

plt.title('Completed Tasks Over Time')
plt.xlabel('Date')
plt.ylabel('Number of Tasks Completed')
plt.xticks(rotation=45, ha='right')
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.tight_layout()
plt.show()
