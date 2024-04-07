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
# Convert date_range to date format to match the index of completion_counts
completion_counts = completion_counts.reindex(date_range.date, fill_value=0)

# Plot
plt.figure(figsize=(15, 6))  # Adjusted figure size for better readability
completion_counts.plot(kind='bar', width=1.0, color='skyblue', edgecolor='none')  # Made bars continuous
plt.title('Completed Tasks Over Time')
plt.xlabel('Date')
plt.ylabel('Number of Tasks Completed')

# Customizing x-ticks to show a limited number of date labels for clarity
# Adjust for ZeroDivisionError in case of date_range being too short
tick_spacing = max(1, int(len(date_range) / 10))
tick_labels = [date.strftime('%Y-%m-%d') if i % tick_spacing == 0 else '' for i, date in enumerate(date_range)]
plt.xticks(ticks=range(len(date_range)), labels=tick_labels, rotation=45, ha='right')

plt.grid(axis='y', linestyle='--', linewidth=0.7)  # Added grid for better visibility of counts
plt.tight_layout()
plt.show()
