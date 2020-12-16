# Course: CS261 - Data Structures
# Author: 
# Assignment: #6 - d_graph.py
# Description: Creating various methods for a directed graph


class DirectedGraph:
    """
    Class to implement directed weighted graph
    - duplicate edges not allowed
    - loops not allowed
    - only positive edge weights
    - vertex names are integers
    """

    def __init__(self, start_edges=None):
        """
        Store graph info as adjacency list
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.v_count = 0
        self.adj_matrix = []

        # populate graph with initial vertices and edges (if provided)
        # before using, implement add_vertex() and add_edge() methods
        if start_edges is not None:
            v_count = 0
            for u, v, _ in start_edges:
                v_count = max(v_count, u, v)
            for _ in range(v_count + 1):
                self.add_vertex()
            for u, v, weight in start_edges:
                self.add_edge(u, v, weight)

    def __str__(self):
        """
        Return content of the graph in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        if self.v_count == 0:
            return 'EMPTY GRAPH\n'
        out = '   |'
        out += ' '.join(['{:2}'.format(i) for i in range(self.v_count)]) + '\n'
        out += '-' * (self.v_count * 3 + 3) + '\n'
        for i in range(self.v_count):
            row = self.adj_matrix[i]
            out += '{:2} |'.format(i)
            out += ' '.join(['{:2}'.format(w) for w in row]) + '\n'
        out = f"GRAPH ({self.v_count} vertices):\n{out}"
        return out

    # ------------------------------------------------------------------ #

    def add_vertex(self) -> int:
        """
        Add new vertex to the graph.
        """
        self.v_count += 1
        self.adj_matrix.append([0] * (self.v_count))
        for i in range(self.v_count - 1):
            self.adj_matrix[i].append(0)

        return self.v_count




    def add_edge(self, src: int, dst: int, weight=1) -> None:
        """
        Add edge to the graph
        """
        if(src >= self.v_count or dst >= self.v_count or weight <= 0 or src == dst):
            return

        self.adj_matrix[src][dst] = weight


    def remove_edge(self, src: int, dst: int) -> None:
        """
        Remove edge from the graph
        """
        if src == dst:
            return

        elif dst not in range(0, self.v_count):
            return

        elif src not in range(0, self.v_count):
            return

        self.adj_matrix[src][dst] = 0




    def get_vertices(self) -> []:
        """
        Return list of vertices in the graph (any order)
        """
        index, verts = 0, []
        if self.v_count == 0:
            return verts

        for i in range(0, self.v_count):
            verts.append(index)
            index += 1

        return verts



    def get_edges(self) -> []:
        """
        Return list of edges in the graph (any order)
        """
        edges = []
        if self.v_count == 0:
            return edges

        for i in range(0, self.v_count):
            for j in range(0, self.v_count):
                if self.adj_matrix[i][j] != 0:
                    val = self.adj_matrix[i][j]
                    edge = (i, j, val)
                    edges.append(edge)

        return edges



    def is_valid_path(self, path: []) -> bool:
        """
        Return true if provided path is valid, False otherwise
        """
        for i in range(len(path) - 1):
            if (self.adj_matrix[path[i]][path[i+1]] == 0):
                return False

        return True


    def dfs(self, v_start, v_end=None) -> []:
        """
        Return list of vertices visited during DFS search
        Vertices are picked in increasing number
        """
        stack, visited = [], []
        edges = self.get_edges()
        verts = self.get_vertices()

        if v_start not in verts:
            return visited

        stack.append(v_start)
        current = v_start

        while len(stack) != 0:
            current = stack.pop()
            if current not in visited:
                visited.append(current)
                successors = []

                for i in range(0, len(edges)):
                    if current == edges[i][0]:
                        successors.append(edges[i][1])

                organized = reversed(sorted(successors))

                for i in organized:
                    stack.append(i)

            if current == v_end:
                return visited

        return visited



    def bfs(self, v_start, v_end=None) -> []:
        """
        Return list of vertices visited during BFS search
        Vertices are picked in increasing number
        """
        queue, visited = [], []
        edges = self.get_edges()
        verts = self.get_vertices()

        if v_start not in verts:
            return visited

        queue.append(v_start)
        current = v_start

        while len(queue) != 0:
            current = queue.pop(0)
            if current not in visited:
                visited.append(current)
                successors = []

                for i in range(0, len(edges)):
                    if current == edges[i][0]:
                        successors.append(edges[i][1])

                organized = sorted(successors)

                for i in organized:
                    queue.append(i)

            if current == v_end:
                return visited

        return visited



    def has_cycle(self):
        """
        Return True if graph contains a cycle, False otherwise
        """
        visited, stack, parent_node = [], [], []
        edges = self.get_edges()
        verts = self.get_vertices()

        for i in verts:
            v_start = i
            stack.append(v_start)

            while len(stack) != 0:
                current = stack.pop()
                if current not in visited:
                    visited.append(current)
                    successors = []

                    for i in range(0, len(edges)):
                        if current == edges[i][0]:
                            parent_node.append(edges[i][0])
                            successors.append(edges[i][1])
                    sorted_successors = reversed(sorted(successors))

                    for i in sorted_successors:
                        stack.append(i)

                for vertex in visited:
                    if vertex in stack:
                        if vertex in parent_node:
                            return True
            return False

    def dijkstra(self, src: int) -> []:
        """
        Return shortest distance to all other vertices in the graph
        'inf' if no vertex is reachable
        """




if __name__ == '__main__':
    print("\nPDF - method add_vertex() / add_edge example 1")
    print("----------------------------------------------")
    g = DirectedGraph()
    print(g)
    for _ in range(5):
        g.add_vertex()
    print(g)

    edges = [(0, 1, 10), (4, 0, 12), (1, 4, 15), (4, 3, 3),
             (3, 1, 5), (2, 1, 23), (3, 2, 7)]
    for src, dst, weight in edges:
        g.add_edge(src, dst, weight)
    print(g)


    print("\nPDF - method get_edges() example 1")
    print("----------------------------------")
    g = DirectedGraph()
    print(g.get_edges(), g.get_vertices(), sep='\n')
    edges = [(0, 1, 10), (4, 0, 12), (1, 4, 15), (4, 3, 3),
             (3, 1, 5), (2, 1, 23), (3, 2, 7)]
    g = DirectedGraph(edges)
    print(g.get_edges(), g.get_vertices(), sep='\n')


    print("\nPDF - method is_valid_path() example 1")
    print("--------------------------------------")
    edges = [(0, 1, 10), (4, 0, 12), (1, 4, 15), (4, 3, 3),
             (3, 1, 5), (2, 1, 23), (3, 2, 7)]
    g = DirectedGraph(edges)
    test_cases = [[0, 1, 4, 3], [1, 3, 2, 1], [0, 4], [4, 0], [], [2]]
    for path in test_cases:
        print(path, g.is_valid_path(path))


    print("\nPDF - method dfs() and bfs() example 1")
    print("--------------------------------------")
    edges = [(0, 1, 10), (4, 0, 12), (1, 4, 15), (4, 3, 3),
             (3, 1, 5), (2, 1, 23), (3, 2, 7)]
    g = DirectedGraph(edges)
    for start in range(5):
        print(f'{start} DFS:{g.dfs(start)} BFS:{g.bfs(start)}')


    print("\nPDF - method has_cycle() example 1")
    print("----------------------------------")
    edges = [(0, 1, 10), (4, 0, 12), (1, 4, 15), (4, 3, 3),
             (3, 1, 5), (2, 1, 23), (3, 2, 7)]
    g = DirectedGraph(edges)

    edges_to_remove = [(3, 1), (4, 0), (3, 2)]
    for src, dst in edges_to_remove:
        g.remove_edge(src, dst)
        print(g.get_edges(), g.has_cycle(), sep='\n')

    edges_to_add = [(4, 3), (2, 3), (1, 3), (4, 0)]
    for src, dst in edges_to_add:
        g.add_edge(src, dst)
        print(g.get_edges(), g.has_cycle(), sep='\n')
    print('\n', g)


    print("\nPDF - dijkstra() example 1")
    print("--------------------------")
    edges = [(0, 1, 10), (4, 0, 12), (1, 4, 15), (4, 3, 3),
             (3, 1, 5), (2, 1, 23), (3, 2, 7)]
    g = DirectedGraph(edges)
    for i in range(5):
        print(f'DIJKSTRA {i} {g.dijkstra(i)}')
    g.remove_edge(4, 3)
    print('\n', g)
    for i in range(5):
        print(f'DIJKSTRA {i} {g.dijkstra(i)}')
