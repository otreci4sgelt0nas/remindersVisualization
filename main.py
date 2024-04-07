import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline

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

# Prepare data for spline interpolation
x = np.arange(len(completion_counts))
y = completion_counts.values

# Increase the resolution of the x values for a smoother spline
x_smooth = np.linspace(x.min(), x.max(), 300)

# Create a spline of order 3 (cubic spline)
spl = make_interp_spline(x, y, k=3)
y_smooth = spl(x_smooth)

# Plot
plt.figure(figsize=(15, 6))
plt.plot(date_range, y, 'o', markersize=4, label='Original Data')  # Original data points
plt.plot(np.array(date_range)[x_smooth.astype(int)], y_smooth, label='Spline Fit', color='red')  # Spline approximation

plt.title('Completed Tasks Over Time')
plt.xlabel('Date')
plt.ylabel('Number of Tasks Completed')
plt.xticks(rotation=45, ha='right')
plt.grid(axis='y', linestyle='--', linewidth=0.7)
plt.legend()
plt.tight_layout()
plt.show()
