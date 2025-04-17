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
    buf.seek(0)
    return buf

# Generate graph and save to RAM temporarily?
buffer = generate_graph(10, 100, 10)

# ignore graph already
# Save to a file for local testing
with open('graph.png', 'wb') as file:
    file.write(buffer.read())
    print("Graph saved as 'graph.png'")

buffer.close()