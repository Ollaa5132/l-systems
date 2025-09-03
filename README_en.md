L-System Visualizations

  This project presents various types of L-systems (Lindenmayer systems) through visualizations using Python and the turtle module. It was created as part of a master’s thesis.

Types of L-Systems
1. D0L L-Systems
Files: DOL_dragon.py, DOL_koch.py, DOL_Sierpinski_triangle.py
Classical deterministic systems that generate well-known fractals such as:
- Heighway’s dragon curve
- Koch curve
- Sierpinski triangle

2. Stochastic L-System
File: stochastic.py
Rules are selected randomly according to predefined probabilities, producing natural-looking fractal trees.

3. Parametric L-System
File: parametric_fern.py
Allows modification of segment lengths at each iteration.
Examples include fern-like leaves or Koch curves with length parameters.

Features
- Generates L-system sequences for a specified number of iterations
- Draws fractals using turtle graphics
- Measures generation and drawing time
- Tracks approximate memory usage
- Allows modification of system parameters directly in the code (no API required)

Usage

1. Install Python (version ≥ 3.8)
2. (Optional) Install dependencies:

pip install memory-profiler

3. Open the .py file corresponding to the desired L-system
4. Modify parameters in the code (axiom, rules, angle, length, iterations)
5. Run the script:

python DOL_dragon.py

6. Watch the fractal drawing in the Turtle window and observe performance results in the terminal

Files
- DOL_dragon.py – Heighway’s dragon curve (D0L)
- DOL_koch.py – Koch curve (D0L)
- DOL_Sierpinski_triangle.py – Sierpinski triangle (D0L)
- stochastic.py – Randomized tree (stochastic)
-parametric_fern.py – Leaves/fern (parametric)
