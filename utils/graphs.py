"""
graphs.py

Brendan Dileo, April 2025
"""

import numpy as np
import matplotlib.pyplot as plt

def generate_graph(start, end, points):
    # x vals between start and end with specified num of points
    x = np.linspace(start, end, points)
    # Linear to test
    y = x  

    # Creates a figure and plot graph
    plt.figure(figsize=(6, 4))
    plt.plot(x, y, label='y = x') 
    plt.title('Basic Graph: y = x')  
    plt.xlabel('x')  
    plt.ylabel('y')  
    plt.grid(True)  
    plt.legend()

    # Save plot as img
    plt.savefig('graph.png') 

    print("Graph saved as 'graph.png'")

# Test
start_value = float(input("Enter the start value for x: "))
end_value = float(input("Enter the end value for x: "))
num_points = int(input("Enter the number of points to plot: "))

generate_graph(start_value, end_value, num_points)
