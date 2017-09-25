#!/usr/bin/python
# use: python run.py <name-of-color-file>

from graph import Graph
from solve import Solve

import sys

# makes sure that the colors file (colors1.txt or colors2.txt) is specified
if (not len(sys.argv) == 2):
    print "Must specify the \'colors\' file name as an argument."
    sys.exit(0)

# extracts the name of the colors file from the command line argument
colorsFile = str(sys.argv[1])

# read the set of allowed colors from the colors file specified on the command line
colors = [line.strip() for line in open(colorsFile)]

# read the graph to color from "graph.txt" file
g = Graph("graph.txt")

# initialize the solver (with graph and the set of colors as input)
solver = Solve(g,colors)

# compute a graph coloring, which is an assignment of colors to nodes in the graph
# if there is no feasible coloring solution, the output is an empty list (assignment = [])
assignment = solver.solve()

# write the assignment (coloring) to the result.txt file
# if assignment is an empty list, output "Infeasible\n" to the result.txt file
f = open('result.txt','w')
    
if not assignment:
    f.write("Infeasible\n")
else:
    for v in assignment:
        f.write(v)
            
    f.write("\n")
