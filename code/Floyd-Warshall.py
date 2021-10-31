class Edge :

    def __init__(self, src, dst, weight) :
        self.src = src
        self.dst = dst
        self.weight = weight

class Graph:

    def __init__(self, arg_nodes):

        self.nodes = arg_nodes
        # Edge weight is a dictionary for storing the weight of the edges { "src-dst" : weight }
        self.edge_list = []        
        # distance is a 2-dimensional array that stores the shortest distance between [src][dst]
        self.distance = [999999999] * arg_nodes
        # next is a 2-dimensional array that stores the node next to the source. This is used
        # for path construction between [src][dst] 
        self.next = [-1] * arg_nodes

        for i in range(arg_nodes):
            self.distance[i] = [999999999] * arg_nodes
            self.next[i] = [-1] * arg_nodes
    
    def AddEdge (self, src, dst, weight, isbidirectional = True):
        e = Edge(src, dst, weight)
        self.edge_list.append(e)
        if (isbidirectional):
            e = Edge(dst, src, weight)
            self.edge_list.append(e)
            
    def Floyd_Warshall(self):

        for i in range (self.nodes):
            self.distance[i][i] = 0
            self.next[i][i] = i

        for edge in self.edge_list:
            weight = edge.weight
            u = edge.src
            v = edge.dst
            self.distance[u][v] = weight
            self.next[u][v] = v


        for k in range(self.nodes):
            for i in range(self.nodes):
                for j in range(self.nodes):
                    if (self.distance[i][j] > self.distance[i][k] + self.distance[k][j]):
                        self.distance[i][j] = self.distance[i][k] + self.distance[k][j]
                        self.next[i][j] = self.next[i][k]

        print("Shortest distance between nodes\n")
        for u in range(self.nodes):
            for v in range(u+1, self.nodes):
                print("Distance ( " + str(u) + " - " + str(v) + " ) : " + str(self.distance[u][v]))
                self.PathConstruction(u, v)
            
    # Construct path from source node to destination node
    def PathConstruction (self, src, dst):

        print("# Path between " + str(src) + " and " + str(dst) + " : ", end = ' ')

        if (self.next[src][dst] == -1):
            print("No path exists")
        else:
            path = []
            path.append(src)

            while (src != dst):
                src = self.next[src][dst]
                path.append(src)

            for node in path:
                print(str(node) + " ", end = ' ')
            print("\n")
            
def main():

    g = Graph(5)

    # Edges from node 0
    g.AddEdge(0, 1, 9)
    g.AddEdge(0, 3, 2)
    g.AddEdge(0, 4, 3)

    # Edges from node 1
    g.AddEdge(1, 2, 3)
    g.AddEdge(1, 4, 7)

    # Edges from node 2
    # Edge from 2 -> 3 is unidirectional. If it was bidirectional, it would introduce negative weight cycle
    # causing the Floyd-Warshall algorithm to fail.
    g.AddEdge(2, 3, -2, False)
    g.AddEdge(2, 4, 1)

    # Edges from node 3
    g.AddEdge(3, 4, 1)

    g.Floyd_Warshall()

if __name__ == "__main__":
    main()
