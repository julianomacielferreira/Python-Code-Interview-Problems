"""
The MIT License

Copyright 2025 Juliano Maciel.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
"""
from collections import defaultdict, deque


class Graph:
    """
    This is an implementation of a Graph class that represents a directed graph and provides methods for adding edges
    and performing a topological sort. Topological sorting is an algorithm that orders the vertices of a directed
    acyclic graph (DAG) so that for each edge (u, v), vertex u comes before vertex v in the sort.
    """

    def __init__(self):
        """
        Initialize an empty graph
        """
        self.graph = defaultdict(list)
        self.in_degree = defaultdict(int)

    def add_edge(self, u, v):
        """
        Add a directed edge from vertex u to vertex v.

        Args:
            u (any): The source vertex.
            v (any): The destination vertex.
        """
        self.graph[u].append(v)
        self.in_degree[v] += 1

        if u not in self.in_degree:
            self.in_degree[u] = 0

    def topological_sort(self):
        """
        Perform a topological sort on the graph.

        Returns:
            list: A list of vertices in topological order.
        """
        queue = deque([v for v in self.in_degree if self.in_degree[v] == 0])
        topological_order = []

        while queue:
            vertex = queue.popleft()
            topological_order.append(vertex)

            for neighbor in self.graph[vertex]:
                self.in_degree[neighbor] -= 1

                if self.in_degree[neighbor] == 0:
                    queue.append(neighbor)

        # If the length of the topological order is not equal to the number of vertices
        if len(topological_order) != len(self.in_degree):
            raise ValueError("Graph contains a cycle and cannot be topologically sorted")

        return topological_order


# Example usage
if __name__ == "__main__":
    graph = Graph()
    graph.add_edge('A', 'B')
    graph.add_edge('A', 'C')
    graph.add_edge('B', 'D')
    graph.add_edge('C', 'D')
    graph.add_edge('D', 'E')

    try:
        topological_order_sorted = graph.topological_sort()
        print("Topological Order:", topological_order_sorted)
    except ValueError as e:
        print(e)
