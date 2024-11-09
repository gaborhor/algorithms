
# ------------- Example of nQueens from which we build graphColoring -------------
# Finds ALL ways to place n non-attacking queens on a n x n board
# NOTE: State[i] is the row for the queen on Column i
# NOTE: There are solutions for n>3

# Stack with list implementation
class MyStack(object):
    def __init__(self, type): # Creates empty list
        self.elemType = type
        self.state = [] # Empty list
    def str (self): # for print
        return str(self.state)
    def empty(self):
        return len(self.state) == 0
    def push(self, elem): # Adds element to the top of stack
        assert type(elem) == self.elemType
        self.state.append(elem)
    def pop(self): # Removes element from the top of stack
        if self.empty():
            raise ValueError("Requested top of an empty stack")
        else:
            return self.state.pop()
    def top(self): # Returns top element of a nonempty stack
        if self.empty():
            raise ValueError("Requested top of an empty stack")
        else:
            return self.state[-1]

def nQueens(n):
    # Each state will include only the queens that have been placed so far
    initialState = [] # Initial empty state

    s = MyStack(list) # For a depth first search
    s.push(initialState) # Push the initial state onto the Stack

    # While we still have states to explore
    while not s.empty():
        currentState = s.pop() # Grab the next state
        currentCol = len(currentState)

        # See if we found a solved state at a leaf node
        # That is, we have filled in every column with a queen
        if currentCol == n:
            print(currentState) # Display the solution
        else:
            # Produce the state's children (if they are feasible)
            # Note children are produced backward so they come off the
            # stack later left to right
            for currentRow in range(n,0,-1):
                # Check horizontal and both diagonals of previous queens
                feasible = True
                for previousCol in range(currentCol):
                    if (currentState[previousCol] == currentRow) or abs(currentState[previousCol]-currentRow) == (currentCol - previousCol):
                        feasible = False
                        break
                if feasible:
                    # Create child by making a copy and appending new col
                    childState = currentState.copy()
                    childState.append(currentRow)
                    s.push(childState) # Push child onto data structure
# # Testing code (check 4,5,6,7)
# for n in range(4,8):
#     nQueens(n)

# -----------------------------------------------------------------------------------------------

def graphColoring(graph, colors):
    num_nodes = len(graph)              # Size of graph
    initial_state = [None] * num_nodes  # Initialize empty state, no colors selected at any node
    # print(initial_state)

    stack = MyStack(list)       # For depth-first search
    stack.push(initial_state)   # Push initial state onto Stack

    while not stack.empty():                    # While we have not found any solution
        current_state = stack.pop()             # Extract most recent state from stack for comparison
        node_to_fill = None                     # Placeholder for 'next node to fill'
        print(f'curr_state: {current_state}')   # Debugging

        for i in range(len(current_state)): # Iterate through current_state to find next node that needs coloring
            if current_state[i] == None:    # If next node not colored
                node_to_fill = i            # Set index of 'node_to_fill' equal to that node's index
                print(f'Node to fill: {node_to_fill}')         # Debugging
                break                       # Exit loop to move to coloring process

        if node_to_fill == None:    # If the previous loop made no change to node_to_fill, then all nodes must be colored
            return current_state    # This is our exit condition for the while-loop, so we return our result

        for color in colors:    # For 'r', 'g', and 'b', perform checks to ensure acceptable placement of colors across graph
            legal = True        # Assume the color will "fit" before we check conditions
            print(f'attempting color: {color}')     # Debugging

            for adjacent in range(node_to_fill + 1):    # For all the nodes from 0 to the 'node_to_fill'
                print(f'checking state of node: {adjacent}')    # Debugging
                # If any nodes are adjacent to our 'node_to_fill' and contain the same color as the one we are testing
                if (graph[node_to_fill][adjacent] == True) and (current_state[adjacent] == color):
                    legal = False   # The color we are testing is no longer legal
                    print(f"adjacent node {adjacent} matches color {color}")    # Debugging
                    break           # Exit the loop that checks other nodes, we need to check other colors instead

            if legal:                               # If we checked all necessary nodes and this color remains legal
                child_state = current_state.copy()  # Create a copy of current_state
                child_state[node_to_fill] = color   # Set the node at this 'node_to_fill' position to the current color
                stack.push(child_state)             # Add this 'child_state' to the stack

    # Handling case in which the while-loop actually empties the stack
    return "stack emptied after depth-first search complete, no solution found"

###################
# Testing Code
###################

# Adjacency matrix representation of a graph
# This particular graph is the one from the videos
graph = [[False, True, False, False, False, True ],
         [True, False, True, False, False, True ],
         [False, True, False, True, True, False],
         [False, False, True, False, True, False],
         [False, False, True, True, False, True ],
         [True, True, False, False, True, False]]
colors = ['r', 'g', 'b']
print(graphColoring(graph, colors))