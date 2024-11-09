

# We retain the 'extract_min' function we would use in Dijkstra's Shortest Path, as the key difference is that we will
# simply use the EDGES for the Prim MST, but we can do so with the same method of extracting minima
def extract_min(verts):
    min_index = 0
    for v in range(1,len(verts)):
        if verts[v][1] < verts[min_index][1]:
            min_index = v
    return verts.pop(min_index)


# Modification of Dijkstra's Shortest Path algorithm into Prim's MST algorithm
def prim_MST(graph):
    # Create a list of vertices and their current shortest distances,
    # which would be "inf" as they have not been processed
    num_verts = len(graph)
    # verts_to_process stores lists representing each vertex as
    # ["vertex index", "minimum edge", "vertex connected by min edge"]
    verts_to_process = [[i, float("inf"), -1] for i in range(num_verts)]

    # Start at vertex 0 - it has a current shortest distance of 0 to itself, which we set manually
    verts_to_process[0][1] = 0
    # Start with an empty list of processed vertices/edges
    MST = []

    while len(verts_to_process) > 0:                    # While there remain vertices to process
        # print("to process:",verts_to_process)           # Show all vertices left to process
        current_vert = extract_min(verts_to_process)    # Identify and pop the vertex with the minimum edge value (vert 0 to start)
        MST.append([current_vert[0], current_vert[2]])  # Append that vertex, and the one it connects to, to the MST (0 to itself, denoted by '-1')
        # print(" processed:",MST)                        # Show progress on MST

        for other_vert in verts_to_process:                 # Examine all remaining vertices
            if graph[current_vert[0]][other_vert[0]] > 0:   # Process only those adjacent to 'current_vert' (edge > 0)

                # Update the distances if edge value to vertex is smaller (than "inf" or previous)
                if graph[current_vert[0]][other_vert[0]] < other_vert[1]:
                    other_vert[1] = graph[current_vert[0]][other_vert[0]]   # Set distance to 'other_vert' to edge value from 'graph'
                    other_vert[2] = current_vert[0]                         # Set vertex connected by this edge value

                    # For example, on first iteration of this 'while' loop, we define 'current_vert' a [0, 0, -1] as we
                    #   move it from 'verts_to_process' into the 'MST'.
                    # Then we append [0, -1] to the MST, representing our starting node and what it connects to.
                    # We go on to check remaining 'verts_to_process' that are adjacent to vertex 0.
                    # From the graph we input, vertex 1 is adjacent via edge value of 7, which is obviously 0 < 7 < inf.
                    # We use this edge value to set the "minimum edge" value for vertex 1 in 'verts_to_process'.
                    # Additionally, we use the index of 'current_vert' (currently vertex 0) to set the
                    #   "vertex connected by min edge" for vertex 1 in 'verts_to_process'.
                    #
                    # This process repeats for any vertices which are adjacent to 'current_vert' such that, when we run
                    # 'extract_min()' the following time, we will select the next smallest, adjacent edge value.
                    # In this first case, that will be vertex 1 with an edge value of 7.
    return MST


# Adjacency matrix representation of a graph
# This particular graph is the one from the videos
# The vertices didn't have labels in the videos
# so I'm using the following vertex labels:
#   2
#  / \
# 3---1--7
# |\  |
# 4 | 0--6
#  \|/
#   5

graph = [[0, 7, 0, 0, 0, 10, 15, 0],
        [7, 0, 12, 5, 0, 0, 0, 9],
        [0, 12, 0, 6, 0, 0, 0, 0],
        [0, 5, 6, 0, 14, 8, 0, 0],
        [0, 0, 0, 14, 0, 3, 0, 0],
        [10, 0, 0, 8, 3, 0, 0, 0],
        [15, 0, 0, 0, 0, 0, 0, 0],
        [0, 9, 0, 0, 0, 0, 0, 0]]

print(prim_MST(graph))