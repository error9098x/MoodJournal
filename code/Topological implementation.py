from collections import deque, defaultdict

class Graph :

    def __init__(self, arg_nodes) :
        self.nodes = arg_nodes
        self.visited = [False] * self.nodes
        # The default dictionary would create an empty list as a default (value) 
        # for the nonexistent keys.
        self.adjlist = defaultdict(list)
        self.stack  = deque()

    def AddEdge(self, src, dst) :
        self.adjlist[src].append(dst)

    def TopologicalSort(self, src) :

        self.visited[src] = True

        # Check if there is an outgoing edge for a node in the adjacency list
        if src in self.adjlist :
            for node in self.adjlist[src] :
                if self.visited[node] == False :
                    self.TopologicalSort(node)

        # Only after all the nodes on the outgoing edges are visited push the
        # source node in the stack
        self.stack.appendleft(src)

    def Traverse(self) :
        for node in range(self.nodes) :
            if self.visited[node] == False :
               self.TopologicalSort(node)

        print("Topological Sorting Order : ", end = ' ')
        while self.stack :
            print(self.stack.popleft(),end=' ')

def main() :

    node_cnt = 7
    g = Graph(node_cnt)

    g.AddEdge(0,2)
    g.AddEdge(0,5)
    g.AddEdge(1,3)
    g.AddEdge(1,6)
    g.AddEdge(2,4)
    g.AddEdge(3,5)
    g.AddEdge(5,2)
    g.AddEdge(5,4)
    g.AddEdge(6,2)

    g.Traverse()

if __name__ == "__main__" :
    main()
