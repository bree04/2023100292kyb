INF = 9999

def printA(A):
    vsize = len(A)
    print("====================================")
    for i in range(vsize):
        for j in range(vsize):
            if A[i][j] == INF:
                print(" INF ", end='')
            else:
                print(f"{A[i][j]:4d} ", end='')
        print("")

def reconstruct_path(next_matrix, start, end):
    path = []
    if next_matrix[start][end] is None:
        return path
    while start != end:
        path.append(start)
        start = next_matrix[start][end]
    path.append(end)
    return path

def shortest_path_floyd(vertex, adj):
    vsize = len(vertex)  
    A = [row[:] for row in adj]  
    next_matrix = [[None if adj[i][j] == INF else j for j in range(vsize)] for i in range(vsize)]

    for k in range(vsize):
        for i in range(vsize):
            for j in range(vsize):
                if A[i][k] + A[k][j] < A[i][j]:
                    A[i][j] = A[i][k] + A[k][j]
                    next_matrix[i][j] = next_matrix[i][k]
        printA(A)

    return A, next_matrix

if __name__ == "__main__":
    
    vertex = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    weight = [
        [0,    7,   INF, INF, 3,    10,  INF],
        [7,    0,   4,   10,  2,    6,   INF],
        [INF,  4,   0,   2,   INF,  INF, INF],
        [INF,  10,  2,   0,   11,   9,   4],
        [3,    2,   INF, 11,  0,    13,  5],
        [10,   6,   INF, 9,   13,   0,   INF],
        [INF,  INF, INF, 4,   5,    INF, 0]
    ]

    print("Shortest Path By Floyd's Algorithm")
    A, next_matrix = shortest_path_floyd(vertex, weight)

    start_vertex = input("Start Vertex: ").strip().upper()
    end_vertex = input("End Vertex: ").strip().upper()

    if start_vertex in vertex and end_vertex in vertex:
        start_index = vertex.index(start_vertex)
        end_index = vertex.index(end_vertex)

        path = reconstruct_path(next_matrix, start_index, end_index)
        if path:
            path_vertices = [vertex[i] for i in path]
            print(f"* Shortest Path: {' -> '.join(path_vertices)}")
            print(f"* Distance of the Shortest Path: {A[start_index][end_index]}")
        else:
            print("No path exists between the selected vertices.")
    else:
        print("Invalid vertices.")
