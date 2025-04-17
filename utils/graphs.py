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
    x = np.arange(1, 21)

    y_constant = np.ones_like(x)
    y_log = np.log2(x)
    y_linear = x
    y_nlogn = x * np.log2(x)
    y_quad = x**2
    y_exp = 2**x
    y_fact = [math.factorial(i) for i in x]

    # New graph size and labels
    plt.figure(figsize=(12, 6))
    plt.plot(x, y_constant, label="O(1)")
    plt.plot(x, y_log, label="O(log n)")
    plt.plot(x, y_linear, label="O(n)")
    plt.plot(x, y_nlogn, label="O(n log n)")
    plt.plot(x, y_quad, label="O(n²)")
    plt.plot(x, y_exp, label="O(2ⁿ)")
    plt.plot(x, y_fact, label="O(n!)")

    # For readability
    plt.yscale('log')

    plt.title("Time Complexity Comparison")
    plt.xlabel("n")
    plt.ylabel("Operations")
    plt.grid(True, which='both', linestyle='--', linewidth=0.5)
    plt.legend(loc='upper left')
    plt.tight_layout()

    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    return buf

# Generate graph and save to RAM temporarily
buffer = generate_graph(10, 100, 10)
tc_buffer = generate_time_complexity_graph()

# Save graph to a file
with open('graph.png', 'wb') as file:
    file.write(buffer.read())
    print("Graph saved as 'graph.png'")

# Save the time complexity graph
with open('tc_graph.png', 'wb') as file:
    file.write(tc_buffer.read())
    print("Graph was saved as 'tc_graph.png' succesfully!")

# Close buffer to save memory
buffer.close()