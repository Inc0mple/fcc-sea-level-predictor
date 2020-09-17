import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    x = df["Year"]
    x_extended = pd.Series([i for i in range(1880,2050,1)])

    y = df["CSIRO Adjusted Sea Level"]

    plt.scatter(x,y)
    plt.xlim([1850,2061])
    plt.ylim([-13,16])
    
    # Create first line of best fit
    slope, intercept, r_value, p_value, std_err = linregress(x,y)
    pred = slope*x_extended + intercept
    plt.plot(x_extended, pred, color="red")
    
    #print(linregress(x,y))
    # Create second line of best fit
    x_recent = x[x >= 2000]
    y_recent = y[x >= 2000]
    x_extended2 = pd.Series([i for i in range(2000,2050,1)])
    slope2, intercept2, r_value2, p_value2, std_err2 = linregress(x_recent,y_recent)
    #x_extended2 = pd.Series([i for i in range(1800,2056,1)])
    pred2 = slope2*x_extended2 + intercept2 
    plt.plot(x_extended2, pred2, color="blue")

    # Add labels and title
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")
    #plt.show()
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
draw_plot()