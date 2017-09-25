
# implementation of the graph class
# nodes are numbered from 0 to numNodes - 1
    
class Graph:

    def __init__(self,graphfile):
        # read the graph.txt. file
        lines = [line.strip() for line in open(graphfile)]

        # the first line of the file specified the number of nodes
        self.numNodes = int(lines[0])

        # the rest of the file specifies an edge per line as [node1 node2] to mean that
        # node1 is connected to node2 (which also means that node2 is connected to node1)
        # adjacency matrix A is a matrix with nodes as rows and columns
        # A[node1][node2] = 1 if and only if there is an edge between node1 and node2; clearly, this matrix is symmetric
        self.adjacencyMatrix = [[0 for x in xrange(self.numNodes)] for x in xrange(self.numNodes)]

        # construct adjacency matrix based on the edges specified in the graph file
        for i in range(1,len(lines)):
            edge = lines[i].split(" ")
            a = int(edge[0])
            b = int(edge[1])
            self.adjacencyMatrix[a-1][b-1] = self.adjacencyMatrix[b-1][a-1] = 1

    def valid(self,assignment):
        # checks whether a specific assignment is a valid graph coloring
        'assignment of values to nodes is valid when no pair of nodes connected by an edge is assigned the same color'
        for i in range(len(assignment)):
            for j in range(self.numNodes):
                if self.adjacencyMatrix[i][j] == 1 and assignment[i] == assignment[j]:
                    return False

        return True

    def connected(self,node1,node2):
        'returns True if node1 is connected to node2'
        return self.adjacencyMatrix[node1][node2] == 1

    def getNumNodes(self):
        return self.numNodes
