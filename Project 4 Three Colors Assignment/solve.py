# implements the graph coloring algorithm

from graph import Graph

class Solve:

    def __init__(self,graph,colors):
        self.graph = graph
        self.colors = colors

    def solve(self):
        assignment = []

        'your implementation goes here: return a valid assignment, or an empty array if there is no feasible (valid) assignment'

        # a) check whether there exists a feasible coloring using the path consistency algorithm
        #    output "Feasible" if there is a feasible coloring and "Infeasible" if there is no feasible coloring

        # b) compute a coloring of the graph using the specified colors, or return "Infeasible" if no feasible coloring exists
        if self.inference():
            self.backtrackSearch(assignment)
        return assignment
    def inference(self):
        #check path
        for i in range(2,self.graph.getNumNodes()):
            for j in range(1,i):
                for k in range(0,j):
                    if self.graph.connected(i,j) and self.graph.connected(i,k) and self.graph.connected(j,k) and len(self.colors) <3:
                        return False
        return True

    def backtrackSearch(self,assignment):
        flag = False
        index = 0
        # use the assignWithIndex to store with the index of color to make problem easier
        assignWithIndex = []
        # initial assignment
        for i in range(self.graph.getNumNodes()):
            assignWithIndex.append(0)
            assignment.append('')
        colorNum = len(self.colors)
        while index >= 0:
            while assignWithIndex[index] < colorNum:
                #apply the value to assignment#
                assignment[index] = self.colors[assignWithIndex[index]]
                if self.checkValid(index, assignment):
                    if index == self.graph.getNumNodes() - 1:
                        # get the final answer, finish the loop
                        flag = True
                        break
                    else:
                        #continue to get the next answer
                        index += 1
                        assignWithIndex[index] = 0
                else:
                    # not right, try the next color
                    assignWithIndex[index] += 1
            if flag:
                break
            
            assignWithIndex[index] = 0
            index -= 1
            assignWithIndex[index] += 1
        if not flag:
            #cannot get the right answer
            assignment = []


    def checkValid(self,index,assignment):
        #check current assignment (before index)
        for i in range(index+1):
            for j in range(index+1):
                if self.graph.adjacencyMatrix[i][j] == 1 and assignment[i] == assignment[j]:
                    return False
        return True



        
