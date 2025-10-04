import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    df_scatter = df.copy()
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.scatter(
        data=df_scatter,
        x='Year',
        y='CSIRO Adjusted Sea Level',
        s=5
    )

    # Create first line of best fit
    slope, intercept, r_value, p_value, std_err = linregress(df_scatter['Year'], df_scatter['CSIRO Adjusted Sea Level'])
    x_pred = np.arange(df_scatter['Year'].min(), 2051)
    y_pred = (slope * x_pred) + intercept
    ax.plot(x_pred, y_pred, color='red', alpha=0.3)

    # Create second line of best fit
    df_newline = df.loc[df['Year'] >= 2000]
    slope, intercept, r_value, p_value, std_err = linregress(df_newline['Year'], df_newline['CSIRO Adjusted Sea Level'])
    x_pred_new = np.arange(df_newline['Year'].min(), 2051)
    y_pred_new = (slope * x_pred_new) + intercept
    ax.plot(x_pred_new, y_pred_new, color='green', alpha=0.3)

    # Add labels and title
    ax.grid()
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    ax.set_title('Rise in Sea Level')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()