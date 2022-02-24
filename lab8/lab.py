"""6.009 Lab 8: Graphs, Paths, Matrices."""

from abc import ABC, abstractmethod
# NO ADDITIONAL IMPORTS ALLOWED!


class Graph(ABC):
    """Interface for a mutable directed, weighted graph."""

    @abstractmethod
    def add_node(self, node):
        """Add a node to the graph.

        Arguments:
            node (str): the node to add

        Raises:
            ValueError: if the node already exists.

        """

    @abstractmethod
    def add_edge(self, start, end, weight):
        """Add a directed edge to the graph.

        If the edge already exists, then set its weight to `weight`.

        Arguments:
            start (str): the node where the edge starts
            end (str): the node where the edge ends
            weight (int or float): the weight of the edge, assumed to be a nonnegative number

        Raises:
            LookupError: if either of these nodes doesn't exist

        """

    @abstractmethod
    def nodes(self):
        """Return the nodes in the graph.

        Returns:
            set: all of the nodes in the graph

        """

    @abstractmethod
    def neighbors(self, node):
        """Return the neighbors of a node.

        Arguments:
            node (str): a node name

        Returns:
            set: all tuples (`neighbor`, `weight`) for which `node` has an
                 edge to `neighbor` with weight `weight`

        Raises:
            LookupError: if `node` is not in the graph

        """

    @abstractmethod
    def get_path_length(self, start, end):
        """Return the length of the shortest path from `start` to `end`.

        Arguments:
            start (str): a node name
            end (str): a node name

        Returns:
            float or int: the length (sum of edge weights) of the path or
                          `None` if there is no such path.

        Raises:
            LookupError: if either `start` or `end` is not in the graph

        """

    @abstractmethod
    def get_path(self, start, end):
        """Return the shortest path from `start` to `end`.

        Arguments:
            start (str): a node name
            end (str): a node name

        Returns:
            list: nodes, starting with `start` and, ending with `end`, which
                  comprise the shortest path from `start` to `end` or `None`
                  if there is no such path

        Raises:
            LookupError: if either `start` or `end` is not in the graph

        """

    @abstractmethod
    def get_all_path_lengths(self):
        """Return lengths of shortest paths between all pairs of nodes.

        Returns:
            dict: map from tuples `(u, v)` to the length of the shortest path
                  from `u` to `v`

        """

    @abstractmethod
    def get_all_paths(self):
        """Return shortest paths between all pairs of nodes.

        Returns:
            dict: map from tuples `(u, v)` to a list of nodes (starting with
                  `u` and ending with `v`) which is a shortest path from `u`
                  to `v`

        """


class AdjacencyDictGraph(Graph):
    """A graph represented by an adjacency dictionary."""

    def __init__(self):
        """Create an empty graph."""
        self.edges = {}
        self.dist = {}
        self.prec = {}

    def add_node(self, node):
        """Add a node to the graph.

        Arguments:
            node (str): the node to add

        Raises:
            ValueError: if the node already exists.

        """
        if node in self.edges:
            raise ValueError
        else:
            self.edges[node] = set()
            self.dist[(node,node)] = 0
            self.prec[(node,node)] = None

    def add_edge(self, start, end, weight):
        """Add a directed edge to the graph.

        If the edge already exists, then set its weight to `weight`.

        Arguments:
            start (str): the node where the edge starts
            end (str): the node where the edge ends
            weight (int or float): the weight of the edge, assumed to be a nonnegative number

        Raises:
            LookupError: if either of these nodes doesn't exist

        """
        if start in self.edges and end in self.edges:
            self.edges[start].add(end)
            self.dist[(start,end)] = weight
            self.prec[(start,end)] = start
        else:
            raise LookupError

    def nodes(self):
        """Return the nodes in the graph.

        Returns:
            set: all of the nodes in the graph

        """
        return set(self.edges.keys())

    def neighbors(self, node):
        """Return the neighbors of a node.

        Arguments:
            node (str): a node name

        Returns:
            set: all tuples (`neighbor`, `weight`) for which `node` has an
                 edge to `neighbor` with weight `weight`

        Raises:
            LookupError: if `node` is not in the graph

        """
        try:
            return set([(v, self.dist[(node,v)]) for v in self.edges[node]])
        except:
            raise LookupError

    def dijkstra(self, start, end, unvisited):
        if unvisited == set():
            return None
        node = min(unvisited, key=lambda v: self.dist[(start,v)])
        if end != None:
            if self.dist[(start,node)] == float('inf'):
                return False
            if node == end:
                return True
        elif self.dist[(start,node)] == float('inf'):
            return None
        for v in self.edges[node]:
            if v in unvisited:
                if self.dist[(start,node)] + self.dist[(node,v)] < self.dist[(start,v)]:
                    self.dist[(start,v)] = self.dist[(start,node)] + self.dist[(node,v)]
                    self.prec[(start,v)] = self.prec[(node,v)]
        unvisited.remove(node)
        return self.dijkstra(start, end, unvisited)

    def get_path_length(self, start, end):
        """Return the length of the shortest path from `start` to `end`.

        Arguments:
            start (str): a node name
            end (str): a node name

        Returns:
            float or int: the length (sum of edge weights) of the path or
                          `None` if there is no such path.

        Raises:
            LookupError: if either `start` or `end` is not in the graph

        """
        if start not in self.edges or end not in self.edges:
            raise LookupError
        for v in self.edges:
            if (start, v) not in self.dist:
                self.dist[(start,v)] = float('inf')
        if self.dijkstra(start, end, set(self.edges)):
            return self.dist[(start,end)]
        return None

    def get_path(self, start, end):
        """Return the shortest path from `start` to `end`.

        Arguments:
            start (str): a node name
            end (str): a node name

        Returns:
            list: nodes, starting with `start` and, ending with `end`, which
                  comprise the shortest path from `start` to `end` or `None`
                  if there is no such path

        Raises:
            LookupError: if either `start` or `end` is not in the graph

        """
        if start not in self.edges or end not in self.edges:
            raise LookupError
        for v in self.edges:
            if (start, v) not in self.dist:
                self.dist[(start,v)] = float('inf')
        if self.dijkstra(start, end, set(self.edges)):
            path = [end]
            while self.prec[(start,path[-1])] != None:
                path.append(self.prec[(start,path[-1])])
            return path[::-1]
        return None


    def get_all_path_lengths(self):
        """Return lengths of shortest paths between all pairs of nodes.

        Returns:
            dict: map from tuples `(u, v)` to the length of the shortest path
                  from `u` to `v`

        """
        for u in self.edges:
            for v in self.edges:
                if (u, v) not in self.dist:
                    self.dist[(u,v)] = float('inf')
            self.dijkstra(u, None, set(self.edges))
        return {key:self.dist[key] for key in self.dist if self.dist[key] != float('inf')}

    def get_all_paths(self):
        """Return shortest paths between all pairs of nodes.

        Returns:
            dict: map from tuples `(u, v)` to a list of nodes (starting with
                  `u` and ending with `v`) which is a shortest path from `u`
                  to `v`

        """
        paths = {}
        for u in self.edges:
            for v in self.edges:
                if (u, v) not in self.dist:
                    self.dist[(u,v)] = float('inf')
            self.dijkstra(u, None, set(self.edges))
            for v in self.edges:
                if self.dist[(u,v)] != float('inf'):
                    path = [v]
                    while self.prec[(u,path[-1])] != None:
                        path.append(self.prec[(u,path[-1])])
                    paths[(u,v)] = path[::-1]
        return paths


class AdjacencyMatrixGraph(Graph):
    """A graph represented by an adjacency matrix."""

    def __init__(self):
        """Create an empty graph."""
        self.adjacency = []
        self.names = {}
        self.ids = {}
        self.prec = {}
        self.d = []


    def add_node(self, node):
        """Add a node to the graph.

        Arguments:
            node (str): the node to add

        Raises:
            ValueError: if the node already exists.

        """
        if node in self.names:
            raise ValueError
        self.names[node] = len(self.adjacency)
        self.ids[len(self.adjacency)] = node
        for row in self.adjacency:
            row.append(float('inf'))
        next = [float('inf') for i in range(len(self.adjacency))]
        next.append(0)
        self.adjacency.append(next)
        self.d = self.adjacency
        self.prec[(node,node)] = None


    def add_edge(self, start, end, weight):
        """Add a directed edge to the graph.

        If the edge already exists, then set its weight to `weight`.

        Arguments:
            start (str): the node where the edge starts
            end (str): the node where the edge ends
            weight (int or float): the weight of the edge, assumed to be a nonnegative number

        Raises:
            LookupError: if either of these nodes doesn't exist

        """
        if start not in self.names or end not in self.names:
            raise LookupError
        self.adjacency[self.names[start]][self.names[end]] = weight
        self.d = self.adjacency
        self.prec[(start,end)] = start


    def nodes(self):
        """Return the nodes in the graph.

        Returns:
            set: all of the nodes in the graph

        """
        return set(self.names.keys())


    def neighbors(self, node):
        """Return the neighbors of a node.

        Arguments:
            node (str): a node name

        Returns:
            set: all tuples (`neighbor`, `weight`) for which `node` has an
                 edge to `neighbor` with weight `weight`

        Raises:
            LookupError: if `node` is not in the graph

        """
        if node not in self.names:
            raise LookupError
        node_row = self.adjacency[self.names[node]]
        return set([(self.ids[j], node_row[j]) for j in range(len(self.adjacency)) if node_row[j] != float('inf') and self.ids[j] != node])

    def SMM(self, k, n):
        if k >= n-1:
            return self.d
        for i in range(n):
            for j in range(n):
                for l in range(n):
                    if self.d[i][l] + self.d[l][j] < self.d[i][j]:
                        self.d[i][j] = self.d[i][l] + self.d[l][j]
                        self.prec[(self.ids[i],self.ids[j])] = self.prec[(self.ids[l],self.ids[j])]
        return self.SMM(2*k, n)


    def get_path_length(self, start, end):
        """Return the length of the shortest path from `start` to `end`.

        Arguments:
            start (str): a node name
            end (str): a node name

        Returns:
            float or int: the length (sum of edge weights) of the path or
                          `None` if there is no such path.

        Raises:
            LookupError: if either `start` or `end` is not in the graph

        """
        if start not in self.names or end not in self.names:
            raise LookupError
        n = len(self.adjacency)
        l = self.SMM(1, n)[self.names[start]][self.names[end]]
        if l == float('inf'):
            return None
        return l


    def get_path(self, start, end):
        """Return the shortest path from `start` to `end`.

        Arguments:
            start (str): a node name
            end (str): a node name

        Returns:
            list: nodes, starting with `start` and, ending with `end`, which
                  comprise the shortest path from `start` to `end` or `None`
                  if there is no such path

        Raises:
            LookupError: if either `start` or `end` is not in the graph

        """
        if start not in self.names or end not in self.names:
            raise LookupError
        n = len(self.adjacency)
        l = self.SMM(1, n)[self.names[start]][self.names[end]]
        if l == float('inf'):
            return None
        path = [end]
        while self.prec[(start,path[-1])] != None:
            path.append(self.prec[(start,path[-1])])
        return path[::-1]


    def get_all_path_lengths(self):
        """Return lengths of shortest paths between all pairs of nodes.

        Returns:
            dict: map from tuples `(u, v)` to the length of the shortest path
                  from `u` to `v`

        """
        n = len(self.adjacency)
        l = self.SMM(1, n)
        D = {}
        for i in range(n):
            for j in range(n):
                if self.d[i][j] != float('inf'):
                    D[(self.ids[i],self.ids[j])] = self.d[i][j]
        return D


    def get_all_paths(self):
        """Return shortest paths between all pairs of nodes.

        Returns:
            dict: map from tuples `(u, v)` to a list of nodes (starting with
                  `u` and ending with `v`) which is a shortest path from `u`
                  to `v`

        """
        n = len(self.adjacency)
        l = self.SMM(1, n)
        D = {}
        for i in range(n):
            for j in range(n):
                if self.d[i][j] != float('inf'):
                    path = [self.ids[j]]
                    while self.prec[(self.ids[i],path[-1])] != None:
                        path.append(self.prec[(self.ids[i],path[-1])])
                    D[(self.ids[i],self.ids[j])] = path[::-1]
        return D


class GraphFactory:
    """Factory for creating instances of `Graph`."""

    def __init__(self, cutoff=0.5):
        """Create a new factory that creates instances of `Graph`.

        Arguments:
            cutoff (float): the maximum density (as defined in the lab handout)
                            for which the an `AdjacencyDictGraph` should be
                            instantiated instead of an `AdjacencyMatrixGraph`

        """
        self.cutoff = cutoff

    def from_edges_and_nodes(self, weighted_edges, nodes):
        """Create a new graph instance.

        Arguments:
            weighted_edges (list): the edges in the graph given as
                                   (start, end, weight) tuples
            nodes (list): nodes in the graph

        Returns:
            Graph: a graph containing the given edges

        """
        n = len(nodes)
        k = len(weighted_edges)
        if k / (n*(n-1)) > self.cutoff:
            g = AdjacencyMatrixGraph()
        else:
            g = AdjacencyDictGraph()
        for node in nodes:
            g.add_node(node)
        for start,end,weight in weighted_edges:
            g.add_edge(start, end, weight)
        return g

def get_most_central_node(graph):
    """Return the most central node in the graph.

    "Most central" is defined as having the shortest average round trip to any
    other node.

    Arguments:
        graph (Graph): a graph with at least one node from which round trips
                       to all other nodes are possible

    Returns:
        node (str): the most central node in the graph; round trips to all
                    other nodes must be possible from this node

    """
    d = graph.get_all_path_lengths()
    most_central = None
    centrality = float('inf')
    for u in graph.nodes():
        flag = False
        avg = 0
        for v in graph.nodes():
            if u != v:
                if (u,v) not in d or (v,u) not in d:
                    flag = True
                    break
                avg += d[(u,v)] + d[(v,u)]
        if not flag:
            avg = avg / len(graph.nodes())
            if avg < centrality:
                centrality = avg
                most_central = u
    return most_central






if __name__ == "__main__":
    # You can place code (like custom test cases) here that will only be
    # executed when running this file from the terminal.
    pass
