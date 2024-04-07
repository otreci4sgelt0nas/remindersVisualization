import pandas as pd
import matplotlib.pyplot as plt

# Load data from CSV
df = pd.read_csv('tasks.csv', parse_dates=['Due Date', 'Completion Date'])

# Count the number of tasks completed each day
completion_counts = df['Completion Date'].value_counts().sort_index()

# Plot
plt.figure(figsize=(10, 6))
completion_counts.plot(kind='bar')
plt.title('Completed Tasks Over Time')
plt.xlabel('Date')
plt.ylabel('Number of Tasks Completed')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
