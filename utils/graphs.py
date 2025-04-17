"""
graphs.py

Brendan Dileo, April 2025
"""

import numpy as np
import matplotlib.pyplot as plt
import io

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

    # Save graph to buffer to be used later
    buf = io.BytesIO()
    plt.savefig(buf, format='png')

    return buf

buf = generate_graph(-10, 10, 100)

# Save it to a file for local testing
with open('generated_graph.png', 'wb') as file:
    file.write(buf.read())
    print("Graph saved as 'generated_graph.png'")