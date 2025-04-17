"""
graphs.py

Brendan Dileo, April 2025
"""

import io
import math
import numpy as np
import matplotlib.pyplot as plt

def generate_graph(start, end, points):
    # x vals between start and end with specified num of points
    x = np.linspace(start, end, points)
    y = x**2

    # Creates a figure and plot graph
    plt.figure(figsize=(6, 4))
    plt.plot(x, y, label='y = x^2')
    plt.title('Graph: y = x^2')
    plt.xlabel('x')
    plt.ylabel('y')  
    plt.grid(True)
    plt.legend()

    # Save graph to buffer to be used later
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    return buf

def generate_time_complexity_graph():

# Generate graph and save to RAM temporarily
buffer = generate_graph(10, 100, 10)

# Save to a file for local testing
with open('graph.png', 'wb') as file:
    file.write(buffer.read())
    print("Graph saved as 'graph.png'")

buffer.close()